from ipl_fantasy.common import get_league_team_name_for_user, USER_IDS, simple_table
from ipl_fantasy.data import get_live_score_for_user


def get_live_scores():
    live_scores = [(get_league_team_name_for_user(user),
                    get_live_score_for_user(user)) for user in USER_IDS]
    return sorted(live_scores, key=lambda x: int(x[1]), reverse=True)


def live_fantasy_scores(bot, update):
    bot.send_message(update.message.chat_id, simple_table(get_live_scores()))
