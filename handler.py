import json
import os
import sys
import logging
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))
sys.path.append(os.path.join(here, "./src"))

import requests
from telegram.bot import Bot
from telegram.chat import Chat
from telegram.update import Update

from wrappers import CustomCommandHandler
from ipl_fantasy.handlers import (power_players, 
                                subs_left, 
                                stealths_left,
                                second_power_players,
                                picked_players,
                                live_fantasy_scores)


log = logging.getLogger(__name__)

START_TEXT = """Ask me:

/start
/livefantasyscores
/powerplayers - Example usage: /powerplayers or /powerplayers sujith
/secondpowerplayers - same as above
/subsleft - Example Usage: /subsleft or /subsleft badri
/stealthleft - Example Usage: /stealthleft or /stealthleft aayush
/pickedplayers - Example Usage: /pickedplayers <teamname1> <teamname2>
                            Where team name is any of:

                                kings-xi-punjab or kxp
                                rajasthan-royals or rr
                                delhi-daredevils or dd
                                chennai-super-kings or csk
                                kolkata-knight-riders or kkr
                                sunrisers-hyderabad or sh
                                mumbai-indians or mi
                                royal-challengers-bangalore or rcb
"""

class Dispatcher(object):

    def __init__(self, bot):
        self.bot = bot
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def process_update(self, update):
        for handler in self.handlers:
            if handler.check_update(update):
                handler.handle_update(update, self.bot)



def start_message(bot, update):
    bot.send_message(update.message.chat_id, START_TEXT)


def main(event, context):

    try:
        bot = Bot(token=os.environ['TELEGRAM_TOKEN'])

        dispatcher = Dispatcher(bot)
        dispatcher.add_handler(CustomCommandHandler('start', start_message))
        dispatcher.add_handler(CustomCommandHandler('livefantasyscores', live_fantasy_scores))

        dispatcher.add_handler(CustomCommandHandler('powerplayers', power_players, pass_args=True))
        dispatcher.add_handler(CustomCommandHandler('secondpowerplayers', second_power_players, pass_args=True))

        dispatcher.add_handler(CustomCommandHandler('subsleft', subs_left, pass_args=True))
        dispatcher.add_handler(CustomCommandHandler('stealthleft', stealths_left, pass_args=True))

        dispatcher.add_handler(CustomCommandHandler('pickedplayers', picked_players, pass_args=True))


        data = json.loads(event["body"])
        update = Update.de_json(data, bot)
        dispatcher.process_update(update)

    except Exception as e:
        log.exception(e)

    return {"statusCode": 200}
