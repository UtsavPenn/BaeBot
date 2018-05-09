from bae_bot.ipl_fantasy.common import determine_player


def test_determine_player():
    player = determine_player('thamp')
    assert player.name.startswith('Basil')
    assert player.name.endswith('(uc)')
    assert player.team == "sunrisers-hyderabad"

