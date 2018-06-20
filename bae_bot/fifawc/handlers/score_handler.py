import requests
from bae_bot.fifawc.common import get_player


def score(bot, update):
    r = requests.get("https://fantasy.fifa.com/services/api/live/mixed")
    data = r.json()['Data']['Value']
    resp = ""
    for scoring in data['Scoring']:
        for team in scoring['TeamScoreLine']:
            resp += str(team['TeamName'])
            resp += " "
            resp += str(team['GoalsScored'])
            resp += " "
        resp += "\n"
        resp += scoring['MatchTime'] + " minutes"
        resp += "\n"

        for player in scoring['PlayerStats']:
            if player['GoalScored']:
                resp += get_player(player['PlayerId']) + " " + str(player['GoalScored'])
                resp += "\n"
        resp += "\n"
    bot.send_message(update.message.chat_id, resp)
