# Clase 28 — Ordenar con `sort(key=...)` y `__repr__`

- **`list.sort(key=criterio, reverse=True)`**: ordenar una lista según un
  criterio propio, definido como una función aparte, en vez de depender del
  orden natural de los elementos (`ordenar.py` muestra el patrón con
  strings, listas numéricas por suma, y listas de strings por un índice
  específico).
- **`__repr__` vs `__str__`**: `clase Gato.py` muestra la diferencia entre
  ambos métodos especiales al imprimir un objeto solo vs. dentro de una
  lista de objetos.
- **Criterios de orden múltiples con tuplas**: ordenar objetos `Gato` primero
  por edad (descendente) y luego por nombre, usando una tupla como `key`.
- **Conteo de frecuencias en archivos**: `catalan.py` cuenta palabras
  repetidas en un archivo de texto y las ordena por frecuencia.

Ejemplos: `clase Gato.py`, `ordenar.py`, `catalan.py`.
