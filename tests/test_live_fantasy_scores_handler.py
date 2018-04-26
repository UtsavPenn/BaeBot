from unittest.mock import create_autospec, MagicMock

from telegram.bot import Bot

from bae_bot.ipl_fantasy.handlers.live_fantasy_scores_handler import live_fantasy_scores


def test_live_fantasy_scores_handler():
    mock_bot = create_autospec(Bot, instance=True)
    mock_update = MagicMock()
    mock_update.message.chat_id = 101

    live_fantasy_scores(mock_bot, mock_update, ['tharun'])

    bot_calls = mock_bot.mock_calls[0][1]
    assert "Live Points: " in bot_calls[1]
