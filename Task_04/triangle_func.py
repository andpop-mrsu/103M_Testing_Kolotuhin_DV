# triangle_func.py

class IncorrectTriangleSides(Exception):
    """Исключение, выбрасываемое при некорректных сторонах треугольника."""
    pass

def get_triangle_type(a, b, c):
    """
   
        a, b, c (числа): длины сторон треугольника.

        str: "equilateral" (равносторонний),
             "isosceles" (равнобедренный),
             "nonequilateral" (разносторонний).

        IncorrectTriangleSides: если стороны не удовлетворяют условиям
                                (не положительные или нарушено неравенство треугольника).

    Примеры:
    >>> get_triangle_type(3, 3, 3)
    'equilateral'
    >>> get_triangle_type(3, 3, 5)
    'isosceles'
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(0, 1, 1)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides
    >>> get_triangle_type(1, 2, 3)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides
    >>> get_triangle_type(1, 1, 3)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides
    """
    # Проверка корректности сторон
    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Стороны должны быть положительными числами")
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("Нарушено неравенство треугольника")
    
    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "nonequilateral"