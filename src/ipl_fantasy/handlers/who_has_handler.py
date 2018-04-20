import functools
from fuzzywuzzy import process

from ipl_fantasy.common import get_ipl_player_to_users_mapping
from ipl_fantasy.data import get_players


@functools.lru_cache()
def get_best_match(query_player):
    all_players = [p.name for p in get_players().values()]
    best_match = process.extractOne(query_player, all_players)
    return best_match


def who_has(bot, update, args):
    if not args:
        bot.send_message(update.message.chat_id, "Usage: /whohas stokes")
        return

    mappings = get_ipl_player_to_users_mapping()
    query_player = args[0]

    best_match = get_best_match(query_player)
    if not best_match:
        bot.send_message(update.message.chat_id,
                         "Couldn't find match for {}".format(query_player))
        return

    player = best_match[0]
    text = "{} ({}): {}".format(player, best_match[1], ", ".join(
        mappings.get(player, ['No one'])))
    bot.send_message(update.message.chat_id, text)
