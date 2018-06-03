from pynamodb.exceptions import DoesNotExist

from bae_bot.fifawc.models import BetsHistory


def pick(bot, update, args):
    user = update.effective_user.first_name
    
    if len(args) < 3 or not args :
      bot.send_message(update.message.chat_id, "Usage: /pick 1234 Argentina 10")
      return
    bet = BetsHistory(event_id=args[0], user_id=user, bet_amount=args[2],result=args[1],bet_processed=0)
    bet.save()
    bot.send_message(update.message.chat_id, "Bet successfully placed")
