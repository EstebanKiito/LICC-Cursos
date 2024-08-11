import json
from os import path

# COMPLETAR LECTURA JSON


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
        pass

    def planificar_concierto(self):
        # COMPLETAR
        pass


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
        pass

    def deserializar_llave(self):
        # COMPLETAR
        pass

    def determinar_big_o_little(self):
        # COMPLETAR
        pass

    def calcular_interes(self, interes_por_genero):
        # COMPLETAR
        pass

    def verificar_datos(self):
        # COMPLETAR
        pass


# COMPLETAR FLUJO PRINCIPAL
