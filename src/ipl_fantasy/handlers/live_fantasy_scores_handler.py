from ipl_fantasy.common import (get_league_team_name_for_user, USER_IDS,
                                simple_table, determine_user,
                                get_total_points_from_live_data, get_player)

from ipl_fantasy.data import get_live_data_for_user

# def _get_player_score_from_points(player):

# 	player_score = player.get('battingPoints', 0) + \
# 					player.get('bowlingPoints', 0) + \
# 					player.get('fieldingPoints', 0) + \
# 					player.get('secondInningBattingPoints', 0) + \
# 					player.get('secondInningBowlingPoints', 0) + \
# 					player.get('secondInningFieldingPoints', 0)

# 	return player_score

# def _get_player_points_table(player_points):
# 	player_points_table = []
# 	for player in player_points:
# 		if not player.get('squadMember'):
# 			continue

# 		score =  _get_player_score_from_points(player)
# 		if not score:
# 			continue
# 		player_name = get_player(player['playerId']).name
# 		print(player_name, player.get('squadMember'))
# 		player_points_table.append((player_name, score))

# 	return sorted(player_points_table, key=lambda x: int(x[1]), reverse=True)


def live_fantasy_scores(bot, update, args):
    if args:
        user = determine_user(args[0])
        live_data = get_live_data_for_user(user)
        bot.send_message(update.message.chat_id,
                         get_total_points_from_live_data(live_data))
    else:
        live_scores = []
        for user in USER_IDS:
            live_data = get_live_data_for_user(user)
            score = get_total_points_from_live_data(live_data)
            live_scores.append((get_league_team_name_for_user(user), score))

        live_scores.sort(key=lambda x: int(x[1]), reverse=True)
        bot.send_message(update.message.chat_id, simple_table(live_scores))
