# Clase 18 — Mutabilidad de listas y paso de parámetros

Una de las clases más importantes del curso: entender qué significa que las
listas sean **mutables**.

- **`demos3.py`**: reasignar un entero dentro de una función **no** afecta
  la variable original fuera de ella — los tipos simples (`int`, `float`,
  `str`) son inmutables y se pasan "por valor".
- **`demos4.py`**: hacer `append()` sobre una lista recibida como parámetro
  **sí** modifica la lista original afuera de la función — las listas son
  mutables y se pasan "por referencia".
- **`demos5.py`**: en cambio, reasignar la lista completa dentro de la
  función (`M = [1, 23]`) **no** afecta la lista original — contraste clave
  entre modificar el contenido de una lista y reemplazarla por otra.
- **`insert()`** para agregar un elemento en una posición específica,
  manteniendo una lista ordenada (`demos.py`/`demos2.py`).
- **Eliminar duplicados de una lista**: por qué modificar una lista mientras
  se recorre puede producir bugs, y cómo evitarlo usando una lista auxiliar
  (`funcion eliminar duplicados BUENA.py`).
- **Listas de listas** como estructura básica para modelar datos
  jerárquicos, por ejemplo un árbol genealógico (`simpsons.py`).

Ejemplos: `demos3.py`, `demos4.py`, `demos5.py`, `funcion eliminar duplicados BUENA.py`.
