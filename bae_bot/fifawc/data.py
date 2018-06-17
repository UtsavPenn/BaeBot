import requests


def get_league_info():
    URL = "https://fantasy.fifa.com/services/api/leagues/92244/leagueleaderboard?optType=2&vPageNo=1&vPageChunk=25&vTopNo=25&vPhaseId=0&gamedayId=1&buster=default"
    r = requests.get(URL)
    return r.json()['Data']['Value']
