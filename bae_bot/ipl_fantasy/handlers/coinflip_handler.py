import random


def coinflip(bot, update, args):
    if not args:
        bot.send_message(update.message.chat_id, random.choice(['heads', 'tails']))
        return

    bot.send_message(update.message.chat_id, random.choice(args))