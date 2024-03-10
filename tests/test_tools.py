from tools import distance, next_cell, find_neighbours, check_inside_field


def test_distance():
    testing_point_1 = (3, 4)
    testing_point_2 = (5, 1)
    expected_result = (2, -3)

    assert distance(testing_point_1, testing_point_2) == expected_result


def test_next_cell():
    testing_point = (3, 4)
    distance = (-1, 3)
    expected_result = (2, 7)

    assert next_cell(testing_point, distance) == expected_result


def test_find_neighbours():
    testing_point = (3, 4)
    expected_result = [(2, 3), (2, 4), (2, 5),
                       (3, 3), (3, 5),
                       (4, 3), (4, 4), (4, 5)]

    assert find_neighbours(testing_point, exclude_coord=True) == expected_result
    expected_result = [(2, 3), (2, 4), (2, 5),
                       (3, 3), (3, 4), (3, 5),
                       (4, 3), (4, 4), (4, 5)]
    assert find_neighbours(testing_point) == expected_result


def test_check_inside_field():
    assert check_inside_field((-1, 2), (20, 30)) is False
    assert check_inside_field((10, 20), (20, 30)) is True
    assert check_inside_field((10, 30), (20, 30)) is False
