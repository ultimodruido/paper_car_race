import pytest

from field import import_track, Track
from game_types import FieldTypes


def test_import_track():
    track = import_track("test_track.csv")
    expected_track = [
        ["G", "G", "G", "G", "G"],
        ["S", "T", "T", "T", "G"],
        ["S", "T", "T", "T", "G"],
        ["G", "G", "T", "T", "G"],
        ["G", "G", "F", "F", "G"],
    ]
    assert expected_track == track


def test_import_track_wrong():
    with pytest.raises(ValueError):
        track = import_track("test_track_wrong.csv")


def test_get_field_type():
    t = Track("test_track.csv")
    assert FieldTypes.Grass == t.get_field_type((0, 0))


def test_get_field_type_error():
    t = Track("test_track.csv")
    with pytest.raises(IndexError):
        t.get_field_type((20, 20))


def test_get_field_list_by_type():
    t = Track("test_track.csv")
    expected_result = [(1, 0), (2, 0)]
    assert t.get_field_list_by_type(FieldTypes.Start) == expected_result
