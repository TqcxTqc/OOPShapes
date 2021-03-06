import pytest
from shapes.triangle import Triangle
from shapes.rectangle import Rectangle
from shapes import BaseShape


def test_rectangle_angles_equals_four():
    rectangle = Rectangle(10, 6)
    assert rectangle.get_angles() == 4


def test_rectangles_equals_area_after_add_area():
    rectangle_1 = Rectangle(5, 2)
    triangle_2 = Triangle(6, 3)
    assert rectangle_1.add_area(triangle_2) == triangle_2.add_area(rectangle_1)


def test_error_if_not_figure():
    rectangle = Rectangle(5, 2)
    with pytest.raises(Exception):
        rectangle.add_area(object())


def test_name_rectangle():
    rectangle = Rectangle(5, 2)
    assert rectangle.get_name() == "Rectangle"


def test_rectangle_is_instance_figure():
    assert isinstance(Rectangle(5, 2), BaseShape)
