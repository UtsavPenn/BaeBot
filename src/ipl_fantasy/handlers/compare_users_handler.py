from ipl_fantasy.common import determine_user, get_player
from ipl_fantasy.data import get_squad_details


def get_players_of(user):
    return set([get_player(p).name for p in get_squad_details(user)['players']])


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

    resp = ""

    user1_players = get_players_of(user1)
    user2_players = get_players_of(user2)

    resp += "Common Players: {} \n\n".format(", ".join(user1_players & user2_players))
    resp += "{} - {}: {} \n\n".format(args[0], args[1], ", ".join(user1_players - user2_players))
    resp += "{} - {}: {} \n\n".format(args[1], args[0], ", ".join(user2_players - user1_players))

    bot.send_message(
        chat_id=update.message.chat_id,
        text=resp)
