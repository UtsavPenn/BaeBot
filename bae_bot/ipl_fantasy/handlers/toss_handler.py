import jmespath

from bae_bot.ipl_fantasy.data import get_scoring_info


def toss(bot, update):
    scoring_info = get_scoring_info()
    toss_info = jmespath.search('matchInfo.additionalInfo."toss.elected"', scoring_info)
    if not toss_info:
        bot.send_message(update.message.chat_id, "No toss and team info found yet.")
        return

    resp = "Toss Info: {} \n".format(toss_info)

    teams = jmespath.search('matchInfo.teams', scoring_info)
    if teams:
        for team in teams:
            resp += "Team: {} \n".format(team['team']['abbreviation'])
            resp += ",".join([player['fullName'] for player in team['players']])
            resp += "\n"
    else:
        resp += "No squad info found yet. Check back shortly."

    bot.send_message(update.message.chat_id, resp)