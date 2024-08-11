# Importamos las reglas del linter a usar
from reglas_linter.regla_espacio_coma import ReglaEspacioDespuesComa
from reglas_linter.regla_limite_caracteres_linea import (
    ReglaLimiteCaracteresLinea
)
from reglas_linter.regla_largo_archivo import ReglaLargoArchivo
from reglas_linter.regla_clases_mayuscula import ReglaClasesMayuscula

# Carpeta en donde irán los archivos a analizar
PATH_CODIGO = "codigo"

# Configuraciones para nuestras reglas a usar
LARGO_MAXIMO_ARCHIVO = 100
LARGO_MAXIMO_LINEA = 50

# Reglas a usar en el linter
REGLAS = [
    ReglaLargoArchivo(LARGO_MAXIMO_ARCHIVO),
    ReglaLimiteCaracteresLinea(LARGO_MAXIMO_LINEA),
    ReglaClasesMayuscula(),
    ReglaEspacioDespuesComa(),
]
