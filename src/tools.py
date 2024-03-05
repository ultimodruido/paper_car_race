"""
Module: tools.py
Collection of useful utilities
"""


def distance(coord_start: tuple[int, int], coord_end: tuple[int, int]) -> tuple[int, int]:
    """
    Calculate the distance in X,Y direction on a 2d map
    :param coord_start:
    :param coord_end:
    :return: tuple(delta X, delta Y)
    """
    return coord_end[0] - coord_start[0], coord_end[1] - coord_start[1]


def next_cell(coord_start: tuple[int, int], distance: tuple[int, int]) -> tuple[int, int]:
    """
    Returns the coordinates of the new cell when moving from coord_start for the given distance
    :param coord_start:
    :param distance:
    :return: new (x, y) coordinates
    """
    return coord_start[0] + distance[0], coord_start[1] + distance[1]


def find_neighbours(coord: tuple[int, int]) -> list[tuple[int, int]]:
    """
    provide a list of all neighbour cells, the list does not include the starting cell
    :param coord:
    :return:
    """
    neighbours = list()
    for x in range(coord[0] - 1, coord[0] + 2):
        for y in range(coord[1] - 1, coord[1] + 2):
            neighbours.append((x, y))

    neighbours.remove(coord)
    return neighbours
