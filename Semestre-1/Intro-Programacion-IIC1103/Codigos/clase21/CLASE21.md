# Clase 21 — Recursión sobre listas y matrices

- **Recursión sobre listas**: `definir largo de lista.py` calcula el largo
  de una lista de forma recursiva, usando slicing (`lista[1:]`) para
  "avanzar" y el caso base `lista == []`.
- **Matrices de adyacencia y cierre transitivo**: `vuelos ejercicio.py`
  representa rutas de vuelos como una lista de listas (matriz), con
  funciones para vuelos directos, vuelos con una escala, y finalmente una
  función recursiva `vuelos_con_escala` que repite el proceso hasta
  encontrar todas las rutas posibles (concepto de grafo simple), combinando
  recursión con estructuras matriciales.

Ejemplos: `definir largo de lista.py`, `vuelos ejercicio.py`.
