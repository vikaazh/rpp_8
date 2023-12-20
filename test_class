import pytest
from triangle_class import Triangle, IncorrectTriangleSides


# Позитивные тесты для корректного создания объекта-треугольника
def valid_triangle_creation():
    triangle = Triangle(5, 5, 5)
    assert triangle.a == 5
    assert triangle.b == 5
    assert triangle.c == 5


# Позитивные тесты для метода triangle_type
def triangle_type():
    triangle = Triangle(5, 5, 5)
    assert triangle.triangle_type() == 'equilateral'

    triangle = Triangle(5, 5, 3)
    assert triangle.triangle_type() == 'isosceles'

    triangle = Triangle(3, 4, 5)
    assert triangle.triangle_type() == 'nonequilateral'


# Позитивные тесты для метода perimeter
def perimeter():
    triangle = Triangle(5, 5, 5)
    assert triangle.perimeter() == 15

    triangle = Triangle(3, 4, 5)
    assert triangle.perimeter() == 12


# Негативные тесты для некорректного создания объекта-треугольника
def invalid_triangle_creation():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 0, 0)

    with pytest.raises(IncorrectTriangleSides):
        Triangle(3, 3, 7)


# Вызов pytest
if __name__ == "__main__":
    pytest.main()
