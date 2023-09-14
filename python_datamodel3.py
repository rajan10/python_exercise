from math import hypot, atan


"""
p1 =Polynomial(3,2,1)
p2= Polynomial(4,3,1)
p3= p1+p2  
"""


class Polynomial:
    def __init__(self, first_term, second_term, third_term):
        self.first_term = first_term
        self.second_term = second_term
        self.third_term = third_term

    def __add__(self, other) -> object:
        return (
            self.first_term + other.first_term,
            self.second_term + other.second_term,
            self.third_term + other.third_term,
        )

    def __str__(self, other) -> str:
        return f"""Sum of {self.first_term, self.second_term, self.third_term} and {other.first_term, other.second_term, other.third_term} is
         {self.first_term + other.first_term,
            self.second_term + other.second_term,
            self.third_term + other.third_term,}"""


p1 = Polynomial(1, 2, 3)
p2 = Polynomial(3, 2, 1)
sum = p1 + p2
print(sum)
