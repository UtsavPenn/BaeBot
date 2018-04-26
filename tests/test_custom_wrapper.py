from bae_bot.wrappers.custom_command_handler import CustomCommandHandler


def test_sample_handler(bot, update):
    def call_back(bot, update):
        bot.send_message(update.message.chat_id, 'Hello')

    test_handler = CustomCommandHandler('test', call_back)
    test_handler.handle_update(update, bot)

    bot.send_message.assert_called_with(101, 'Hello')


