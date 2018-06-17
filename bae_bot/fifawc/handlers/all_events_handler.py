import arrow
from bae_bot.fifawc.models import EventInfo
import tabulate

def all_events(bot, update, args):
    all = []
    events = EventInfo.scan()
    for event in events:
        if event.event_outcome:
            continue
        all.append((event.event_id,
                    event.event_description,
                    ",".join(event.event_result_choices),
                    event.event_deadline))
    all = sorted(all, key=lambda x: arrow.get(x[3]).timestamp)
    if args:
        all = all[:int(args[0])]
    all.insert(0, ("event_id", "description", "event_choices", "deadline"))
    bot.send_message(update.message.chat_id, tabulate.tabulate(all[:25]))

