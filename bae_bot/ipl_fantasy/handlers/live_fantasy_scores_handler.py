from bae_bot.ipl_fantasy.common import (get_league_team_name_for_user, USER_IDS,
                                        simple_table, determine_user,
                                        get_total_points_from_live_data, get_player,
                                        get_points_from_live_player_points)

from bae_bot.ipl_fantasy.data import get_live_data_for_user, get_squad_details
from bae_bot.ipl_fantasy.data import get_scoring_info

def get_score_card():
    def pn(id): return get_player(id).name

    scoring_info = get_scoring_info()
    innings = scoring_info['innings']
    resp = ""

    for inning in innings:
        sc = inning['scorecard']
        resp += "{}/{} {} \n".format(sc['runs'], sc['wkts'], inning['overProgress'])

    current_batsmen = list(scoring_info['currentState']['currentBatsmen'])
    for bm in current_batsmen:
        for inning in innings:
            for bS in inning['scorecard']['battingStats']:
                if bS['playerId'] == bm:
                    resp += "{}: {} off {} {} \n".format(pn(bm), bS['r'], bS['b'], bS.get('sr'))

    current_bowler = scoring_info['currentState']['currentBowler']
    for inning in innings:
        for bs in inning['scorecard']['bowlingStats']:
            if bs['playerId'] == current_bowler:
                resp += "{}: {} {} {} {} \n".format(pn(current_bowler), bs['ov'], bs['r'], bs['w'], bs.get('e'))

    return resp

def live_fantasy_scores(bot, update, args):
    resp = get_score_card()
    resp += "\n"

    if args:
        user = determine_user(args[0])
        live_data = get_live_data_for_user(user)
        user_players = get_squad_details(user)['players']

        player_points = []
        for player in live_data['playerPoints']:
            if player['playerId'] in user_players:
                points = get_points_from_live_player_points(player)
                if not points:
                    continue
                player_points.append((get_player(player['playerId']).name, points))

        player_points = sorted(player_points, key=lambda x: int(x[1]), reverse=True)

        resp += "Live Points: {} \n".format(get_total_points_from_live_data(live_data))
        resp += simple_table(player_points)

        bot.send_message(update.message.chat_id, resp)
    else:
        live_scores = []
        for user in USER_IDS:
            live_data = get_live_data_for_user(user)
            score = get_total_points_from_live_data(live_data)
            live_scores.append((get_league_team_name_for_user(user), score))

        live_scores.sort(key=lambda x: int(x[1]), reverse=True)
        resp += simple_table(live_scores)
        bot.send_message(update.message.chat_id, resp)
