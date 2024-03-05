"""
Module: field.py
function and memory structure to load and manage the track field
"""
import csv

type TrackType = list[list[str]]

field_type = ("S", "F", "G", "T")


def import_track(filename: str) -> TrackType:
    """
    read the given cvs file and build the memory map of the field
    :param filename: csv file
    :return: 2D table (list of list) with the type of fields
    the 2d table is address as track[row][column], first the row then the column
    in a Cartesian plane track[Y][X] first with the vertical coordinate
    """
    track = list()
    with open(filename) as csv_file:
        csv_content = csv.reader(csv_file, delimiter=',')
        for row in csv_content:
            for item in row:
                if item not in field_type:
                    raise ValueError("Allowed fields are 'S', 'F', 'G', 'T'")
            track.append(row)
    return track


class Track:
    def __init__(self, filename):
        # import track
        self._track = import_track(filename)
        self.rows = len(self._track)
        self.columns = len(self._track[0])

    def get_field_type(self, coord: tuple[int, int]) -> str:
        if coord[0] >= self.rows:
            raise IndexError("Coordinates out of range")
        if coord[1] >= self.columns:
            raise IndexError("Coordinates out of range")
        return self._track[coord[0]][coord[1]]
