import math
import sys
sys.path.append('../geometric_lib')  # Убедитесь, что путь корректный
import calculate

def test_circle_area():
    radius = 3
    expected = math.pi * radius * radius
    assert expected == calculate.calc('circle', 'area', [radius])

def test_circle_perimeter():
    radius = 3
    expected = 2 * math.pi * radius
    assert expected == calculate.calc('circle', 'perimeter', [radius])

def test_square_area():
    side = 4
    expected = side * side
    assert expected == calculate.calc('square', 'area', [side])

def test_square_perimeter():
    side = 4
    expected = 4 * side
    assert expected == calculate.calc('square', 'perimeter', [side])

def test_rectangle_area():
    width, height = 5, 6
    expected = width * height
    assert expected == calculate.calc('rectangle', 'area', [width, height])

def test_rectangle_perimeter():
    width, height = 5, 6
    expected = 2 * (width + height)
    assert expected == calculate.calc('rectangle', 'perimeter', [width, height])


def test_triangle_area():
    side1, side2, side3 = 3, 4, 5
    pol_p = (side1 + side2 + side3) / 2
    expected = (pol_p * (pol_p - side1) * (pol_p - side2) * (pol_p - side3)) ** 0.5
    assert expected == calculate.calc('triangle', 'area', [side1, side2, side3])

def test_triangle_perimeter():
    side1, side2, side3 = 3, 4, 5
    expected = side1 + side2 + side3
    assert expected == calculate.calc('triangle', 'perimeter', [side1, side2, side3])
