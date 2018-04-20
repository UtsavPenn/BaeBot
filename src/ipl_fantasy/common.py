import re
import tabulate

from ipl_fantasy.data import get_league_details, get_players


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


def get_league_team_name_for_user(user_id):
    for member in get_league_details()['leagueMembers']:
        if member['userId'] == user_id:
            return member['teamName']


def simple_table(data):
	return tabulate.tabulate(data)



def get_player(player_id):
    players = get_players()
    return players.get(int(player_id))
    

def determine_user(user):
    user_regexes = [
        (re.compile('gopi', re.IGNORECASE), "shubhamdas947@gmail.com"),
        (re.compile('tha', re.IGNORECASE), "tarunreddy.bethi@gmail.com"),
        (re.compile('uts', re.IGNORECASE), "utsavkiit@gmail.com"),
        (re.compile('(pro)?a?dity', re.IGNORECASE), "adityanarayan.1191@gmail.com"),
        (re.compile('suj', re.IGNORECASE), "sujith90@gmail.com"),
        (re.compile('a?ayu', re.IGNORECASE), "aayush.krishankumar@gmail.com"),
        (re.compile('bad', re.IGNORECASE), "badrinathrayadurg@gmail.com"),
        (re.compile('sra', re.IGNORECASE), "sravyakotaru@gmail.com"),
        (re.compile('bhai|nir', re.IGNORECASE), "nanaya5588@gmail.com"),
    ]
    
    for regex, user_id in user_regexes:
        if regex.match(user):
            return user_id
