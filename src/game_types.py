"""
Module: field.py
function and memory structure to load and manage the track field
"""
from enum import Enum

type Row = int
type Col = int
type Coord = tuple[Row, Col]
type CoordList = list[tuple[Row, Col]]

type FieldType = str


class FieldEnum(Enum):
    G: FieldType = "G"
    T: FieldType = "T"
    S: FieldType = "S"
    F: FieldType = "F"


type TrackType = list[list[FieldType]]
