def es_valido(texto: str) -> bool:
    for valor in texto.split(','):
        if not valor.isnumeric():
            return False
    return True


def ordenar(lista_de_numeros: list) -> list:
    lista_de_numeros.sort()
    return lista_de_numeros


def procesar_input(texto_input: str) -> str:
    texto_input = texto_input.replace(' ', '').strip(',')
    if not es_valido(texto_input):
        return 'Input no válido'
    lista_de_numeros = [int(porcion) for porcion in texto_input.split(',')]
    numeros_ordenados = ordenar(lista_de_numeros)
    texto_resultado = ", ".join([str(numero) for numero in numeros_ordenados])
    return texto_resultado
