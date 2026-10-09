# Clase 09 — Módulos propios y simulaciones con estado

- **Módulos propios**: importar funciones definidas en otro archivo del
  mismo proyecto con `import amigos`, para reutilizar código entre archivos
  (`dccamaradas A.py`).
- **Simulación con estado que persiste entre iteraciones**: `pig.py` extiende
  el juego de dados de la clase anterior, acumulando el puntaje del turno
  actual (`puntos_este_turno`) y decidiendo un ganador al final.
- **Algoritmo del dígito verificador del RUT chileno** (`rut.py`): un buen
  ejercicio de módulo/división entera (`%10`, `//10`) para ir extrayendo
  dígitos uno a uno, con un acumulador que usa un multiplicador cíclico, y
  manejo de casos especiales como el dígito `K` y el `0`.

Ejemplos: `dccamaradas A.py`, `pig.py`, `rut.py`.
