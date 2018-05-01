from utils import get_sent_message

from bae_bot.ipl_fantasy.handlers.top_picks_handler import top_picks


def test_top_picks_handler_with_args(bot, update):
    top_picks(bot, update, ['mi'])
    assert "Players" in get_sent_message(bot)


def test_top_picks_handler_without_args(bot, update):
    top_picks(bot, update, [])
    assert "Players" in get_sent_message(bot)
