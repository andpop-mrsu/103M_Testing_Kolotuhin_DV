import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestTriangleType(unittest.TestCase):
    
    def test_equilateral(self):
        self.assertEqual(get_triangle_type(3, 3, 3), "equilateral")
        self.assertEqual(get_triangle_type(5, 5, 5), "equilateral")
    
    def test_isosceles(self):
        self.assertEqual(get_triangle_type(3, 3, 5), "isosceles")
        self.assertEqual(get_triangle_type(4, 6, 4), "isosceles")
        self.assertEqual(get_triangle_type(7, 5, 5), "isosceles")
    
    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")
        self.assertEqual(get_triangle_type(2, 3, 4), "nonequilateral")
    
    def test_negative_sides(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 2, 3)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, -2, 3)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, -3)
    
    def test_zero_sides(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 1, 1)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 0, 1)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 1, 0)
    
    def test_inequality_violation(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)   # 1+2=3
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 1, 3)   # 1+1<3
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(5, 1, 2)   # 1+2<5

if __name__ == '__main__':
    unittest.main()