"""
Module: player.py
Class describing the player
"""
from tools import next_cell, distance


class Player:
    def __init__(self, color: str):
        self._position = (-1, -1)
        self._prev_position = (-1, -1)
        self.color = color

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self._prev_position = self.position
        self._position = new_position

    def next_position(self):
        return next_cell(self.position, distance(self._prev_position, self.position))
