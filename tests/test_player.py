from player import Player


def test_player_position():
    player = Player("G")
    player.position = (3, 2)
    player.position = (4, 4)
    assert (4, 4) == player._position
    assert (3, 2) == player._prev_position


def test_player_next_position():
    player = Player("G")
    player.position = (3, 2)
    player.position = (4, 4)
    assert (5, 6) == player.next_position()
