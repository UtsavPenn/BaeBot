import uuid
from pynamodb.exceptions import DoesNotExist
from bae_bot.fifawc.models import BetsHistory, EventInfo
from datetime import datetime,timezone

def place_bet(bot, update, args):
    user = update.effective_user.first_name
   
    if len(args) < 3 or not args :
      bot.send_message(update.message.chat_id, "Usage: /pick 1234 ARG 10")
      return
    
    try:
      event = EventInfo.get(int(args[0]))
    except DoesNotExist:
      bot.send_message(update.message.chat_id, "Event id is not for a valid event.")
      return

    if not args[1] in event.event_result_choices:
      bot.send_message(update.message.chat_id, "Prediction choice not present in list of probable outcomes for the event.")
      return

    dt = datetime.now()
    
    if dt.replace(tzinfo=timezone.utc) > event.event_deadline:
      bot.send_message(update.message.chat_id, "Oops.Event deadline already passed :(")

    betId =  str(uuid.uuid4())
    bet = BetsHistory(bet_id=betId, event_id=int(args[0]), user_id=user, bet_amount=int(args[2]),result=args[1],bet_processed=0)
    bet.save()
    resp = "Bet succesfully placed on "+ args[1] +" for " + event.event_description 
    bot.send_message(update.message.chat_id, resp)

