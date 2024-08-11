from typing import List
from clases import Tortuga
import pickle


###################
#### ENCRIPTAR ####
###################
def serializar_tortuga(tortuga: Tortuga) -> bytearray:
    # Completar
    pass


def verificar_rango(mensaje: bytearray, inicio: int, fin: int) -> None:
    # Completar
    pass


def codificar_rango(inicio: int, fin: int) -> bytearray:
    # Completar
    pass


def codificar_largo(largo: int) -> bytearray:
    # Completar
    pass


def separar_msg(mensaje: bytearray, inicio: int, fin: int) -> List[bytearray]:
    m_extraido = bytearray()
    m_con_mascara = bytearray()
    # Completar

    return [m_extraido, m_con_mascara]


def encriptar(mensaje: bytearray, inicio: int, fin: int) -> bytearray:
    # Se la damos listas
    verificar_rango(mensaje, inicio, fin)

    m_extraido, m_con_mascara = separar_msg(mensaje, inicio, fin)
    rango_codificado = codificar_rango(inicio, fin)
    return (
        codificar_largo(fin - inicio + 1)
        + m_extraido
        + m_con_mascara
        + rango_codificado
    )


######################
#### DESENCRIPTAR ####
######################
def deserializar_tortuga(mensaje_codificado: bytearray) -> Tortuga:
    # Completar
    pass


def decodificar_largo(mensaje: bytearray) -> int:
    # Completar
    pass


def separar_msg_encriptado(mensaje: bytearray) -> List[bytearray]:
    m_extraido = bytearray()
    m_con_mascara = bytearray()
    rango_codificado = bytearray()
    # Completar

    return [m_extraido, m_con_mascara, rango_codificado]


def decodificar_rango(rango_codificado: bytearray) -> List[int]:
    inicio = None
    fin = None
    # Completar

    return [inicio, fin]


def desencriptar(mensaje: bytearray) -> bytearray:
    # Completar
    pass


if __name__ == "__main__":
    # Tortuga
    tama = Tortuga("Tama2")
    print("Nombre: ", tama.nombre)
    print("Edad: ", tama.edad)
    print(tama.celebrar_anivesario())
    print()

    # Encriptar
    original = serializar_tortuga(tama)
    print("Original: ", original)
    encriptado = encriptar(original, 6, 24)
    print("Encriptado: ", encriptado)
    print()

    # Desencriptar
    mensaje =  bytearray(b'\x00\x00\x13roT\x07\x8c\x94sesalc\x06\x8c\x00\x00\x00\x00\x00\x80\x04\x958\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12tuga\x94\x93\x94)\x81\x94}\x94(\x8c\x06nombre\x94\x8c\x05Tama2\x94\x8c\x04edad\x94K\x01ub.\x00\x00\x06\x00\x00\x18')
    desencriptado = desencriptar(mensaje)
    tama = deserializar_tortuga(desencriptado)

    # Tortuga
    print("Tortuga: ", tama)
    print("Nombre: ", tama.nombre)
    print("Edad: ", tama.edad)
