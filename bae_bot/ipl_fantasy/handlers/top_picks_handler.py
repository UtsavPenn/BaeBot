import arrow
import pytz
import tabulate

from bae_bot.ipl_fantasy.common import  get_player, determine_team,simple_table
from bae_bot.ipl_fantasy.data import get_matches, get_top_players

def get_all_players_rank_data():
    #return get_squad_details('utsavkiit@gmail.com')
    player_standings = get_top_players()
    player_info = []
    for player_standing in player_standings:
        player_id = player_standing['playerId']
        player_name = player_standing['fullName']
        batting_rank = player_standing['battingRank']
        bowling_rank = player_standing['bowlingRank']
        team_name = get_player(player_id)['team']
        player_type = get_player(player_id).type
        player_points = sum((v for k,v in player_standing.items() if k.endswith('P')))
        player_info.append((player_id,player_name,player_type, batting_rank,bowling_rank,player_points,team_name))
    #write_updated_top_picks_to_file(json.dumps(player_info))
    #write_updated_top_picks_to_file(data)
    return player_info

def get_top_picks(short_team_name=None): 
    all_players = get_all_players_rank_data()
    if short_team_name:
        team_name = determine_team(short_team_name)
        all_players = [x for x in all_players if x[6] == team_name]
    top_players = sorted(all_players, key=lambda x: int(x[5]), reverse=True)[:5]
    return top_players

def top_picks(bot, update, args): 
    rankings = []
    if(args):
        team = determine_team(args[0])
        rankings = get_top_picks(team)
    else:
        rankings = get_top_picks()
    rankings_table = []

    for rank in rankings:
        row = [rank[1],rank[5], rank[2]]
        rankings_table.append(row)
    bot.send_message(update.message.chat_id,simple_table(rankings_table))
