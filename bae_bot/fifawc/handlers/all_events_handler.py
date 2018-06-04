from bae_bot.fifawc.models import EventInfo
import tabulate

def all_events(bot, update, args):
    all = []
    events = EventInfo.scan()
    for event in events:
        all.append((event.event_id,
                    event.event_description,
                    ",".join(event.event_result_choices),
                    event.event_deadline))
    all = sorted(all, key=lambda x: x[3].timestamp())
    bot.send_message(update.message.chat_id, tabulate.tabulate(all))

