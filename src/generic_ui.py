"""
Module: generic_ui.py
protocol class used for implementation of UIs
"""
from typing import Protocol

from field import Track
from player import Player
from game_types import CoordList


class UI(Protocol):
    def move(self, player: Player, positions: CoordList):
        ...

    def start_game(self, track: Track):
        ...

    def end_game(self, winner: Player):
        ...
