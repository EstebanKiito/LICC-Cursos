import os


# Teclas
TECLA_ARRIBA = "w"
TECLA_IZQUIERDA = "a"
TECLA_ABAJO = "s"
TECLA_DERECHA = "d"

# Topos
WIDTH_TOPO = 140
HEIGHT_TOPO = 120

TOPO_L_X = 110
TOPO_L_Y = 360

TOPO_R_X = 450
TOPO_R_Y = 360

TOPO_U_X = 280
TOPO_U_Y = 270

TOPO_D_X = 280
TOPO_D_Y = 450

POS_TOPO_HIDE = (700, 700)

# Martillo
WIDTH_MARTILLO = 100
HEIGHT_MARTILLO = 100
POS_INICIO_MARTILLO = (20, 230, WIDTH_MARTILLO, HEIGHT_MARTILLO)

MARTILLO_L_X = 80
MARTILLO_L_Y = 340

MARTILLO_R_X = 450
MARTILLO_R_Y = 340

MARTILLO_U_X = 260
MARTILLO_U_Y = 230

MARTILLO_D_X = 260
MARTILLO_D_Y = 450


# puntos
PUNTAJE_INICIAL = 0
PUNTAJE_HIT = 10
PUNTAJE_MISS = 5

# Duracion timers
TIEMPO_JUEGO = 60000
ACTUALIZAR_JUEGO = 100
RESET_MARTILLO = 250
TOPO_COOLDOWN = 2000
RANGO_APARICION_TOPO = (1000, 5000)
RANGO_AFUERA_TOPO = (750, 2000)

# Ventana de Inicio
PASSWORD = 'DCCode'
MAX_CARACTERES = 12

# Rutas
RUTA_LOGO = os.path.join('frontend', 'assets', 'logo.png')
RUTA_UI_VENTANA_JUEGO = os.path.join("frontend", "assets", "ventana_juego.ui")
RUTA_UI_VENTANA_POSTJUEGO = os.path.join("frontend", "assets",
                                         "ventana_postjuego.ui")
RUTA_TOPO = os.path.join('frontend', 'assets', 'topo.png')
RUTA_MARTILLO = os.path.join('frontend', 'assets', 'martillo.png')
