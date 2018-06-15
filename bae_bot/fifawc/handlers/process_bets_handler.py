from bae_bot.fifawc.models import EventInfo, BetsHistory, User
from fifawc.payout_distribution import get_payout_distribution
import time

def process_bets(bot, update):
    resp = "Processing bets: \n"
    for event in EventInfo.scan():
        if event.event_outcome:
            payout_distribution = get_payout_distribution(event.event_id)
            for bet in BetsHistory.scan():
                if bet.event_id == event.event_id and not bet.bet_processed:
                    time.sleep(1)
                    user = User.get(bet.user_id)
                    user.reserved_amount -= bet.bet_amount
                    user.total_amount -= bet.bet_amount
                    if bet.result == event.event_outcome:
                        payout = bet.bet_amount * payout_distribution[bet.result]
                        user.total_amount += payout
                        resp += "User {} won {}, Total: {} Reserved Amount {} \n".format(user.user_id,
                                                                                              payout,
                                                                                              user.total_amount,
                                                                                              user.reserved_amount)
                    else:
                        resp += "User {} lost {}, Total {} Reserved Amount {} \n".format(user.user_id,
                                                                                                bet.bet_amount,
                                                                                                user.total_amount,
                                                                                                user.reserved_amount)
                    bet.bet_processed = True
                    bet.save()
                    user.save()

    bot.send_message(update.message.chat_id, resp)



