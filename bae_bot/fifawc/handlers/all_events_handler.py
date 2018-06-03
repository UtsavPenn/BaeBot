from bae_bot.fifawc.models import EventInfo
import tabulate

def all_events(bot, update, args):
    all = []
    events = EventInfo.scan()
    for event in events:
        all.append((event.bet_id,
                    event.bet_description,
                    ",".join(event.bet_result_choices),
                    str(event.bet_deadline)))
    bot.send_message(update.message.chat_id, tabulate.tabulate(all))

