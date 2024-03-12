"""
Module: field.py
function and memory structure to load and manage the track field
"""
type Row = int
type Col = int
type Coord = tuple[Row, Col]
type CoordList = list[tuple[Row, Col]]

type FieldType = str


class FieldTypes:
    Grass: FieldType = "G"
    Track: FieldType = "T"
    Start: FieldType = "S"
    Finish: FieldType = "F"
    _elems = [Grass, Track, Start, Finish]

    def __iter__(self):
        return iter(self._elems)


type TrackType = list[list[FieldType]]
