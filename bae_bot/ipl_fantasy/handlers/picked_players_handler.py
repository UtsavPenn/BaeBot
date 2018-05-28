from collections import defaultdict

from bae_bot.ipl_fantasy.data import get_squad_details
from bae_bot.ipl_fantasy.common import (get_player, get_league_team_name_for_user,
                                simple_table, USER_IDS, determine_team,
                                get_ipl_player_to_users_mapping)


def picked_players(bot, update, args):
    # bot.send_message(update.message.chat_id, "Stealth for life!")
    # return
    if not args:
        bot.send_message(update.message.chat_id,
                         "Usage: /pickedplayers <team1> <team2> ...")
        return

    args = list(map(determine_team, args))
    ipl_players = get_ipl_player_to_users_mapping(args)

    data = sorted(ipl_players.items(), key=lambda x: len(x[1]), reverse=True)
    data = list(map(lambda x: (x[0], ", ".join(x[1])), data))

    bot.send_message(update.message.chat_id, simple_table(data))
