from PyQt6.QtCore import QObject, pyqtSignal


class Procesador(QObject):
    senal_actualizar = pyqtSignal(str)

    def es_valido(self, texto: str) -> bool:
        for valor in texto.split(','):
            if not valor.isnumeric():
                return False
        return True

    def ordenar(self, lista_de_numeros: list) -> list:
        lista_de_numeros.sort()
        return lista_de_numeros

    def procesar_input(self, texto_input: str) -> None:
        texto_input = texto_input.replace(' ', '').strip(',')
        if not self.es_valido(texto_input):
            self.actualizar_interfaz('Input no válido')
            return
        lista_de_numeros = [int(porcion) for porcion in texto_input.split(',')]
        numeros_ordenados = self.ordenar(lista_de_numeros)
        texto_resultado = ", ".join([str(numero)
                                    for numero in numeros_ordenados])
        self.actualizar_interfaz(texto_resultado)

    def actualizar_interfaz(self, texto: str) -> None:
        self.senal_actualizar.emit(texto)
