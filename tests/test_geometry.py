import pytest
from math import pi
import sys
sys.path.append('../geometric_lib')
from calculate import calc


@pytest.mark.parametrize('size, expected, is_correct', [
        ({2}, 4, True),
        ({5}, 25, True),
        ({10}, 1, False),
        ({-4}, -16, False)
        
    ])
def test_area_square(size, expected, is_correct):
    if (is_correct):
        assert expected == calc('square', 'area', size)
    else:
        assert expected != calc('square', 'area', size)


@pytest.mark.parametrize('size, expected, is_correct', [
        ({2}, 8, True),
        ({5}, 20, True),
        ({-5}, 10, False),
        ({'world'}, 10, False)
    ])
def test_perimeter_square(size, expected, is_correct):
    if (is_correct):
        assert expected == calc('square', 'perimeter', size)
    else:
        assert expected != calc('square', 'perimeter', size)


@pytest.mark.parametrize('size, expected, is_correct', [
        ({6, 8, 10}, 24, True),
        ({-6, -8, 10}, -24, False),
        ({7, 24, 25}, 84, True)
])
def test_area_triangle(size, expected, is_correct):
    if (is_correct):
        assert expected == calc('triangle', 'area', size)
    else:
        assert expected != calc('triangle', 'area', size)


@pytest.mark.parametrize('size, expected, is_correct', [
        ({5, 12, 13}, 30, True),
        ({-5, -12, 13}, 26, False),
        ([3, 3, 3], 9, True),
        ({3, 4, 50}, 57, True)
])
def test_perimeter_triangle(size, expected, is_correct):
    if (is_correct):
        assert expected == calc('triangle', 'perimeter', size)
    else:
        assert expected != calc('triangle', 'perimeter', size)


@pytest.mark.parametrize('size, expected, is_correct', [
        ({2, 3}, 6, True),
        ({-5, -4}, -20, False),
        ({6, 9}, 54, True),
        ({50, 100}, 5000, True)
])
def test_area_rectangle(size, expected, is_correct):
    if (is_correct):
        assert expected == calc('rectangle', 'area', size)
    else:
        assert expected != calc('rectangle', 'area', size)


@pytest.mark.parametrize('size, expected, is_correct', [
        ({4, 6}, 20, True),
        ({-4, -6}, 20, False),
        ([2, 2], 8, True),
        ({8, 15}, 46, True),
        ([60, 60], 60, False)
])
def test_perimeter_rectangle(size, expected, is_correct):
    if (is_correct):
        assert expected == calc('rectangle', 'perimeter', size)
    else:
        assert expected != calc('rectangle', 'perimeter', size)


@pytest.mark.parametrize('size, expected, is_correct', [
        ({2}, 4 * pi, True),
        ({-2}, 4 * pi, True),
        ({7}, 49 * pi, True),
        ({-12}, 121 * pi, False)
])
def test_circle_area(size, expected, is_correct):
    if (is_correct):
        assert expected == calc('circle', 'area', size)
    else:
        assert expected != calc('circle', 'area', size)


@pytest.mark.parametrize('size, expected, is_correct', [
        ({2}, 4 * pi, True),
        ({-2}, 4 * pi, False),
        ({7}, 14 * pi, True),
        ({20}, 40 * pi, True)
])
def test_perimeter_area(size, expected, is_correct):
    if (is_correct):
        assert expected == calc('circle', 'perimeter', size)
    else:
        assert expected != calc('circle', 'perimeter', size)
