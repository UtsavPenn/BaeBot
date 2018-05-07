from collections import defaultdict
import json
import os

import boto3

from bae_bot.ipl_fantasy.data import get_match_id, get_squad_details
from bae_bot.ipl_fantasy.common import USER_IDS, get_player, get_league_team_name_for_user
from bae_bot.ipl_fantasy.data import get_match


def main(event, context):
    squad_history = defaultdict(list)
    current_match_id = get_match_id()
    for user in USER_IDS:
        for match_id in range(7894, current_match_id):
            print("Processing {} {}".format(user, match_id))

            match = get_match(match_id)

            try:
                squad_details = get_squad_details(user, match_id)

            except KeyError:
                print("Unable to get details for {} {}".format(user, match_id))
                continue

            players = [get_player(p) for p in squad_details['players']]
            squad_details['players'] = [p.name for p in players]
            squad_details['powerPlayer'] = get_player(squad_details['powerPlayer']).name
            squad_details['secondPowerPlayer'] = get_player(squad_details['secondPowerPlayer']).name
            squad_details['matchDescription'] = match.description
            squad_details['teams'] = match.teams
            squad_details['numPlayersPlaying'] = len([p for p in players if p.team in match.teams])

            del squad_details['transfersRemaining']
            del squad_details['stealthList']
            del squad_details['doublePointsList']
            del squad_details['freeTransfer']

            squad_history[get_league_team_name_for_user(user)].append(squad_details)

    print("Uploading data to s3")
    s3_client = boto3.client('s3')
    s3_client.put_object(Bucket=os.environ.get('S3_STORAGE_BUCKET', 'com.baebot.dev.storage'),
                         Key="teams_squad_history.json",
                         Body=json.dumps(squad_history))


    return {"statusCode": 200}
