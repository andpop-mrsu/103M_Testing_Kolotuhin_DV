# triangle_class.py

class IncorrectTriangleSides(Exception):
    """Исключение, выбрасываемое при некорректных сторонах треугольника."""
    pass

class Triangle:
    def __init__(self, a, b, c):
        """
        Конструктор треугольника.
        Проверяет корректность сторон (положительные и неравенство треугольника).
        """
        if a <= 0 or b <= 0 or c <= 0:
            raise IncorrectTriangleSides("Стороны должны быть положительными числами")
        if a + b <= c or a + c <= b or b + c <= a:
            raise IncorrectTriangleSides("Нарушено неравенство треугольника")
        self.a = a
        self.b = b
        self.c = c
    
    def triangle_type(self):
        """Возвращает тип треугольника."""
        a, b, c = self.a, self.b, self.c
        if a == b == c:
            return "equilateral"
        elif a == b or a == c or b == c:
            return "isosceles"
        else:
            return "nonequilateral"
    
    def perimeter(self):
        """Возвращает периметр треугольника."""
        return self.a + self.b + self.c