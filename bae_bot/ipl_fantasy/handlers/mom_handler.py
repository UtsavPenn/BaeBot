import jmespath

from bae_bot.ipl_fantasy.data import get_scoring_info


def mom(bot, update):
    scoring_info = get_scoring_info()
    mom = jmespath.search('matchInfo.additionalInfo."result.playerofthematch"', scoring_info)
    if mom:
        bot.send_message(update.message.chat_id, mom)
    else:
        bot.send_message(update.message.chat_id, "No info found yet")

