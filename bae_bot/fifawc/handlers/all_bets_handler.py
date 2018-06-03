from bae_bot.fifawc.models import BetInfo
import tabulate

def all_bets(bot, update, args):
    all = []
    bets = BetInfo.scan()
    for bet in bets:
        all.append((bet.bet_id,
                    bet.bet_description,
                    ",".join(bet.bet_result_choices),
                    str(bet.bet_deadline)))
    bot.send_message(update.message.chat_id, tabulate.tabulate(all))

