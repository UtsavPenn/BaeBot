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
    players = [get_player(p) for p in get_squad_details(user)['players']]

    if len(args) > 1:
        team = determine_team(args[1])
        players = [p for p in players if p['team'] == team]

    player_names = [p.name for p in players]

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

    bot.send_message(update.message.chat_id, message)
