from pynamodb.exceptions import DoesNotExist

from bae_bot.fifawc.models import User


def join(bot, update):
    first_name = update.effective_user.first_name
    try:
        User.get(update.effective_user.first_name)
        bot.send_message(update.message.chat_id, "{} already joined".format(first_name))
    except DoesNotExist:
        user = User(first_name, total_amount=25, reserved_amount=0)
        user.save()
        bot.send_message(update.message.chat_id, "{} successfully joined.".format(first_name))
