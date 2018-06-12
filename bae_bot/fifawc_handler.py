try:
    import unzip_requirements
except ImportError:
    pass

import json
import logging
import os
import sys

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./"))
sys.path.append(os.path.join(here, "./vendored"))

from telegram.bot import Bot
from telegram.update import Update

from bae_bot.wrappers import CustomCommandHandler
from bae_bot.dispatcher import Dispatcher

from bae_bot.fifawc.handlers import (join,
                                     all_events,
                                     place_bet,
                                     standings,
                                     event_info)

log = logging.getLogger(__name__)

START_TEXT = """Hi {first_name}. Here are the commands:

/start
/join - Join the League
/events - Show all available bets
/eventinfo - Show all the bets for that event
/placebet - Place a bet on an event 
/standings - Show all standings till now
"""

bot = Bot(token=os.environ['TELEGRAM_TOKEN'])


def start_message(bot, update):
    bot.send_message(update.message.chat_id, START_TEXT.format(first_name=update.effective_user.first_name))


def main(event, context):
    try:
        dispatcher = Dispatcher(bot)
        dispatcher.add_handler(CustomCommandHandler('start', start_message))
        dispatcher.add_handler(CustomCommandHandler('join', join))
        dispatcher.add_handler(CustomCommandHandler('placebet', place_bet, pass_args=True))
        dispatcher.add_handler(CustomCommandHandler('events', all_events, pass_args=True))
        dispatcher.add_handler(CustomCommandHandler('eventinfo', event_info, pass_args=True))
        dispatcher.add_handler(CustomCommandHandler('standings', standings, pass_args=True))

        data = json.loads(event["body"])
        update = Update.de_json(data, bot)
        dispatcher.process_update(update)

    except Exception as e:
        log.exception(e)

    return {"statusCode": 200}
