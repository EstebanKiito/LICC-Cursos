# Clase 06 — Condicionales anidados y `elif`

Esta clase es clave para entender por qué `elif` existe y cuándo conviene
usarlo.

- **`if` anidados**: clasificar un valor según rangos numéricos encadenando
  varios `if`/`else` dentro de otros. Las distintas versiones de
  `monitoreo.py` muestran cómo esto rápidamente se vuelve difícil de leer.
- **El problema de usar varios `if` sueltos** (`monitoreo4.py`): si las
  condiciones no son excluyentes, se pueden evaluar y ejecutar bloques que no
  correspondían, o quedar casos sin cubrir.
- **La solución: `elif`** (`monitoreo5.py`, `monitoreo6.py`): encadenar
  condiciones con `elif` para que solo se ejecute una rama, y por qué el
  **orden** de las condiciones importa (una condición muy amplia puesta
  primero puede "tapar" a las siguientes).
- Comparaciones encadenadas de rango, como `0 <= valor <= 99`.

Ejemplos: `chocolates.py`, `monitoreo.py` a `monitoreo6.py`.
