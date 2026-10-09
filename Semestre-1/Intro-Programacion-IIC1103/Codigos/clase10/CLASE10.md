# Clase 10 — Hacia las funciones: motivación

Antes de definir funciones formalmente, vemos por qué las necesitamos.

- **Patrón sentinela para mínimo/máximo**: ir comparando cada nuevo valor
  ingresado contra el mejor encontrado hasta ahora, para quedarse con el
  menor tiempo de una carrera (`carrera1.py`) y luego también el mayor y la
  diferencia entre ambos (`carrera2.py`).
- **Conversión manual de formato de tiempo** ("hhmmss" a segundos), un
  cálculo que se repite varias veces en el código.
- **La motivación para usar funciones** (`carrera3.py`): al notar que el
  cálculo de segundos se repite, se extrae a una función `segundos(hora)`
  con `return`, dejando el programa principal más corto y claro — la idea
  central de **modularizar** código repetido.

Ejemplos: `carrera1.py`, `carrera2.py`, `carrera3.py`.
