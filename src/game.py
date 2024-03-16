"""
Module: game.py
game mechanics
"""
from random import shuffle
from field import Track
from game_types import FieldTypes, CoordList
from generic_ui import UI
from tools import find_neighbours, check_inside_field


class Game:
    def __init__(self, player_list: list, track: Track, ui: UI):
        self.players = player_list
        shuffle(self.players)
        self.track = track
        self.ui = ui

    @property
    def player_positions(self):
        return (player.position for player in self.players)

    def start_game(self):
        # initiate the UI
        self.ui.start_game(self.track)

        for player in self.players:
            start_positions = [pos for pos in self.track.get_field_list_by_type(FieldTypes.Start)
                               if pos not in self.player_positions]

            player.position = self.ui.move(player, start_positions)

    def game_loop(self) -> bool:
        # calculate positions for the next move
        for player in self.players:
            choice_positions = self.player_choice(player)

            # check if possible position is not an empty list.
            if choice_positions:
                player.position = self.ui.move(player, choice_positions)
                # check if player won
                if self.track.get_field_type(player.position) == FieldTypes.Finish:
                    # notify UI about the winner
                    self.ui.end_game(player)
                    return False

        return True

    def player_choice(self, player) -> CoordList:
        if self.track.get_field_type(player.position) == FieldTypes.Grass:
            target_position = player.position
        else:
            target_position = player.next_position()
        # get neighbours & remove already occupied positions
        choice_positions = [pos for pos in find_neighbours(target_position)
                            if pos not in self.player_positions]
        # remove options outside field
        choice_positions = [pos for pos in choice_positions
                            if check_inside_field(pos, self.track.size)]
        return choice_positions
