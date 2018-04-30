from bae_bot.ipl_fantasy.handlers.next_opportunities_handler import next_opportunities

from utils import get_sent_message


def test_next_in(bot, update):
    next_opportunities(bot, update, ['kohli'])

    msg = get_sent_message(bot)
    assert len(msg) > 2
    assert "date" in msg


