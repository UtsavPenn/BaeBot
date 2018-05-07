from bae_bot.ipl_fantasy.handlers.mom_handler import mom

from utils import get_sent_message

def test_mom(bot, update):
    mom(bot, update)

    msg = get_sent_message(bot)
    assert msg
