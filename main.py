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
sys.path.append(os.path.join(here, ".serverless", "requirements"))

import requests
from telegram.bot import Bot
from telegram.chat import Chat
from telegram.update import Update

from wrappers import CustomCommandHandler
from ipl_fantasy.data import get_live_data_for_user



