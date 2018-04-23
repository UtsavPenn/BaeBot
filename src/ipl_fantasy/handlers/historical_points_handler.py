try:
    import unzip_requirements
except ImportError:
    pass

import matplotlib
matplotlib.use('AGG')

from ipl_fantasy.data import get_points_history_for_user
from ipl_fantasy.common import simple_table, determine_user

import matplotlib.pyplot as plt
import seaborn as sns

import tempfile


def get_user_points_history(user_id):
    points_per_match = []
    points_history = get_points_history_for_user(user_id)['pointsHistory']
    for i, points in enumerate(points_history):
        total_points = int(points['btP']) + int(points['boP']) + \
            int(points['fP']) + int(points['mP']) + int(points['wP'])
        points_per_match.append((i + 1, total_points))
    return points_per_match


def historical_points(bot, update, args):
    if args:
        user = determine_user(args[0])
        points = get_user_points_history(user)

        # bot.send_message(update.message.chat_id, simple_table(get_user_points_history(user)))

        plt.figure()
        named_file = tempfile.NamedTemporaryFile(suffix='.png')
        plot = sns.pointplot(
            x=[p[0] for p in points], y=[p[1] for p in points])
        plot.figure.savefig(named_file.name)
        bot.send_photo(
            update.message.chat_id, photo=open(named_file.name, 'rb'))

        plt.figure()
        named_file = tempfile.NamedTemporaryFile(suffix='.png')
        plot = sns.barplot(x=[p[0] for p in points], y=[p[1] for p in points])
        plot.figure.savefig(named_file.name)
        bot.send_photo(
            update.message.chat_id, photo=open(named_file.name, 'rb'))

        # plot = sns.pointplot(x=[p[0] for p in points], y=[p[1] for p in points])
        # plot.figure.savefig('/tmp/tmp.png')
        # bot.send_photo(update.message.chat_id, photo=open('/tmp/tmp.png', 'rb'))

    else:
        bot.send_message(
            chat_id=update.message.chat_id, text="Please specify a user")
