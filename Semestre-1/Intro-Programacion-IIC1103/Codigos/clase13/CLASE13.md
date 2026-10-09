# Clase 13 — Funciones sobre strings

Seguimos combinando funciones con procesamiento de texto.

- **Búsqueda de substrings "a mano"**: `definir buscar.py` implementa el
  equivalente de `find()` usando slicing (`x[i:i+len(y)]`) y retornando el
  índice encontrado o `-1` si no existe — el patrón clásico de búsqueda.
- **Contar ocurrencias de un carácter**: dos formas de recorrer un string,
  iterando directo sobre sus caracteres (`for letra in x`) o por índice
  (`definir contar.py`), comparando ambos estilos.
- **Funciones con varios parámetros** para ordenar tres strings
  alfabéticamente sin usar `sort()`, encadenando varios `elif`
  (`funcion ordenar.py`).
- **Módulos de datos externos**: `from diccionario import *` para usar datos
  definidos en otro archivo, y un patrón de "generar y validar" probando
  reemplazos de vocales en una palabra (`problema corregir.py`).

Ejemplos: `definir buscar.py`, `definir contar.py`, `funcion ordenar.py`.
