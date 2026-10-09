# Clase 20 — Recursión

Introducción a las funciones recursivas: funciones que se llaman a sí mismas.

- **Caso base y caso recursivo**: toda función recursiva necesita una
  condición de salida (caso base) para no llamarse infinitamente. En
  `funcion factorial.py` el caso base es `n == 0`, y se compara con la
  versión iterativa vista en la clase 11.
- **Recursión con dos llamadas**: `func fibonacci.py` calcula Fibonacci con
  dos casos base (`mes == 1` o `mes == 2`) y dos llamadas recursivas dentro
  de la misma función.
- **Recursión visual con `turtle`**: `tortuga.py` dibuja un árbol fractal
  usando `forward`, `left`, `right`, `back`, con dos llamadas recursivas
  (como un árbol binario) — ayuda a "ver" cómo se ramifica la recursión.

Ejemplos: `func fibonacci.py`, `funcion factorial.py`, `tortuga.py`.
