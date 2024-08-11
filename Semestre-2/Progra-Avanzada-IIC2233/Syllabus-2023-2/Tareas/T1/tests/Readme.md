# Tests

Para correr cada archivo, desde la consola debes posicionarte en la carpeta de la `tests`, y luego escribir `python3 test_COMPLETAR.py`. Por ejemplo `python3 test_pieza_explosiva.py`. Si no funciona `python3`, probar con `py` o `python`.

El _pipeline_ que sigue cada archivo es el siguiente:
1. Se hace `sys.path.append("..")` para acceder a los archivos de la carpeta padre, es decir, a los archivos dentro de T1. Este comando es de uso exclusivo por el cuerpo docente. Su uso no está permitido en las evaluaciones.

2. Ejecutar los _tests_ para validar 1 método o _property_ en específico bajo diferentes casos.

3. Reportar, en consola, cuales _tests_ fueron exitosos, cuales no lo fueron, y cuales tuvieron algún error.


## Correr todos los tests

Para correr todos los _tests_, está el archivo `tests_todos.py` que se encarga de ejecutar todos los _tests_ contenido en la carpeta `tests`-
