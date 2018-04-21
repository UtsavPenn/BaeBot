from ipl_fantasy.common import (get_league_team_name_for_user, USER_IDS,
                                simple_table, determine_user, get_total_score_so_far_for_user)
from ipl_fantasy.data import get_live_score_for_user, get_league_details



def get_live_total_scores(args=None):
    live_total_scores = {
        _user: get_total_score_so_far_for_user(_user)
        for _user in USER_IDS
    }
    if args:
        user = determine_user(args[0])
        user_score = live_total_scores.get(user)
        live_total_scores = {
            _user: score - user_score
            for _user, score in live_total_scores.items()
        }
    live_total_scores = {get_league_team_name_for_user(user): score for user, score in live_total_scores.items()}
    return sorted(
        live_total_scores.items(), key=lambda x: int(x[1]), reverse=True)


def cumulative_scores(bot, update, args):
    bot.send_message(update.message.chat_id,
                     simple_table(get_live_total_scores(args)))
