class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __add__(self, other):
        nuevo_den = self.den*other.den
        nuevo_num = self.den*other.num + other.den*self.num
        return Fraccion(nuevo_num,nuevo_den)

f = Fraccion(1, 4)
g = Fraccion(1, 2)
h = f+g
print(h)
