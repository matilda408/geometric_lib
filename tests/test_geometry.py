import math
import sys 
sys.path.append('../geometric_lib')
import calculate



# Тесты для фигуры Circle
class TestCircle:
    def test_circle_area(self):
        radius = 3
        assert math.pi * radius * radius == calculate.calc('circle', 'area', [radius])

    def test_circle_perimeter(self):
        radius = 3
        assert 2 * math.pi * radius == calculate.calc('circle', 'perimeter', [radius])


# Тесты для фигуры Square
class TestSquare:
    def test_square_area(self):
        side = 4
        assert side * side == calculate.calc('square', 'area', [side])

    def test_square_perimeter(self):
        side = 4
        assert 4 * side == calculate.calc('square', 'perimeter', [side])


# Тесты для фигуры Rectangle
class TestRectangle:
    def test_rectangle_area(self):
        width, height = 5, 6
        assert width * height == calculate.calc('rectangle', 'area', [width, height])

    def test_rectangle_perimeter(self):
        width, height = 5, 6
        assert 2 * (width + height) == calculate.calc('rectangle', 'perimeter', [width, height])


# Тесты для фигуры Triangle
class TestTriangle:
    def test_triangle_area(self):
        side1, side2, side3 = 3, 4, 5
        pol_p = (side1 + side2 + side3) / 2
        result = (pol_p * (pol_p - side1) * (pol_p - side2) * (pol_p - side3)) ** 0.5
        assert result == calculate.calc('triangle', 'area', [side1, side2, side3])

    def test_triangle_perimeter(self):
        side1, side2, side3 = 3, 4, 5
        assert side1 + side2 + side3 == calculate.calc('triangle', 'perimeter', [side1, side2, side3])
