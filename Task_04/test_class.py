import pytest
from triangle_class import Triangle, IncorrectTriangleSides

def test_equilateral():
    t = Triangle(3, 3, 3)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == 9

def test_isosceles():
    t = Triangle(5, 5, 8)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == 18

def test_nonequilateral():
    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == 12

def test_negative_sides():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 2, 3)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, -2, 3)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, -3)

def test_zero_sides():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 1, 1)

def test_inequality_violation():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)   # 1+2=3
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 1, 3)   # 1+1<3

def test_perimeter():
    t = Triangle(2, 3, 4)
    assert t.perimeter() == 9
    t2 = Triangle(5, 5, 5)
    assert t2.perimeter() == 15