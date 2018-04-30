import arrow
import pytz
from tabulate import tabulate

from bae_bot.ipl_fantasy.common import team_short_name
from bae_bot.ipl_fantasy.common import determine_player
from bae_bot.ipl_fantasy.data import get_matches


def next_opportunities(bot, update, args):
    if not args:
        bot.send_message(update.message.chat_id, "Usage: /nextin bravo")
        return

    player = determine_player(args[0])
    all_matches = get_matches()

    pacific_tz = pytz.timezone('US/Pacific')
    now = arrow.now().astimezone(pacific_tz)

    next_opportunity = 0
    opps = []

    for match in all_matches:
        starttime = arrow.get(match.starttime).astimezone(pacific_tz)
        if now > starttime:
            continue

        next_opportunity += 1
        if player.team in match.teams:
            # This is tricky but basically finds the complement in the list
            opposing_team = match.teams[int(not match.teams.index(player.team))]

            opps.append((str(starttime.date()), team_short_name(opposing_team), next_opportunity))

    resp = "Player: {} \n".format(player.name)
    resp += tabulate(opps, headers=('date', 'vs', 'matches to go'))
    bot.send_message(update.message.chat_id, resp)
