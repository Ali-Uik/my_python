class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


vector1 = Vector(5, 6)
vector2 = Vector(3, 2)
print(vector1)
print(vector2)
print(vector1 + vector2)
print(vector1.distance(vector2))
