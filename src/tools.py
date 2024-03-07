"""
Module: tools.py
Collection of useful utilities
"""
from game_types import Coord, CoordList


def distance(coord_start: Coord, coord_end: Coord) -> Coord:
    """
    Calculate the distance in X,Y direction on a 2d map
    :param coord_start:
    :param coord_end:
    :return: tuple(delta X, delta Y)
    """
    return coord_end[0] - coord_start[0], coord_end[1] - coord_start[1]


def next_cell(coord_start: Coord, distance: Coord) -> Coord:
    """
    Returns the coordinates of the new cell when moving from coord_start for the given distance
    :param coord_start:
    :param distance:
    :return: new (x, y) coordinates
    """
    return coord_start[0] + distance[0], coord_start[1] + distance[1]


def find_neighbours(coord: Coord, exclude_coord: bool = False) -> CoordList:
    """
    provide a list of all neighbour cells, the list does not include the starting cell
    :param coord:
    :return:
    """
    neighbours = list()
    for x in range(coord[0] - 1, coord[0] + 2):
        for y in range(coord[1] - 1, coord[1] + 2):
            neighbours.append((x, y))

    if exclude_coord:
        neighbours.remove(coord)
    return neighbours
