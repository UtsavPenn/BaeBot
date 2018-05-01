from utils import get_sent_message

from bae_bot.ipl_fantasy.handlers.stats_of_handler import stats_of


def test_stats__of_handler_with_args(bot, update):
    stats_of(bot, update, ['shakib'])
    assert "Points not" in get_sent_message(bot)


def test_stats__of_handler_without_args(bot, update):
    stats_of(bot, update, [])
    assert "Usage" in get_sent_message(bot)
