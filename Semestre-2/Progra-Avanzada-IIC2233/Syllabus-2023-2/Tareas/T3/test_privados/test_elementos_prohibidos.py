import ast
import os


ARCHIVOS_OMITIDOS = [
    ('..', 'peli.py'),
    ('..', 'utilidades.py'),
    ('..', 'api.py'),
]

CARPETA_TEST_OMITIDA = ["../test_publicos", "../test_privados"]


class ComandoProhibidoError(BaseException):
    def __init__(self, comando: str, archivo: str, linea: int, *args: object) -> None:
        mensaje = f"Utiliza '{comando}' ('{archivo}' - {linea})"
        super().__init__(mensaje, *args[2:])


def obtener_archivos_python(omitidos: list) -> list:
    archivos_omitidos = {os.path.join(*path) for path in omitidos}
    archivos_python = set()

    for path, _, archivos in os.walk('..'):
        if path in CARPETA_TEST_OMITIDA:
            continue

        for archivo in archivos:
            if archivo.endswith('.py'):
                archivos_python.add(os.path.join(path, archivo))

    return archivos_python - archivos_omitidos


def revisar_comandos_prohibidos(archivo: str) -> None:
    try:
        with open(archivo) as file:
            codigo = ast.parse(file.read())
    except UnicodeDecodeError:
        with open(archivo, encoding="utf-8") as file:
            codigo = ast.parse(file.read())
    except SyntaxError as e:
        texto = 'El código presenta errores de sintáxis (SyntaxError), no es posible ejecutarlo ' \
                f'ni revisar su contenido: ({file} - line {e.lineno}) {e.text}'
        print(texto)
        return

    faltas = set()
    for nodo in ast.walk(codigo):
        if isinstance(nodo, (ast.While, ast.For, ast.List, ast.Dict, ast.Tuple, ast.Set)):
            comando = type(nodo).__name__.lower()
            linea = nodo.lineno
            faltas.add(str(ComandoProhibidoError(comando, archivo, linea)))

        if isinstance(nodo, ast.Name):
            if nodo.id in ('list', 'dict', 'set', 'tuple'):
                linea = nodo.lineno
                faltas.add(str(ComandoProhibidoError(nodo.id, archivo, linea)))

        if isinstance(nodo, ast.Assign):
            if isinstance(nodo.value, (ast.List, ast.Dict, ast.Tuple, ast.Set)):
                comando = type(nodo.value).__name__.lower()
                linea = nodo.lineno
                faltas.add(str(ComandoProhibidoError(comando, archivo, linea)))
    for falta in faltas:
        print(falta)


def revisar_comandos_prohibidos_todo_archivos(omitidos: list = ARCHIVOS_OMITIDOS) -> None:
    for archivo in obtener_archivos_python(omitidos):
        revisar_comandos_prohibidos(archivo)


if __name__ == "__main__":
    revisar_comandos_prohibidos_todo_archivos()
