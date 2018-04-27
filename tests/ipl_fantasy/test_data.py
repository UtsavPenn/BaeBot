import arrow

from bae_bot.ipl_fantasy.data import get_matches, get_players


def test_get_matches():
    matches = get_matches()
    assert len(matches) == 56

    match = matches[0]
    starttime = arrow.get(match.starttime)
    now = arrow.now()

    assert (now.date() - starttime.date()).days >= 20


def test_teams_and_players_teams_match():
    players = get_players()
    players_teams = [player.team for player in players.values()]
    matches_teams = [team for match in get_matches() for team in match.teams]
    assert (set(players_teams) - set(matches_teams)) == set()
