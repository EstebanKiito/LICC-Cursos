# Tests

Para correr cada archivo, desde copiar esta carpeta junto al código de la tarea. Luego, debes posiciona la terminal dentro de la carpeta `tests_privados` (se recomienda utilizar `cd`). Finalmente, escribir `python3 item_XX_COMPLETAR.py`, por ejemplo, `python3 item_01_test_pieza_explosiva_V_H.py`. Si no funciona `python3`, probar con `py` o `python`.

El _pipeline_ que sigue cada archivo es el siguiente:
1. Se hace `sys.path.append("..")` para acceder a los archivos de la carpeta padre, es decir, a los archivos dentro de T1. Este comando es de uso exclusivo por el cuerpo docente. Su uso no está permitido en las evaluaciones.

2. Ejecutar los _tests_ para validar 1 método o _property_ en específico bajo diferentes casos.

3. Reportar, en consola, cuales _tests_ fueron exitosos, cuales no lo fueron, y cuales tuvieron algún error.
