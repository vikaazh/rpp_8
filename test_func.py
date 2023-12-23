import unittest

from main import get_triangle_type


class TestTriangleType(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(get_triangle_type(10, 10, 10), 'equilateral')

    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(1, 2, 3), 'nonequilateral')

    def test_isosceles(self):
        self.assertEqual(get_triangle_type(2, 2, 1), 'isosceles')
        self.assertEqual(get_triangle_type(2, 1, 2), 'isosceles')
        self.assertEqual(get_triangle_type(1, 2, 2), 'isosceles')

    def test_incorrect_sides(self):
        self.assertEqual(get_triangle_type(2, 2, 4), 'IncorrectTriangleSides')
        self.assertEqual(get_triangle_type(0, 0, 0), 'IncorrectTriangleSides')
        self.assertEqual(get_triangle_type(6, 8, 10), 'IncorrectTriangleSides')


if __name__ == '__main__':
    unittest.main()
