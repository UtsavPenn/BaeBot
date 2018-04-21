from ipl_fantasy.data import get_points_history_for_user
from ipl_fantasy.common import simple_table, determine_user


def get_user_points_history(user_id):
	points_per_match = []
	points_history = get_points_history_for_user(user_id)['pointsHistory']
	match_number = 1;
	for points in points_history:
		total_points = int(points['btP']) + int (points['boP']) + int (points['fP']) + int (points['mP']) + int (points['wP'])
		points_per_match.append(('MatchNo:'+ str(match_number),total_points))
		match_number = match_number + 1
	return points_per_match


def historical_points(bot, update, args):
    if args:
        user = determine_user(args[0])
        bot.send_message(update.message.chat_id, get_user_points_history(user))
    else:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Please specify a user")
