import json
import os
import logging

import bunch
import requests
from cachetools import func as functools

from bae_bot.ipl_fantasy.headers import API_HEADERS

LOG = logging.getLogger(__name__)

def get_request_data(url, headers=None):
    """This appears to be how the data is wrapped in the responses"""

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.json()['data']
    except Exception as e:
        LOG.exception("Failed to get request data for {}".format(url))
        raise e

def post_data(url, headers=None):
    """This appears to be how the data is wrapped in the responses"""
    r = requests.post(url, headers=headers)
    r.raise_for_status()
    return r.json()['data']

@functools.ttl_cache(ttl=100)
def get_live_match_details():
    live_match_details = requests.get(
        'https://s3-ap-southeast-1.amazonaws.com/images-fantasy-iplt20/match-data/livematch.json')
    return live_match_details.json()


def _is_score_calculated(live_match_details):
    if int(live_match_details.get('liveMatchId')) == 7925: #Hardcoding due to IPL bug
        return True
    return live_match_details.get('scoreCalculated', False)


def get_match_id():
    live_match_details = get_live_match_details()
    if not _is_score_calculated(live_match_details):
        return int(live_match_details.get('liveMatchId'))
    else:
        return int(live_match_details.get('liveMatchId')) + 1


@functools.ttl_cache(ttl=200)
def get_user_details(user_id):
    URL = "https://2fjfpxrbb3.execute-api.ap-southeast-1.amazonaws.com/production/useriplapi/getuserprofile?userid={}".format(
        user_id)
    return get_request_data(URL, headers=API_HEADERS)


@functools.ttl_cache(ttl=200)
def get_squad_details(user_id, match_id=None):
    if not match_id:
        match_id = get_match_id()
    URL = "https://2fjfpxrbb3.execute-api.ap-southeast-1.amazonaws.com/production/useriplapi/getsquad?matchId={}&userid={}".format(
        match_id, user_id)
    return get_request_data(URL, headers=API_HEADERS)


@functools.ttl_cache(ttl=200)
def get_league_details(league_id='ip3NjxML'):
    URL = "https://2fjfpxrbb3.execute-api.ap-southeast-1.amazonaws.com/production/leagueapi/getleaguemembers?leagueId={}".format(
        league_id)
    return get_request_data(URL, headers=API_HEADERS)


def get_live_data_for_user(user_id):
    live_match_details = get_live_match_details()
    match_id = get_match_id()
    live_match_url = live_match_details.get('liveUrl')

    URL = "https://2fjfpxrbb3.execute-api.ap-southeast-1.amazonaws.com/production/useriplapi/getlivescore?matchId={}&userid={}&matchLink={}".format(
        match_id, user_id, live_match_url)
    data = get_request_data(URL, headers=API_HEADERS)
    return data


def get_points_history_for_user(user_id):
    URL = "https://2fjfpxrbb3.execute-api.ap-southeast-1.amazonaws.com/production/useriplapi/getuserprofile?userid={}".format(
        user_id)
    return get_request_data(URL, headers=API_HEADERS)

@functools.ttl_cache(ttl=200)
def get_match_wise_live_data_for_user(user_id,match_id,match_no):
    if(int(match_no) < 10):
        match_no = '0' + match_no

    live_match_url = 'http://datacdn.iplt20.com/dynamic/data/core/cricket/2012/ipl2018/ipl2018-'+match_no+'/scoring.js'

    URL = "https://2fjfpxrbb3.execute-api.ap-southeast-1.amazonaws.com/production/useriplapi/getlivescore?matchId={}&userid={}&matchLink={}".format(
        match_id, user_id, live_match_url)
    data = get_request_data(URL, headers=API_HEADERS)
    return data

@functools.ttl_cache(ttl=200)
def get_top_players():
    URL = "https://2fjfpxrbb3.execute-api.ap-southeast-1.amazonaws.com/production/leaderboardsapi/gettopplayers"
    data = post_data(URL,headers=API_HEADERS)
    return data


class Player(bunch.Bunch):

    @property
    def name(self):
        from bae_bot.ipl_fantasy.common import team_short_name

        player_name = " ".join(map(lambda x: x.capitalize(), self['name'].split('-')))
        return player_name + " ({})".format(team_short_name(self['team']))


class Match(bunch.Bunch):

    @property
    def description(self):
        from bae_bot.ipl_fantasy.common import team_short_name

        return " vs ".join(map(team_short_name, self['teams']))


@functools.lru_cache()
def get_players():
    with open(os.path.join(os.environ['LAMBDA_TASK_ROOT'], 'bae_bot', 'ipl_fantasy', 'players.json')) as fp:
        players = json.loads(fp.read())
    return {int(id): Player(player) for id, player in players.items()}


@functools.lru_cache()
def get_matches():
    with open(os.path.join(os.environ['LAMBDA_TASK_ROOT'], 'bae_bot', 'ipl_fantasy', 'matches.json')) as fp:
        matches = json.loads(fp.read())
    return list(map(Match, matches))


def get_match(match_id):
    match_id = int(match_id)
    all_matches = get_matches()
    for i, match in enumerate(all_matches):
        if i + 7894 == int(match_id):
            return match


def get_scoring_info(match_id=None):
    if not match_id:
        match_id = get_match_id()
    URL = "https://cricketapi.platform.iplt20.com//fixtures/{}/scoring".format(match_id)
    r = requests.get(URL)
    return r.json()
