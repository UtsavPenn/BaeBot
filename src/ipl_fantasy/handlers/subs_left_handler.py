from ipl_fantasy.data import get_squad_details
from ipl_fantasy.common import USER_IDS, get_league_team_name_for_user, simple_table, determine_user


def get_subs_left_for_user(user_id):
    transfers = get_squad_details(user_id)['transfersRemaining']
    return transfers


def get_subs_left():
    subs_left = [(get_league_team_name_for_user(user),
                  get_subs_left_for_user(user)) for user in USER_IDS]
    return sorted(subs_left, key=lambda x: int(x[1]), reverse=True)


def subs_left(bot, update, args):
    if args:
        user = determine_user(args[0])
        bot.send_message(update.message.chat_id, get_subs_left_for_user(user))
    else:
        bot.send_message(update.message.chat_id, simple_table(get_subs_left()))
