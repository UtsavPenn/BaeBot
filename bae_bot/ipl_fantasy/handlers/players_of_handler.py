from bae_bot.ipl_fantasy.common import determine_user, get_player, determine_team
from bae_bot.ipl_fantasy.data import get_squad_details


def players_of(bot, update, args):
    if not args:
        bot.send_message(update.message.chat_id, "Usage: /playersof badri mi")
        return

    user = determine_user(args[0])
    players = [get_player(p) for p in get_squad_details(user)['players']]

    if len(args) > 1:
        team = determine_team(args[1])
        players = [p for p in players if p['team'] == team]

    player_names = [p.name for p in players]

    if not player_names:
        bot.send_message(update.message.chat_id, "No players")
        return
    
    message = "Player (team) (next match in)\n"
    now = arrow.now()
    for player in players:
        for match in get_matches():
            starttime = arrow.get(match.starttime)
            if((player.team in match.teams) and (now < starttime)):
                message += player.name + " " + str((starttime-now).days) + "\n"
                break
    bot.send_message(update.message.chat_id, message)
