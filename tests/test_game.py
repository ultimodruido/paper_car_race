from random import choice
from field import Track
from game_types import FieldTypes
from player import Player
from game import CoordList, Game


class MockUI:
    def start_game(self, track: Track):
        pass

    def end_game(self, winner: Player):
        pass

    def move(self, player: Player, positions: CoordList):
        return choice(positions)


def test_start_game():
    g = Game([Player('W'), Player('R')], Track("test_track.csv"), MockUI())
    g.start_game()

    for player in g.players:
        assert FieldTypes.Start == g.track.get_field_type(player.position)


def test_player_positions():
    player_w = Player('W')
    player_r = Player('R')
    g = Game([player_w, player_r], Track("test_track.csv"), MockUI())

    player_w.position = (0, 1)
    player_r.position = (1, 1)

    expected_result = [player_w.position, player_r.position]
    result = list(g.player_positions)

    assert expected_result.sort() == result.sort()


def test_player_choice_in_grass():
    player_w = Player('W')
    player_r = Player('R')
    g = Game([player_w, player_r], Track("test_track.csv"), MockUI())

    player_w.position = (0, 1)
    player_r.position = (1, 1)

    player_w_choice = g.player_choice(player_w)
    expected_result = [(0, 0), (0, 2), (1, 0), (1, 2)]

    assert player_w_choice.sort() == expected_result.sort()


def test_game_loop_true(mocker):
    mocker.patch('field.Track.get_field_type', return_value=FieldTypes.Track)

    player_w = Player('W')
    player_w.position = (1, 0)
    player_w.position = (2, 1)
    g = Game([player_w], Track("test_track.csv"), MockUI())
    assert g.game_loop() is True


def test_game_loop_false(mocker):
    mocker.patch('field.Track.get_field_type', return_value=FieldTypes.Finish)

    player_w = Player('W')
    player_w.position = (1, 0)
    player_w.position = (2, 1)
    g = Game([player_w], Track("test_track.csv"), MockUI())
    assert g.game_loop() is False
