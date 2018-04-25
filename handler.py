try:
    import unzip_requirements
except ImportError:
    pass

import json
import os
import sys
import logging

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))
sys.path.append(os.path.join(here, "./src"))

from telegram.bot import Bot
from telegram.update import Update

from wrappers import CustomCommandHandler
from ipl_fantasy.handlers import (power_players,
                                  subs_left,
                                  stealths_left,
                                  second_power_players,
                                  picked_players,
                                  live_fantasy_scores,
                                  compare_users,
                                  players_of,
                                  who_has,
                                  cumulative_scores,
                                  sub_strike_rate,
                                  historical_points,
                                  points_of)

log = logging.getLogger(__name__)

START_TEXT = """Ask me:

/start
/live
/total - Example usage: /total [or] /total sujith
/history - Example usage: /history [or] /history proditya
/pp - Example usage: /pp or /pp sujith
/spp - same as above
/subsleft - Example Usage: /subsleft or /subsleft badri
/stealthleft - Example Usage: /stealthleft or /stealthleft aayush
/pickedplayers - Example Usage: /pickedplayers <teamname1> <teamname2>
/compare - Example usage: /compare badri tharun <teamname1> ...
/playersof - Example usage: /playersof aditya [or] /playersof aditya csk
/whohas - Example usage: /whohas stokes
/subsrr - sub strike rate. Example usage: /subsrr [or] /subsrr tharun
/pointsof - Get live points of player. Example usage: /pointsof rashid
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

        dispatcher.add_handler(CustomCommandHandler('total', cumulative_scores, pass_args=True))
        dispatcher.add_handler(CustomCommandHandler('live', live_fantasy_scores, pass_args=True))
        dispatcher.add_handler(CustomCommandHandler('history', historical_points, pass_args=True))
        dispatcher.add_handler(CustomCommandHandler('pp', power_players, pass_args=True))
        dispatcher.add_handler(CustomCommandHandler('spp', second_power_players, pass_args=True))
        dispatcher.add_handler(CustomCommandHandler('subsleft', subs_left, pass_args=True))
        dispatcher.add_handler(CustomCommandHandler('stealthleft', stealths_left, pass_args=True))
        dispatcher.add_handler(CustomCommandHandler('pickedplayers', picked_players, pass_args=True))
        dispatcher.add_handler(CustomCommandHandler('compare', compare_users, pass_args=True))
        dispatcher.add_handler(CustomCommandHandler('playersof', players_of, pass_args=True))
        dispatcher.add_handler(CustomCommandHandler('whohas', who_has, pass_args=True))
        dispatcher.add_handler(CustomCommandHandler('subsrr', sub_strike_rate, pass_args=True))
        dispatcher.add_handler(CustomCommandHandler('pointsof', points_of, pass_args=True))

        data = json.loads(event["body"])
        update = Update.de_json(data, bot)
        dispatcher.process_update(update)

    except Exception as e:
        log.exception(e)

    return {"statusCode": 200}
