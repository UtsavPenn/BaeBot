import tabulate

from bae_bot.fifawc.models import User


def standings(bot, update, args):
    users = User.scan()
    _users = []
    for user in users:
        _users.append((user.user_id, user.total_amount, user.reserved_amount))
    _users = sorted(_users, key=lambda x: x[1])
    _users.insert(0, ("user", "total", 'reserved'))
    bot.send_message(update.message.chat_id, tabulate.tabulate(_users))