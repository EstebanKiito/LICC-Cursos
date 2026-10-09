# Clase 16 — Introducción a listas

Primer contacto formal con listas como estructura de datos.

- **De contadores sueltos a listas**: `votos0.py` cuenta votos con variables
  separadas (`voto1`, `voto2`); `votos1.py` muestra que una **lista** puede
  reemplazar eso como un arreglo de contadores (`votos = [0]*cuantos`),
  accediendo e incrementando por índice (`votos[voto-1] += 1`).
- **`append()` y `count()`**: `votos2.py` usa una estrategia distinta,
  agregando cada voto a una lista dinámica con `append()` y luego contando
  ocurrencias con `count()` — útil para comparar dos formas válidas de
  resolver el mismo problema (arreglo fijo vs. lista dinámica).
- **Módulos de datos externos**: búsqueda de máximos/mínimos recorriendo
  datos definidos en otro módulo (`dccompletos A.py`).

Ejemplos: `votos0.py`, `votos1.py`, `votos2.py`.
