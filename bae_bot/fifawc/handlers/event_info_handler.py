from bae_bot.fifawc.models import BetsHistory
from bae_bot.fifawc.payout_distribution import get_payout_distribution
from pynamodb.exceptions import DoesNotExist
from bae_bot.fifawc.models import EventInfo


def event_info(bot, update, args):
    if not args:
        bot.send_message(update.message.chat_id, "Usage: /eventinfo <event_id>")
        return

    event_id = int(args[0])
    try:
        event_info = EventInfo.get(event_id)
    except DoesNotExist:
        bot.send_message(update.message.chat_id, "Event with id {} doesn't exist".format(event_id))
        return

    resp = "Event Information: \n"
    resp += "Event Id: {} \n".format(event_id)
    resp += "{} \n".format(event_info.event_description)

    resp += "\n"
    resp += "Odds Information: \n"
    for outcome, odds in get_payout_distribution(event_id).items():
        resp += "If you put 1 on {}, you get {} if {} \n".format(outcome, odds, outcome)

    resp += "\n"
    resp += "Bets placed: \n"

    for bet in BetsHistory.scan():
        if bet.event_id == event_id:
            resp += "{} placed a bet of {} on {} \n".format(bet.user_id, bet.bet_amount, bet.result)

    bot.send_message(update.message.chat_id, resp)