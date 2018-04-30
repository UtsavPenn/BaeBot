import arrow
import pytz

from bae_bot.ipl_fantasy.common import determine_team, team_short_name
from bae_bot.ipl_fantasy.data import get_matches
from ipl_fantasy.common import simple_table


def _is_int(arg):
    try:
        int(arg)
        return True
    except ValueError:
        return False


def schedule(bot, update, args):
    all_matches = get_matches()

    pacific_tz = pytz.timezone('US/Pacific')
    now = arrow.now().astimezone(pacific_tz)

    resp = "Next matches: \n"
    next_matches = [match for match in all_matches if arrow.get(match.starttime).astimezone(pacific_tz) > now]

    if args:
        if _is_int(args[0]):
            n = int(args[0])
            resp = "Next {} matches: \n".format(n)
            next_matches = next_matches[:n]
        else:
            team = determine_team(args[0])
            resp = "Next {} matches: \n".format(team)
            next_matches = [match for match in next_matches if team in match.teams]

    matches_table = []
    for match in next_matches:
        row = [str(arrow.get(match.starttime).astimezone(pacific_tz).date())[5:]]
        row.extend(list(map(team_short_name, match.teams)))
        matches_table.append(row)

    resp += simple_table(matches_table)
    bot.send_message(update.message.chat_id, resp)
