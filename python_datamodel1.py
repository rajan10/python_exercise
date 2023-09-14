from math import hypot


class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return hypot(self.x, self.y)

    def __gt__(self, other) -> bool:
        return abs(self) > abs(other)


vector_a = Vector2d(3, 6)
vector_b = Vector2d(5, 6)
if vector_a > vector_b:
    print("Hello")
