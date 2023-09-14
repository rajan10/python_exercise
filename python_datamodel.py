from math import hypot

# class is designed by developer
# and what input is needed to pass, is passed to instance when calling.


class Vector2d:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __abs__(self) -> float:  # is overloaded here to call hypot we sums hypotenus
        return hypot(self.x, self.y)


vector = Vector2d(3, 4)
print(abs(vector))
