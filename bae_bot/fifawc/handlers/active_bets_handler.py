from bae_bot.fifawc.models import BetsHistory


def active_bets(bot, update):
    resp = ""
    for bet in BetsHistory.scan():
        if bet.bet_processed:
            continue
        resp += "Bet of {} placed on {} for {} by {} \n".format(bet.bet_amount,
                                                                bet.result,
                                                                bet.event_id,
                                                                bet.user_id)
    bot.send_message(update.message.chat_id, resp)

