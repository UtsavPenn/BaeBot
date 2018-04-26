from bae_bot.ipl_fantasy.common import get_ipl_player_to_users_mapping, determine_player


def who_has(bot, update, args):

    if not args:
        bot.send_message(update.message.chat_id, "Usage: /whohas stokes")
        return

    mappings = get_ipl_player_to_users_mapping()
    query_player = args[0]

    player = determine_player(query_player)
    if not player:
        bot.send_message(update.message.chat_id,
                         "Couldn't find match for {}".format(query_player))
        return

    text = "{}: {}".format(player.name, ", ".join(mappings.get(player.name, ['No one'])))
    bot.send_message(update.message.chat_id, text)
