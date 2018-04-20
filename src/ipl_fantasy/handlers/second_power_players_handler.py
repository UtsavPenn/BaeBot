from ipl_fantasy.common import (get_player,
                                get_league_team_name_for_user,
                                simple_table,
                                determine_user, 
                                USER_IDS)
from ipl_fantasy.data import get_squad_details


def get_second_power_player_for_user(user_id):
    player = get_squad_details(user_id)['secondPowerPlayer']
    return get_player(player).name


def get_second_power_players():
    return [(get_league_team_name_for_user(user),
             get_second_power_player_for_user(user)) for user in USER_IDS]


def second_power_players(bot, update, args):
    if args:
        user = determine_user(args[0])
        bot.send_message(update.message.chat_id,
                         get_second_power_player_for_user(user))
    else:
        bot.send_message(update.message.chat_id, simple_table(get_second_power_players()))
