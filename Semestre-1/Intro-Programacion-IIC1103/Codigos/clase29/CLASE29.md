# Clase 29 — Algoritmos de ordenamiento: Selection Sort

Primer algoritmo de ordenamiento programado explícitamente (no usando el
`sort()` de Python).

- **`ordenar1`**: una versión "fácil" usando las funciones built-in de
  Python, `min()` y `.index()`, para encontrar el menor elemento restante en
  cada pasada.
- **`ordenar`**: la implementación "a mano" del algoritmo Selection Sort,
  con bucles anidados que recorren la lista buscando el mínimo de la parte
  no ordenada e intercambiando posiciones con
  `lista[ip], lista[m] = lista[m], lista[ip]`.
- El objetivo es entender **cómo funciona** un algoritmo de ordenamiento por
  dentro, en vez de solo usar `sort()`.

Ejemplo: `selection sort.py`.
