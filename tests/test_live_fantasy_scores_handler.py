from unittest.mock import MagicMock


from bae_bot.ipl_fantasy.handlers.live_fantasy_scores_handler import live_fantasy_scores


def test_live_fantasy_scores_handler(bot, update):
    mock_update = MagicMock()
    mock_update.message.chat_id = 101

    live_fantasy_scores(bot, update, ['tharun'])

    send_message_args = bot.mock_calls[0][1]
    text = send_message_args[1]

    assert "Live Points: " in text
