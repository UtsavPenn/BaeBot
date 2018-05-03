from bae_bot.ipl_fantasy.common import USER_IDS
from bae_bot.ipl_fantasy.data import get_squad_details
from bae_bot.ipl_fantasy.common import get_league_team_name_for_user
from bae_bot.ipl_fantasy.common import determine_user
from bae_bot.ipl_fantasy.common import simple_table


def _get_mult_left(squad_details):
    return 3 - len(squad_details['doublePointsList'])


def mult_left(bot, update, args):
    mult_left = []

    if args:
        user = determine_user(args[0])
        squad_details = get_squad_details(user)
        bot.send_message(update.message.chat_id, _get_mult_left(squad_details))
        return

    for user_id in USER_IDS:
        squad_details = get_squad_details(user_id)
        mult_left.append((get_league_team_name_for_user(user_id), _get_mult_left(squad_details)))

    mult_left.sort(key=lambda x: int(x[1]), reverse=True)
    resp = "2X left: \n"
    resp += simple_table(mult_left)

    bot.send_message(update.message.chat_id, resp)

