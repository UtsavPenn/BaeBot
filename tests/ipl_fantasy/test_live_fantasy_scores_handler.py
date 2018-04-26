from bae_bot.ipl_fantasy.handlers.live_fantasy_scores_handler import live_fantasy_scores


def test_live_fantasy_scores_handler(bot, update):
    live_fantasy_scores(bot, update, ['tharun'])

    send_message_args = bot.mock_calls[0][1]
    text = send_message_args[1]

    assert "Live Points: " in text
