import arrow
import pytz
import tabulate

from bae_bot.ipl_fantasy.common import determine_user, get_player, determine_team
from bae_bot.ipl_fantasy.data import get_squad_details, get_matches


def players_of(bot, update, args):
    if not args:
        bot.send_message(update.message.chat_id, "Usage: /playersof badri mi")
        return

    user = determine_user(args[0])
    squad_details = get_squad_details(user)
    players = [get_player(p) for p in squad_details['players']]

    if len(args) > 1:
        teams = list(map(determine_team, args[1:]))
        players = [p for p in players if p['team'] in teams]

    player_names = []
    for player in players:
        if int(player.id) == squad_details['powerPlayer']:
            player_names.append(player.name+"(PP)")
        elif int(player.id) == squad_details['secondPowerPlayer']:
            player_names.append(player.name+"(SPP)")
        else:
            player_names.append(player.name)

    if not player_names:
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
                players_table.append((player.name, next_opportunity))
                break

    message = tabulate.tabulate(players_table, headers=['Player', 'nextopportunityin'])
    resp = "Total Players: {} \n".format(len(players_table))
    resp += message

    bot.send_message(update.message.chat_id, resp)
