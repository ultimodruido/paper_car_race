from field import import_track, Track


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


def test_get_field_type():
    t = Track("test_track.csv")
    assert "G" == t.get_field_type((0,0))