class Punto2D:

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __str__(self):
        return f'[{self.x}, {self.y}]'

    def distancia(self, other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5

punto1 = Punto2D(0,5)
punto2 = Punto2D(5,-10)

print(punto1.x, punto1.y)
print(punto2.x, punto2.y)

print(punto1.distancia(punto2))