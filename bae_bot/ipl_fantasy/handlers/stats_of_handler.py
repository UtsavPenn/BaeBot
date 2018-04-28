from bae_bot.ipl_fantasy.common import determine_player, get_points_from_live_player_points
from bae_bot.ipl_fantasy.data import get_match_wise_live_data_for_user,get_match_id



def get_player_stats(query_player):
    player = determine_player(query_player)
    match_wise_points = []
    match_num = 1
    match_id = 7894
    print(get_match_id())
    while match_id < get_match_id():
        match_points = 0
        live_user_data = get_match_wise_live_data_for_user('tarunreddy.bethi@gmail.com',match_id,str(match_num))
        for points in live_user_data['playerPoints']:
    	    if int(points['playerId']) == int(player.id):
                match_points = sum((v for k,v in points.items() if not k.startswith('second') and k.endswith('Points')))
        if match_points != 0:
            match_wise_points.append((match_num,match_points)) 
        print(match_wise_points)
        match_num = match_num + 1
        match_id = match_id + 1
    return match_wise_points

def historical_points(bot, update, args):
    if args:
        user = determine_user(args[0])
        points = get_user_points_history(user)

        # bot.send_message(update.message.chat_id, simple_table(get_user_points_history(user)))

        plt.figure()
        named_file = tempfile.NamedTemporaryFile(suffix='.png')
        plot = sns.pointplot(
            x=[p[0] for p in points], y=[p[1] for p in points])

        if len(args) > 1:
            user2 = determine_user(args[1])
            points2 = get_user_points_history(user2)
            plot = sns.pointplot(
                x=[p[0] for p in points2], y=[p[1] for p in points2], color='red')
    
        plot.legend(handles=plot.lines[::len(points)+1], labels=args)
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

def stats_of(bot, update, args):
    if not args:
        bot.send_message(update.message.chat_id, "Usage: /statsof thampi")
        return

    query_player = args[0]
    player = determine_player(query_player)
    points = get_player_stats(player)

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


    #bot.send_message(update.message.chat_id, "Player - {}: {}".format(player.name, points))
