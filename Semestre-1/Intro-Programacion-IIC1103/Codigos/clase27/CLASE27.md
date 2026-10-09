# Clase 27 — POO con varias clases y composición

Se extiende POO a un ejemplo con dos clases que se relacionan entre sí.

- **Clase `Carta`**: con métodos propios como `diferencia` (comparar dos
  cartas), `cambiar_pinta`, y un `__str__` con lógica especial para mostrar
  correctamente J, Q, K y A.
- **Composición**: la clase `Mazo` **contiene** una lista de objetos
  `Carta` como atributo — un objeto construido a partir de otros objetos,
  en vez de heredar de ellos.
- **Métodos que operan sobre la colección interna**: `quedan_cartas()` para
  saber cuántas cartas quedan, y `sacar()` para extraer una carta al azar
  del mazo usando `pop()` — un ejemplo clásico de cómo modelar un mazo de
  cartas con POO.

Ejemplo: `cartas.py`.
