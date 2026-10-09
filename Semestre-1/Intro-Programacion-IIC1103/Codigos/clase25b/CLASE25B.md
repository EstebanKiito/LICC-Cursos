# Clase 25b — Procesamiento de archivos de texto y CSV

Aplicamos el manejo de archivos a datos más realistas, tipo tabla o CSV.

- **`split()` y `strip()`**: separar cada línea de un archivo en sus campos,
  quitando saltos de línea y espacios sobrantes — la base para procesar
  cualquier archivo de texto estructurado.
- **Cruzar datos de varios archivos**: `catalan 12.py` lee un diccionario
  catalán-castellano separando con `split('-')` y escribe el resultado
  cruzado en un tercer archivo.
- **Búsqueda por campo**: `dccarcadeA.py` separa campos de un registro y
  busca una coincidencia por nombre.
- **Procesamiento tipo CSV**: `procesar datos excel.py` usa `;` como
  delimitador, convierte columnas de texto a `float`, acumula puntajes y
  filtra filas según una condición, escribiendo el resultado final a otro
  archivo — un ejemplo cercano a cómo se procesan datos tabulares reales.

Ejemplos: `catalan 12.py`, `dccarcadeA.py`, `procesar datos excel.py`.
