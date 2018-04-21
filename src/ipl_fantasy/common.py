import re
import tabulate
from collections import defaultdict
from fuzzywuzzy import process

from ipl_fantasy.data import get_league_details, get_players, get_squad_details, Player


USER_IDS = \
['sujith90@gmail.com',
 'shubhamdas947@gmail.com',
 'aayush.krishankumar@gmail.com',
 'utsavkiit@gmail.com',
 'adityanarayan.1191@gmail.com',
 'badrinathrayadurg@gmail.com',
 'sravyakotaru@gmail.com',
 'tarunreddy.bethi@gmail.com',
 'nanaya5588@gmail.com',
 'sarkarr612@gmail.com']


TEAMS = \
['kings-xi-punjab', 
'rajasthan-royals', 
'delhi-daredevils', 
'chennai-super-kings', 
'kolkata-knight-riders', 
'sunrisers-hyderabad', 
'mumbai-indians', 
'royal-challengers-bangalore']


USER_TO_LEAGUE_NAME_MAPPING = \
{'aayush.krishankumar@gmail.com': 'RaisedByWolves',
 'adityanarayan.1191@gmail.com': 'Alpine Warriors',
 'badrinathrayadurg@gmail.com': 'Warriors',
 'nanaya5588@gmail.com': 'MumbaiKarz',
 'sarkarr612@gmail.com': 'Kolkata Rangers',
 'shubhamdas947@gmail.com': 'Rocky United',
 'sravyakotaru@gmail.com': 'BaskinRobins',
 'sujith90@gmail.com': 'SujiWuji XI',
 'tarunreddy.bethi@gmail.com': 'TRDY',
 'utsavkiit@gmail.com': 'Blaugrana'}


def get_league_team_name_for_user(user_id):
    return USER_TO_LEAGUE_NAME_MAPPING.get(user_id)


def simple_table(data):
	return tabulate.tabulate(data)


def get_player(player_id):
    players = get_players()
    match = players.get(int(player_id))
    if not match:
        return Player({'id': 'nan', 'name': 'nan', 'team': 'nan'})    
    return match    

def determine_user(user):
    user_regexes = [
        (re.compile('gopi', re.IGNORECASE), "shubhamdas947@gmail.com"),
        (re.compile('tha', re.IGNORECASE), "tarunreddy.bethi@gmail.com"),
        (re.compile('uts|stud', re.IGNORECASE), "utsavkiit@gmail.com"),
        (re.compile('(pro)?a?di|chut', re.IGNORECASE), "adityanarayan.1191@gmail.com"),
        (re.compile('suj', re.IGNORECASE), "sujith90@gmail.com"),
        (re.compile('a?ayu', re.IGNORECASE), "aayush.krishankumar@gmail.com"),
        (re.compile('bad', re.IGNORECASE), "badrinathrayadurg@gmail.com"),
        (re.compile('sra', re.IGNORECASE), "sravyakotaru@gmail.com"),
        (re.compile('bhai|nir', re.IGNORECASE), "nanaya5588@gmail.com"),
    ]
    
    for regex, user_id in user_regexes:
        if regex.match(user):
            return user_id


def team_short_name(team):
    return "".join(map(lambda x: x[0], team.split('-')))

def determine_team(short_name):
    for team in TEAMS:
        if short_name == team_short_name(team):
            return team
        if short_name == team:
            return team

    return process.extractOne(short_name, TEAMS)[0]



def get_ipl_player_to_users_mapping(teams=None):
    ipl_players = defaultdict(list)
    for user_id in USER_IDS:
        for player in get_squad_details(user_id)['players']:
            player_details = get_player(player)
            if teams and not player_details['team'] in teams:
                continue
            ipl_players[player_details.name].append(
                get_league_team_name_for_user(user_id))

    return ipl_players


def get_total_score_so_far_for_user(user_id):
    for member in get_league_details()['leagueMembers']:
        if member['userId'] == user_id:
            return member['totalPoints']





