import tabulate

from bae_bot.fifawc.models import User
from bae_bot.fifawc.data import get_league_info


def standings(bot, update, args):
    users = User.scan()
    _users = []
    for user in users:
        _users.append((user.user_id, round(user.total_amount, 2), round(user.reserved_amount, 2)))
    _users = sorted(_users, key=lambda x: x[1], reverse=True)
    _users.insert(0, ("user", "total", 'reserved'))
    bot.send_message(update.message.chat_id, tabulate.tabulate(_users))

    league_info = get_league_info()
    players = [(p['FullName'], p['Rank']) for p in league_info['Rest']]
    bot.send_message(update.message.chat_id, tabulate.tabulate(players))
