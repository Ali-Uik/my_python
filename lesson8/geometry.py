PI = 3.14


def SofSquare(a):
    return a * a


def PofSquare(a):
    return a * 4


# написат функции для нахождения плоўади и периметра
# треугольника, прямоугольника и круга

def PofRectangle(a, b):
    return a * 2 + b * 2


def SofRectangle(a, b):
    return a * b


def PofCircle(r):
    return 2 * PI * r


def SofCircle(r):
    return PI * (r ** 2)


def PofTriangel(a, b, c):
    return a + b + c


def SofTriangle(h, a):
    return (h * a) / 2
