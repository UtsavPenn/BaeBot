def get_sent_message(bot):
    send_message_args = bot.mock_calls[0][1]
    text = send_message_args[1]
    return text
