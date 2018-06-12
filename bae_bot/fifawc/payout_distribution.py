from bae_bot.fifawc.models import EventInfo, BetsHistory

def get_payout_distribution(event_id):
    distribution = {}
    event_info = EventInfo.get(event_id)
    outcomes = event_info.event_result_choices
    bets = [bet for bet in BetsHistory.scan() if bet.event_id == event_id]

    total_amount = sum((bet.bet_amount for bet in bets))
    for outcome in outcomes:
        pledged_amount = sum((bet.bet_amount for bet in bets if bet.result == outcome))
        if pledged_amount:
            distribution[outcome] = total_amount/pledged_amount

    return distribution
