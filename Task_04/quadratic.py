def solve_quadratic(a, b, c):
    """
    Решает квадратное уравнение ax^2 + bx + c = 0.
    Возвращает список корней (действительных) в порядке возрастания.
    Если корней нет, возвращает пустой список.
    Если уравнение тождество (0=0), возвращает None.
    """
    if a == 0:
        if b == 0:
            if c == 0:
                return None  # бесконечно много решений
            else:
                return []    # нет решений
        else:
            return [-c / b]
    else:
        D = b**2 - 4*a*c
        if D < 0:
            return []
        elif D == 0:
            x = -b / (2*a)
            return [x]
        else:
            sqrt_D = D**0.5
            x1 = (-b - sqrt_D) / (2*a)
            x2 = (-b + sqrt_D) / (2*a)
            return sorted([x1, x2])