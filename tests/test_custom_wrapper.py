from unittest.mock import create_autospec, MagicMock
from telegram.bot import Update, Bot
from bae_bot.wrappers.custom_command_handler import CustomCommandHandler


def test_sample_handler():
    mock_bot = create_autospec(Bot, instance=True)
    mock_update = MagicMock()
    mock_update.message.chat_id = 101

    def call_back(bot, update):
        bot.send_message(update.message.chat_id, 'Hello')

    test_handler = CustomCommandHandler('test', call_back)
    test_handler.handle_update(mock_update, mock_bot)

    mock_bot.send_message.assert_called_with(101, 'Hello')


