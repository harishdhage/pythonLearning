class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Vector ({self.a}, {self.b})'

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Vector(self.a - other.a, self.b - other.b)

    def __mul__(self, scalar):
        return Vector(self.a * scalar, self.b * scalar)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)        # Vector (7, 8)
print(v1 - v2)        # Vector (-3, 12)
print(v1 * 3)         # Vector (6, 30)
print(v1 == v2)       # False