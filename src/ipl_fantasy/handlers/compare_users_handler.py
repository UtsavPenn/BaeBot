from ipl_fantasy.common import determine_user, get_player
from ipl_fantasy.data import get_squad_details


def get_common_players(user1, user2):
    user1_players = get_squad_details(user1)['players']
    user2_players = get_squad_details(user2)['players']
    common_players = set(user1_players) & set(user2_players)
    return [get_player(player).name for player in common_players]


def compare_users(bot, update, args):
    if not len(args) > 1:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Example usage: /compare tharun utsav")
        return

    user1 = determine_user(args[0])
    if not user1:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Unable to determine user {}".format(args[0]))
        return

    user2 = determine_user(args[1])
    if not user2:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Unable to determine user {}".format(args[1]))
        return

    bot.send_message(
        chat_id=update.message.chat_id,
        text="Common Players: " + ", ".join(get_common_players(user1, user2)))
