"""
Module: field.py
function and memory structure to load and manage the track field
"""
import csv
from game_types import TrackType, FieldTypes, Coord, FieldType, CoordList
from tools import check_inside_field


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
                if item not in FieldTypes():
                    raise ValueError("Allowed fields are 'S', 'F', 'G', 'T'")
            track.append(row)
    return track


class Track:
    def __init__(self, filename):
        # import track
        self._track: TrackType = import_track(filename)
        self.rows = len(self._track)
        self.columns = len(self._track[0])

    def get_field_type(self, coord: Coord) -> FieldType:
        if check_inside_field(coord, self.size):
            return self._track[coord[0]][coord[1]]
        else:
            raise IndexError("Coordinates out of range")

    def get_field_list_by_type(self, field_type: FieldType) -> CoordList:
        match_list = list()
        for row in range(self.rows):
            for col in range(self.columns):
                if self.get_field_type((row, col)) == field_type:
                    match_list.append((row, col))
        return match_list

    @property
    def size(self) -> tuple[int, int]:
        return self.rows, self.columns
