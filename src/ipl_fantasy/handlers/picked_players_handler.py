from collections import defaultdict

from ipl_fantasy.data import get_squad_details
from ipl_fantasy.common import (get_player, 
                                get_league_team_name_for_user, 
                                simple_table, 
                                USER_IDS, 
                                determine_team)


def get_ipl_player_to_users_mapping(teams=None):
    ipl_players = defaultdict(list)
    for user_id in USER_IDS:
        for player in get_squad_details(user_id)['players']:
            player_details = get_player(player)
            if teams and not player_details['team'] in teams:
                continue
            ipl_players[player_details.name].append(
                get_league_team_name_for_user(user_id))

    return map(lambda x: (x[0], ", ".join(x[1])), sorted(ipl_players.items(), key=lambda x: len(x[1]), reverse=True))


def picked_players(bot, update, args):
    if not args:
        bot.send_message(update.message.chat_id, "Usage: /pickedplayers <team1> <team2> ...")
        return

    args = list(map(determine_team, args))
    bot.send_message(update.message.chat_id, simple_table(
        get_ipl_player_to_users_mapping(args)))
