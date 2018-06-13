import uuid

from bae_bot.fifawc.models import User
from pynamodb.exceptions import DoesNotExist
from bae_bot.fifawc.models import BetsHistory, EventInfo
import arrow


def place_bet(bot, update, args):
    user = update.effective_user.first_name

    try:
        user_info = User.get(user)
    except DoesNotExist:
        bot.send_message(update.message.chat_id, "User {} not registered".format(user))
        return

    if len(args) < 3:
        bot.send_message(update.message.chat_id, "Usage: /placebet <event_id> ARG <amount>")
        return

    event_id, choice, bet_amount = int(args[0]), args[1].upper(), int(args[2])
    try:
        event = EventInfo.get(int(event_id))
    except DoesNotExist:
        bot.send_message(update.message.chat_id, "Event id is not for a valid event.")
        return

    if not choice in event.event_result_choices:
        bot.send_message(update.message.chat_id,
                         "Prediction choice {} not one of {}.".format(choice, event.event_result_choices))
        return

    if arrow.utcnow() > arrow.get(event.event_deadline):
        bot.send_message(update.message.chat_id, "Oops.Event deadline already passed :(")
        return

    buying_power = user_info.total_amount - user_info.reserved_amount
    if int(bet_amount) > buying_power:
        bot.send_message(update.message.chat_id, "You cannot bet more than your buying power: {}".format(buying_power))
        return

    betId = str(uuid.uuid4())
    bet = BetsHistory(bet_id=betId,
                      event_id=int(event_id),
                      user_id=user,
                      bet_amount=int(bet_amount),
                      result=choice,
                      bet_processed=False)
    bet.save()

    user_info.reserved_amount += int(bet_amount)
    user_info.save()

    resp = "Bet of {} successfully placed on {} for {}".format(bet_amount, choice, event.event_description)
    bot.send_message(update.message.chat_id, resp)
