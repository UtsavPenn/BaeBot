from ipl_fantasy.data import get_squad_details
from ipl_fantasy.common import (USER_IDS, get_league_team_name_for_user,
                                simple_table, determine_user,
                                get_total_score_so_far_for_user)


def get_sub_strike_rate_for_user(user_id):
    transfers_used = 75 - get_squad_details(user_id)['transfersRemaining']
    points = get_total_score_so_far_for_user(user_id)
    return round(points / transfers_used, 3)


def get_sub_strike_rates():
    sub_strike_rates = [(get_league_team_name_for_user(user),
                         get_sub_strike_rate_for_user(user))
                        for user in USER_IDS]
    return sorted(sub_strike_rates, key=lambda x: int(x[1]), reverse=True)


def sub_strike_rate(bot, update, args):
    if args:
        user = determine_user(args[0])
        bot.send_message(update.message.chat_id,
                         get_sub_strike_rate_for_user(user))
    else:
        bot.send_message(update.message.chat_id,
                         simple_table(get_sub_strike_rates()))
