from bae_bot.fifawc.models import EventInfo
from pynamodb.exceptions import DoesNotExist


def set_outcome(bot, update, args):
    first_name = update.effective_user.first_name
    event_id, outcome = int(args[0]), args[1]
    try:
        event_info = EventInfo.get(event_id)
    except DoesNotExist:
        bot.send_message(update.message.chat_id, "Event with id {} not found".format(event_id))
        return

    if outcome not in event_info.event_result_choices:
        bot.send_message(update.message.chat_id, "outcome {} not in {}".format(outcome, event_info.event_result_choices))
        return

    event_info.event_outcome = outcome
    event_info.save()
    bot.send_message(update.message.chat_id, "Outcome {} successfully saved for {}".format(event_info.event_outcome, event_info.event_id))

