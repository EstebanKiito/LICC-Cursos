import ast
import os


ARCHIVOS_OMITIDOS = [
    ('.', 'archivo_con_for.py'),
    ('.', 'peli.py'),
    ('.', 'utilidades.py'),
    ('.', 'api.py'),
    ('.', 'test_publicos', 'test_00_peliculas_genero.py'),
    ('.', 'test_publicos', 'test_01_personas_mayores.py'),
    ('.', 'test_publicos', 'test_02_funciones_fecha.py'),
    ('.', 'test_publicos', 'test_03_titulo_mas_largo.py'),
    ('.', 'test_publicos', 'test_04_normalizar_fechas.py'),
    ('.', 'test_publicos', 'test_05_personas_reservas.py'),
    ('.', 'test_publicos', 'test_06_peliculas_en_base_al_rating.py'),
    ('.', 'test_publicos', 'test_07_mejores_peliculas.py'),
    ('.', 'test_publicos', 'test_08_pelicula_genero_mayor_rating.py'),
    ('.', 'test_publicos', 'test_09_fechas_funciones_pelicula.py'),
    ('.', 'test_publicos', 'test_10_genero_mas_transmitido.py'),
    ('.', 'test_publicos', 'test_11_id_funciones_genero.py'),
    ('.', 'test_publicos', 'test_12_butacas_por_funcion.py'),
    ('.', 'test_publicos', 'test_13_salas_de_pelicula.py'),
    ('.', 'test_publicos', 'test_14_nombres_butacas_altas.py'),
    ('.', 'test_publicos', 'test_17_edad_promedio.py'),
    ('.', 'test_publicos', 'test_15_nombres_persona_genero_mayores.py'),
    ('.', 'test_publicos', 'test_16_genero_comun.py'),
    ('.', 'test_publicos', 'test_18_obtener_horarios_disponibles.py'),
    ('.', 'test_publicos', 'test_19_personas_no_asisten.py'),
    ('.', 'test_publicos', 'test_20_saludar.py'),
    ('.', 'test_publicos', 'test_21_verificar_informacion.py'),
    ('.', 'test_publicos', 'test_22_dar_informacion.py'),
    ('.', 'test_publicos', 'test_23_dar_informacion_aleatoria.py'),
    ('.', 'test_publicos', 'test_24_agregar_informacion.py'),
    ('.', 'test_publicos', 'test_25_actualizar_informacion.py'),
    ('.', 'test_publicos', 'test_26_eliminar_pelicula.py'),
    ('.', 'test_publicos', 'test_elementos_prohibidos.py'),
]


class ComandoProhibidoError(BaseException):
    def __init__(self, comando: str, archivo: str, linea: int, *args: object) -> None:
        mensaje = f'Se ha hecho uso de "{comando}", en: "{archivo}", line {linea}.' \
            ' Como se indica en el enunciado, el uso de este comando implica nota mínima en la tarea.'
        super().__init__(mensaje, *args[2:])


def obtener_archivos_python(omitidos: list) -> list:
    archivos_omitidos = {os.path.join(*path) for path in omitidos}
    archivos_python = set()

    for path, _, archivos in os.walk('.'):
        for archivo in archivos:
            if archivo.endswith('.py'):
                archivos_python.add(os.path.join(path, archivo))

    return archivos_python - archivos_omitidos


def revisar_comandos_prohibidos(archivo: str) -> None:
    with open(archivo) as file:
        codigo = ast.parse(file.read())

    for nodo in ast.walk(codigo):
        if isinstance(nodo, (ast.While, ast.For, ast.List, ast.Dict, ast.Tuple, ast.Set)):
            comando = type(nodo).__name__.lower()
            linea = nodo.lineno
            raise ComandoProhibidoError(comando, archivo, linea)

        if isinstance(nodo, ast.Name):
            if nodo.id in ('list', 'dict', 'set', 'tuple'):
                linea = nodo.lineno
                raise ComandoProhibidoError(nodo.id, archivo, linea)

        if isinstance(nodo, ast.Assign):
            if isinstance(nodo.value, (ast.List, ast.Dict, ast.Tuple, ast.Set)):
                comando = type(nodo.value).__name__.lower()
                linea = nodo.lineno
                raise ComandoProhibidoError(comando, archivo, linea)


def revisar_comandos_prohibidos_todo_archivos(omitidos: list = ARCHIVOS_OMITIDOS) -> None:
    for archivo in obtener_archivos_python(omitidos):
        revisar_comandos_prohibidos(archivo)
