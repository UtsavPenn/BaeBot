from bae_bot.ipl_fantasy.handlers.toss_handler import toss

from utils import get_sent_message

def test_toss(bot, update):
    toss(bot, update)

    msg = get_sent_message(bot)
    assert msg
