from ipl_fantasy.data import get_squad_details
from ipl_fantasy.common import (USER_IDS, get_league_team_name_for_user,
                                simple_table, determine_user)


def get_stealth_left_for_user(user_id):
    stealth = 5 - len(get_squad_details(user_id)['stealthList'])
    return stealth


def get_stealths_left():
    stealths = [(get_league_team_name_for_user(user),
                 get_stealth_left_for_user(user)) for user in USER_IDS]
    return sorted(stealths, key=lambda x: int(x[1]), reverse=True)


def stealths_left(bot, update, args):
    if args:
        user = determine_user(args[0])
        bot.send_message(update.message.chat_id,
                         get_stealth_left_for_user(user))
    else:
        bot.send_message(update.message.chat_id,
                         simple_table(get_stealths_left()))
