from utils import get_sent_message

from bae_bot.ipl_fantasy.handlers.players_of_handler import players_of


def test_players_of(bot, update):
    players_of(bot, update, ['sujith'])
    assert "0" not in get_sent_message(bot)
