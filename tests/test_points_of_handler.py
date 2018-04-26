from unittest.mock import create_autospec, MagicMock

from telegram.bot import Bot

from bae_bot.ipl_fantasy.handlers.points_of_handler import points_of


def test_points_of_handler(bot, update):

    points_of(bot, update, ['shakib'])

    send_message_args = bot.mock_calls[0][1]
    text = send_message_args[1]
    assert "Player" in text
