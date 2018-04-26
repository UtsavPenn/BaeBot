from unittest.mock import create_autospec, MagicMock

from telegram.bot import Bot

from bae_bot.ipl_fantasy.handlers.points_of_handler import points_of


def test_points_of_handler():
    mock_bot = create_autospec(Bot, instance=True)
    mock_update = MagicMock()
    mock_update.message.chat_id = 101

    points_of(mock_bot, mock_update, ['shakib'])

    bot_calls = mock_bot.mock_calls[0][1]
    assert "Player" in bot_calls[1]
