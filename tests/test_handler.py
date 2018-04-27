from unittest.mock import patch

from bae_bot.handler import main


def test_handler(bot, event):
    with patch('bae_bot.handler.bot', bot):
        main(event, None)

        send_message_args = bot.mock_calls[-1][1]
        text = send_message_args[1]

        assert "Ask me" in text

