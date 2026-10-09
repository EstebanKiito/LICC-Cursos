# Clase 15 — Simulaciones complejas con módulos externos

Clase de práctica integrando lo visto hasta ahora en problemas más grandes.

- **Simulación de juegos de mesa**: `dccolumnas.py` maneja varias variables
  de estado por jugador dentro de bucles `while` anidados y condicionales
  complejas, mostrando cómo crece la dificultad al simular reglas de juego
  reales.
- **Módulos externos de datos**: `pizzas A.py`/`pizzas B.py` usan un módulo
  `pizza` con funciones ya definidas (`ingrediente_principal`,
  `precio_ingrediente`) para buscar, por ejemplo, el día más barato
  recorriendo los días de la semana.
- **Strings como "mapas"**: en los ejercicios `wakanda` se representan
  mapas con caracteres (`'-'`, `'V'`), se calculan rachas máximas de
  caracteres repetidos y se usan funciones booleanas auxiliares junto con
  slicing (`trozo = m[i:i+k]`) para analizar ventanas del string.

Ejemplos: `dccolumnas.py`, `pizzas A.py`, `wakanda A.py`.
