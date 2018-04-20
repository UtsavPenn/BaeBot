from fuzzywuzzy import process

from ipl_fantasy.common import get_ipl_player_to_users_mapping
from ipl_fantasy.data import get_players


def who_has(bot, update, args):
	if not args:
		bot.send_message(update.message.chat_id, "Usage: /whohas stokes")
		return


	mappings = get_ipl_player_to_users_mapping()
	all_players = [p.name for p in get_players().values()]
	query_player = args[0]

	best_match = process.extractOne(query_player, all_players)
	if not best_match:
		bot.send_message(update.message.chat_id, "Couldn't find match for {}".format(query_player))
		return

	player = best_match[0]
	text = "{} ({}): {}".format(player, best_match[1], ", ".join(mappings.get(player, ['No one'])))
	bot.send_message(update.message.chat_id, text)
