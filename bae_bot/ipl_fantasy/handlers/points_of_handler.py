from bae_bot.ipl_fantasy.common import determine_player, get_points_from_live_player_points
from bae_bot.ipl_fantasy.data import get_live_data_for_user



def get_live_player_points(player):
    live_user_data = get_live_data_for_user('tarunreddy.bethi@gmail.com')
    for points in live_user_data['playerPoints']:
        if int(points['playerId']) == int(player.id):
            return get_points_from_live_player_points(points)

def points_of(bot, update, args):
    if not args:
        bot.send_message(update.message.chat_id, "Usage: /pointsof thampi")
        return

    query_player = args[0]
    player = determine_player(query_player)
    points = get_live_player_points(player)

    bot.send_message(update.message.chat_id, "Player - {}: {}".format(player.name, points))
