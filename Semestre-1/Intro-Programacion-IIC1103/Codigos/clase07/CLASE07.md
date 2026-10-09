# Clase 07 — Bucles `while` y `for`

Clase larga y central: aquí aparecen los bucles, la herramienta que permite
repetir código.

- **`while`**: repetir un bloque mientras se cumpla una condición. Se ve el
  patrón clásico de contador (`n += 1`) y acumulador (`suma += valor`) para
  calcular cosas como promedios (`notas.py`).
- **Bucles infinitos**: `que pasa.py` es un ejemplo a propósito roto, donde
  la condición del `while` nunca cambia — útil para aprender a detectar y
  evitar este error común.
- **`for ... in range(...)`**: la alternativa a `while` cuando se sabe de
  antemano cuántas veces se quiere repetir (`notas2.py`).
- **Patrón de sentinela**: terminar un bucle de ingreso de datos cuando el
  usuario escribe un valor especial (por ejemplo `-1`), usando una bandera
  booleana o `break` (`notas terminando en 1.py` y su variante con `break`).
- **Bucles anidados y estado compartido**: `pig.py` simula un juego de dados
  con un `while` de turnos que contiene otro `while` de lanzamientos,
  acumulando puntaje entre iteraciones.
- **`and` / `or` combinados** entre varias variables para detectar alertas
  (`monitoreo.py`).
- Formato de salida con `\t`, `\n` y el parámetro `end=` de `print`.

Ejemplos: `escribir cuadrados.py`, `notas.py`, `notas2.py`, `pig.py`, `monitoreo.py`.
