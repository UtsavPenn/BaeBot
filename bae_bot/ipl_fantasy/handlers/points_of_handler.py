from bae_bot.ipl_fantasy.common import determine_player, get_points_from_live_player_points, get_player
from bae_bot.ipl_fantasy.common import simple_table
from bae_bot.ipl_fantasy.data import get_live_data_for_user


def get_live_points():
    live_user_data = get_live_data_for_user('tarunreddy.bethi@gmail.com')
    points = []
    for player_points in live_user_data['playerPoints']:
        _player_points = get_points_from_live_player_points(player_points)
        if _player_points:
            points.append((player_points['playerId'], _player_points))

    return sorted(points, key=lambda x: int(x[1]), reverse=True)

def points_of(bot, update, args):
    live_points = get_live_points()

    if len(args) >= 1:
        query_player = args[0]
        player = determine_player(query_player)

        for live_point in live_points:
            if int(live_point[0]) == int(player.id):
                bot.send_message(update.message.chat_id, "Player - {}: {}".format(player.name, live_point[1]))
                return

        bot.send_message(update.message.chat_id, "Points not found for {}".format(player.name))
        return

    live_points = map(lambda x: (get_player(x[0]).name, x[1]), live_points)
    bot.send_message(update.message.chat_id, simple_table(live_points))
