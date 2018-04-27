from utils import get_sent_message

from bae_bot.ipl_fantasy.handlers.subs_left_handler import subs_left


def test_points_of_handler_with_args(bot, update):
    subs_left(bot, update, [])
    assert "Matches left" in get_sent_message(bot)
