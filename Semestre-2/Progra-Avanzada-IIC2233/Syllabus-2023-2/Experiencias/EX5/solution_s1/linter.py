import os
from parametros import PATH_CODIGO, REGLAS


class Linter:
    """
        Clase con nuestro linter. Principalmente se encarga de contener
        los menús que tiene nuestro programa y de llamar a las reglas cuando
        el usuario lo pide.
    """
    def __init__(self) -> None:
        self.nombre_archivo = None
        self.reglas = REGLAS
        self.opciones = {
            "1": {
                "texto": "Cargar un archivo nuevo",
                "funcion": self.cargar_archivo_menu,
            },
            "2": {
                "texto": "Revisar una regla individual",
                "funcion": self.ejecutar_regla_menu,
            },
            "3": {
                "texto": "Salir",
                "funcion": exit,
            },
        }

    # Menu principal del programa
    def menu(self):
        print(
            "✨ ¡Bienvenido al DCCorrector de DCCódigo! ✨"
            "\n"
        )

        if self.nombre_archivo:
            print(
                f"Archivo actualmente cargado: {self.nombre_archivo}"
                "\n"
            )
        else:
            print(
                "Todavía no hay ningún archivo cargado en el sistema."
                "\n"
            )

        while True:
            print("¿Qué deseas hacer?")
            for letra, opcion in self.opciones.items():
                print(
                    f"[{letra}] {opcion['texto']}"
                )
            opcion = input(">")
            print()
            if opcion not in self.opciones:
                print("Opción inválida. Selecciona otra.")
            else:
                self.opciones[opcion]["funcion"]()

    # Submenu para cargar archivos, las opciones las saca
    # desde la carpeta dada en los parámetros como carpeta de código
    def cargar_archivo_menu(self):
        archivos_disponibles = os.listdir(PATH_CODIGO)

        while True:
            print("¿Qué archivo deseas cargar?")
            for indice, archivo in enumerate(archivos_disponibles):
                print(
                    f"[{str(indice)}] {archivo}"
                )
            opcion = input(">")
            print()
            if opcion not in [
                str(x) for x in range(len(archivos_disponibles))
            ]:
                print("Opción inválida. Selecciona otra.")
            else:
                self.nombre_archivo = archivos_disponibles[int(opcion)]
                print(f"¡Archivo \"{self.nombre_archivo}\" cargado!")
                return

    # Menu para las reglas. Las saca del archivo de parámetros.
    def ejecutar_regla_menu(self):
        if not self.nombre_archivo:
            print(
                "No tienes ningún archivo cargado."
                "\n"
            )
            return
        while True:
            print("¿Qué regla deseas revisar?")
            for indice, opcion in enumerate(self.reglas):
                print(
                    f"[{indice}] {opcion.nombre}"
                )
            print(f"[{len(self.reglas)}] Salir")
            opcion = input(">")
            print()
            if opcion == str(len(self.reglas)):
                return
            elif opcion not in [str(x) for x in range(len(self.reglas))]:
                print("Opción inválida. Selecciona otra.")
            else:
                self.revisar_reglas(self.reglas[int(opcion)])

    # Procedimiento para revisar una regla.
    # Abre el archivo, le pasa su contenido al método de revisar
    # de cada regla, y luego imprime el resumen de faltas encontradas
    def revisar_reglas(self, regla_a_revisar):
        with open(
            os.path.join(PATH_CODIGO, self.nombre_archivo),
            'r',
            encoding="UTF-8"
        ) as archivo:
            contenido = archivo.readlines()
            regla_a_revisar.reiniciar_faltas()
            regla_a_revisar.revisar_regla(self.nombre_archivo, contenido)
            regla_a_revisar.imprimir_resumen()
