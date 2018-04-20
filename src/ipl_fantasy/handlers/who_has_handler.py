from fuzzywuzzy import process

from ipl_fantasy.common import get_ipl_player_to_users_mapping


def who_has(bot, update, args):
	if not args:
		bot.send_message(update.message.chat_id, "Usage: /whohas stokes")
		return

	mappings = get_ipl_player_to_users_mapping()
	all_players = mappings.keys()
	query_player = args[0]

	best_match = process.extractOne(query_player, all_players)
	if not best_match:
		bot.send_message(update.message.chat_id, "Couldn't find match for {}".format(query_player))
		return

	player = best_match[0]
	bot.send_message(update.message.chat_id, player + ": " + ",".join(mappings.get(player)))
