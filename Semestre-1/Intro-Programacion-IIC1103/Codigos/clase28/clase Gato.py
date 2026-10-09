class Gato:
    def __init__(self, nombre, color, peso, edad, ultima_vacuna):
        self.nombre = nombre
        self.color = color
        self.peso = peso
        self.edad = edad
        self.ultima_vacuna = ultima_vacuna

    def __str__(self):
        return f'{self.nombre}: color: {self.color}, peso: {self.peso}, edad: {self.edad}, vacuna: {self.ultima_vacuna}'

    def __repr__(self):
        return str(self)

def criterio(item):
    return -1*item.edad, item.nombre

garf = Gato("Garfield", "Naranjo", 8, 10, 2023)
tom = Gato("Tom", "Gris", 5, 15, 2018)
silv = Gato("Silvestre", "Blanco y negro", 8, 12, 2025)
bot = Gato("Gato con Botas", "Naranjo", 4, 10, 2019)
grump = Gato("Grumpy Cat", "Gris", 8, 10, 2019)

gatos = [garf, tom, silv, bot, grump]
#print(gatos): para cada gato llama a __repr__ y no a __str__

gatos.sort(key=criterio)
for g in gatos:
    print(g)
