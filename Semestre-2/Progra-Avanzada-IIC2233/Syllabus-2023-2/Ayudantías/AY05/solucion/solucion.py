import json
from os import path

with open(path.join("data", "actos.json"), "rb") as file:
    actos = json.load(file)

with open(path.join("data", "generos.json"), "rb") as file:
    generos = json.load(file)


class Concierto:

    def __init__(self):
        self.actos = []
        self.planificacion = []

    def agregar_acto(self, acto):
        self.actos.append(acto)

    def eliminar_acto(self, acto):
        self.actos.remove(acto)

    def validar_actos(self):
        # COMPLETAR
        por_eliminar = []
        for b in self.actos:
            try:
                print("Verificando acto:", b.nombre)
                b.verificar_datos()
            except ValueError as e:
                print("Eliminando acto del concierto. Motivo:")
                print(e.args[0])
                por_eliminar.append(b)
            else:
                print("Acto verificado exitosamente.\n")

        for b in por_eliminar:
            self.eliminar_acto(b)

    def planificar_concierto(self):
        # COMPLETAR

        # Ordenar los actos en orden ascendente de interes
        for b in self.actos:
            b.calcular_interes(generos)

        self.actos.sort(key=lambda b: b.interes)

        # Generar una archivo serializado en JSON con las bandas planificadas
        actos = [self.actos[i].__dict__ for i in range(len(self.actos))]
        json.dump(actos, open("planificacion.json", "w"))

        # E imprimir los actos en orden
        print("PLANIFICACIÓN DEL FESTIVAL:")
        for i, b in enumerate(self.actos):
            print(f"{i+1}. {b.nombre} - {b.genero}" +
                  f"- Se presentará(n) por {b.largo_acto} minutos.")


class Acto:

    def __init__(self, nombre, largo_acto, miembros, genero, llave):
        self.nombre = nombre
        self.largo_acto = largo_acto
        self.miembros = miembros
        self.genero = genero
        self.llave = llave
        self.interes = 0

    def serializar_llave(self):
        # COMPLETAR
        self.llave = bytearray(self.llave.encode("utf-8"))

    def deserializar_llave(self):
        # COMPLETAR
        self.llave = self.llave.decode("utf-8")

    def determinar_big_o_little(self):
        # COMPLETAR
        resultado = self.llave[0] % 2 == 0
        return resultado

    def calcular_interes(self, interes_por_genero):
        # COMPLETAR
        try:
            self.interes = self.largo_acto * interes_por_genero[self.genero]
        except KeyError:
            self.interes = 0

    def verificar_datos(self):
        # COMPLETAR
        self.serializar_llave()

        # Dividir los bytes
        bytes_datos = self.llave[1:]
        bytes_1 = bytes_datos[:2]
        bytes_2 = bytes_datos[2:]

        # Obtener numeros desde secuencias
        # Si es big endian
        if self.determinar_big_o_little():
            num_1 = int.from_bytes(bytes_1, byteorder="big")
            num_2 = int.from_bytes(bytes_2, byteorder="big")
        else:
            num_1 = int.from_bytes(bytes_1, byteorder="little")
            num_2 = int.from_bytes(bytes_2, byteorder="little")

        # Realizar operaciones
        num_miembros = abs(num_1 - num_2) % 10
        num_largo = abs(num_1 + num_2) % 100
        self.deserializar_llave()

        if num_miembros - self.miembros or num_largo - self.largo_acto:
            msg = ""
            if num_miembros - self.miembros:
                msg += "Número de miembros incorrecto.\n"
            if num_largo - self.largo_acto:
                msg += "Largo de show incorrecto.\n"
            raise ValueError(msg)
        else:
            return True


# COMPLETAR
concierto = Concierto()

for b in actos:
    # Cada B es un diccionario de una acto
    acto = Acto(
        b["nombre"], b["largo_acto"],
        b["miembros"], b["genero"], b["llave"]
    )
    concierto.agregar_acto(acto)

concierto.validar_actos()
concierto.planificar_concierto()
