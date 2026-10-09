# Clase 24 — Manejo de archivos

Primera clase de lectura y escritura de archivos de texto.

- **Lectura**: `open()` y `readlines()` para leer todas las líneas de un
  archivo, por ejemplo para contarlas (`contador.py`) o elegir una al azar
  con `random.randint` (`palabra azar.py`, usando además `encoding='latin-1'`
  para caracteres especiales). Siempre cerrar el archivo con `close()`.
- **Escritura**: modo `'w'` para escribir (sobrescribiendo el archivo) usando
  `print(..., file=archivo)`; `programamalo.py` es un ejemplo a propósito
  "malo" por no verificar nada antes de sobrescribir.
- **Modo `'a'` (append)**: agregar contenido al final de un archivo sin
  borrar lo anterior, usado en `traductor.py` dentro de un bucle con
  sentinela ('fin') para ir guardando pares palabra/traducción con un
  formato delimitado.

Ejemplos: `contador.py`, `palabra azar.py`, `traductor.py`.
