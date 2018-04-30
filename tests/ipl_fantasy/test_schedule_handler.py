from utils import get_sent_message

from bae_bot.ipl_fantasy.handlers.schedule_handler import schedule


def test_schedule_without_args(bot, update):
    schedule(bot, update, [])
    msg = get_sent_message(bot)

    assert "Next matches:" in msg


def test_schedule_with_number(bot, update):
    schedule(bot, update, ['6'])
    msg = get_sent_message(bot)

    assert "Next 6 matches:" in msg


def test_schedule_with_team(bot, update):
    schedule(bot, update, ['sh'])
    msg = get_sent_message(bot)

    assert "Next sunrisers-hyderabad matches:" in msg
