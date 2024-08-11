class Tortuga:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.edad = 0

    def celebrar_anivesario(self):
        self.edad += 1
        return "¡Estoy de cumpleaños!"