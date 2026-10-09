# Clase 12 — Strings y slicing

Trabajamos los strings como secuencias de caracteres que se pueden "cortar".

- **Slicing**: extraer partes de un string con `s[inicio:fin]`, y el truco
  `s[::-1]` para invertirlo completo.
- **Múltiples soluciones para un mismo problema**: `funcion palindrome.py`
  muestra tres formas de verificar si un string es palíndromo —
  recorriendo con índices que avanzan desde los extremos, invirtiendo con
  slicing y comparando, o retornando directamente una expresión booleana.
  La idea es notar que no hay una sola forma "correcta", pero algunas son
  más elegantes y legibles que otras.
- **`len()`** para comparar largos y quedarse con el string más largo
  ingresado, usando patrón de sentinela de texto (`'fin'`/`'FIN'`) en
  `palabra mas larga.py`.

Ejemplos: `funcion palindrome.py`, `palabra mas larga.py`.
