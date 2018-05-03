from bae_bot.ipl_fantasy.handlers.mult_left_handler import mult_left

from utils import get_sent_message

def test_mult_left_without_args(bot, update):
    mult_left(bot, update, [])

    msg = get_sent_message(bot)
    assert "2X left: " in msg


def test_mult_left_with_args(bot, update):
    mult_left(bot, update, ['tharun'])

    msg = get_sent_message(bot)
    assert int(msg) >= 0


