import functools
from fuzzywuzzy import process

from ipl_fantasy.common import get_ipl_player_to_users_mapping, determine_player
from ipl_fantasy.data import get_players, get_live_data_for_user


def get_live_player_points(player):
    live_user_data = get_live_data_for_user('tarunreddy.bethi@gmail.com')
    for points in live_user_data['playerPoints']:
        if int(points['playerId']) == int(player.id):
            return sum((v for k,v in points.items() if not k.startswith('second') and k.endswith('Points')))

def points_of(bot, update, args):
    if not args:
        bot.send_message(update.message.chat_id, "Usage: /pointsof thampi")
        return

    query_player = args[0]
    player = determine_player(query_player)
    points = get_live_player_points(player)

    bot.send_message(update.message.chat_id, "{}: {}".format(player.name, points))
