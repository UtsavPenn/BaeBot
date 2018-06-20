import json
import os


def get_player(id):
    path = os.path.join(os.environ['LAMBDA_TASK_ROOT'], 'bae_bot', 'fifawc', 'players.json')
    with open(path) as fp:
        id_to_name_mapping = json.loads(fp.read())
    return id_to_name_mapping.get(str(id))
