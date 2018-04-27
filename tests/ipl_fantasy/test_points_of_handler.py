from utils import get_sent_message

from bae_bot.ipl_fantasy.handlers.points_of_handler import points_of


def test_points_of_handler_with_args(bot, update):
    points_of(bot, update, ['shakib'])
    assert "Points not" in get_sent_message(bot)


def test_points_of_handler_without_args(bot, update):
    points_of(bot, update, [])
    assert "------------" in get_sent_message(bot)
