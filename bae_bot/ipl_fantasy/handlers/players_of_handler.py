import arrow
import pytz
import tabulate

from bae_bot.ipl_fantasy.common import determine_user, get_player, determine_team
from bae_bot.ipl_fantasy.data import get_squad_details, get_matches

def _get_player_name(player, squad_details):
    if int(player.id) == squad_details['powerPlayer']:
        return player.name + "(PP)"

    if int(player.id) == squad_details['secondPowerPlayer']:
        return player.name + "(SPP)"

    return player.name

def players_of(bot, update, args):
    # bot.send_message(update.message.chat_id, "Stealth for life!")
    # return
    if not args:
        bot.send_message(update.message.chat_id, "Usage: /playersof badri mi")
        return

    user = determine_user(args[0])
    squad_details = get_squad_details(user)
    players = [get_player(p) for p in squad_details['players']]

    if len(args) > 1:
        teams = list(map(determine_team, args[1:]))
        players = [p for p in players if p['team'] in teams]

    if not players:
        bot.send_message(update.message.chat_id, "No players")
        return

    players_table = []

    pacific_tz = pytz.timezone('US/Pacific')
    now = arrow.now().astimezone(pacific_tz)
    matches = get_matches()
    for player in players:
        next_opportunity = 0
        for match in matches:
            starttime = arrow.get(match.starttime).astimezone(pacific_tz)
            if now > starttime:
                continue
            next_opportunity += 1
            if player.team in match.teams:
                break
        players_table.append((_get_player_name(player, squad_details), next_opportunity))

    message = tabulate.tabulate(players_table, headers=['Player', 'nextopportunityin'])
    resp = "Total Players: {} \n".format(len(players_table))
    resp += message

    bot.send_message(update.message.chat_id, resp)
