def get_triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return 'IncorrectTriangleSides'
    elif a == b == c:
        return 'equilateral'
    elif a == b or b == c or a == c:
        return 'isosceles'

    else:
        return 'nonequilateral'

