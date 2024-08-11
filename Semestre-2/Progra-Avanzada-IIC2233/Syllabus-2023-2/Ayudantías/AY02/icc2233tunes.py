
import random

### COMPLETAR: Define una Canción con la estructura adecuada


class Playlist:

    def __init__(self, canciones):
        self.canciones = canciones
        self.cola = None

    def mostrar_canciones(self):
        ### COMPLETAR
        pass

    def existen_canciones(self):
        return len(self.canciones)

    def siguiente_cancion(self):
        ### COMPLETAR
        pass

    def reproducir_por_nombre(self, cancion):
        ### COMPLETAR
        pass

    def reproducir_al_azar(self):
        ### COMPLETAR
        pass

    def agregar_cancion(self, cancion):
        ### COMPLETAR
        pass

    def eliminar_cancion(self, cancion):
        ### COMPLETAR
        pass


class IIC2233Tunes:

    def __init__(self):
        # Debe ser None si no suena nada, y ser reemplazada con la cancion actual
        self.cancion_actual = None

        # Debe ser None si no suena nada, y ser reemplazada al elegir
        # una playlist para reproducir por la playlist correspondiente
        self.playlist_actual = None

        # Un diccionario donde se guardan las playlists por sus nombres.
        self.playlists = {}

    def fusionar_playlists(self, p1, p2):

        ### COMPLETAR

        # Debes crear una nueva playlist con las canciones de p1 y p2.
        # Recuerda que las canciones solo deben aparecer una sola vez,
        # y no importa el órden de su aparición.

        print("\n")
        print("-" * 40)
        nombre_playlist = input("Introduce el nombre de la playlist: ")

    def siguiente_cancion(self):

        ### COMPLETAR

        # Si existe una playlist actual, intentar pasar a la siguiente canción
        if self.playlist_actual is not None:
            # Además, debe asignar la canción a self.cancion_actual

            # En caso de que la playlist haya acabado, recuerda reiniciar
            # cancion_actual y playlist_actual
            pass
        else:
            print("-" * 40)
            print("No hay canciones a la cola")
            print("-" * 40 + "\n")

    def menu_ver_playlists(self):

        ### COMPLETAR

        print("\n")
        print("¿Qué quieres hacer?")
        print("-" * 40)

        # Estos son los menús a abrir.
        # Cada uno se abre llamando al 
        # método correspondiente
        print("1. Reproducir playlist")     # Usar self.menu_reproducir_playlist
        print("2. Agregar playlist")        # Usar self.menu_agregar_playlist
        print("3. Editar playlist")         # Usar self.menu_editar_playlist
        print("4. Fusionar playlists")      # Usar self.menu_fusionar_playlist

        print("-" * 40 + "\n")

        # El input es recibido como un int
        opc = int(input("Elige una opción por su número: "))

    def reproducir_por_nombre(self, playlist):
        cancion = input("Introduce la canción (<canción>-<artista>): ")

        ### COMPLETAR

        # Debes ejecutar el método correspondiente de la clase playlist
        # dada la información de la canción recibida

        # Además, debes iniciar la iteración de la playlist :O

    def reproducir_al_azar(self, playlist):

        ### COMPLETAR

        # Debes ejecutar el método correspondiente de la clase playlist

        # También, debes iniciar la iteración de la playlist
        pass

    # NO MODIFICAR DE AQUÍ HACIA ABAJO
    # El resto son más menús y funciones auxiliares

    def elegir_playlists(self):
        nombres_playlists = list(self.playlists.keys())
        print("\n")
        for pl in nombres_playlists:
            print(f" - {pl}")
        print("-" * 40 + "\n")
        opc = input("Elige una playlist por su nombre: ")
        return opc

    def ejecutar(self):
        self.menu_principal()

    def menu_principal(self):

        menu_principal = {
            1: self.siguiente_cancion,
            2: self.menu_ver_playlists,
            3: self.salir
        }
        while True:
            print("\n")
            if self.cancion_actual is not None:
                print(f"Estas escuchando: {self.cancion_actual.nombre}" +
                      f" - {self.cancion_actual.artista}")
            else:
                print("Estas escuchando: -")
            print("\n")
            print("¿Qué quieres hacer?")
            print("-" * 40)
            print("1. Siguiente canción")
            print("2. Mis playlists")
            print("3. Salir")
            print("-" * 40 + "\n")

            opc = int(input("Elige una opción por su número: "))
            if opc == 3:
                break
            else:
                menu_principal[opc]()

    def menu_reproducir_playlist(self):

        playlist = self.playlists[self.elegir_playlists()]
        self.playlist_actual = playlist
        if playlist.existen_canciones():
            playlist.mostrar_canciones()
            opciones_reproducir_playlist = {
                1: self.reproducir_por_nombre,
                2: self.reproducir_al_azar
            }

            print("\n")
            print("¿Qué quieres hacer?")
            print("-" * 40)
            print("1. Reproducir por nombre de canción")
            print("2. Reproducir al azar")
            print("-" * 40 + "\n")
            opc = int(input("Elige una opción por su número: "))
            return opciones_reproducir_playlist[opc](playlist)
        else:
            print("-" * 40)
            print("La playlist está vacía")
            print("-" * 40 + "\n")

    def menu_agregar_playlist(self):
        canciones = set()
        continuar = True
        print("\n")
        print("-" * 40)
        while continuar:
            print("(deja vacío para continuar)")
            cancion = input("Introduce la canción (<canción>-<artista>): ")
            if cancion == "":
                continuar = False
            else:
                nombre, artista = cancion.split("-")
                canciones.add(Cancion(nombre, artista))

        print("\n")
        print("-" * 40)
        nombre_playlist = input("Introduce el nombre de la playlist: ")
        nueva_playlist = Playlist(list(canciones))
        self.playlists[nombre_playlist] = nueva_playlist

    def menu_editar_playlist(self):
        if len(self.playlists):
            playlist = self.playlists[self.elegir_playlists()]
            playlist.mostrar_canciones()
            opciones_reproducir_playlist = {
                1: self.menu_agregar_cancion,
                2: self.menu_eliminar_cancion
            }
            print("\n")
            print("¿Qué quieres hacer?")
            print("-" * 40)
            print("1. Agregar canción")
            print("2. Eliminar canción")
            print("-" * 40 + "\n")
            opc = int(input("Elige una opción por su número: "))
            return opciones_reproducir_playlist[opc](playlist)
        else:
            print("-" * 40)
            print("No hay playlists aún")
            print("-" * 40 + "\n")
            return

    def menu_agregar_cancion(self, playlist):
        cancion = input("Introduce la canción (<canción>-<artista>): ")
        cancion = Cancion(*cancion.split("-"))
        self.agregar_cancion(playlist, cancion)

    def menu_eliminar_cancion(self, playlist):
        cancion = input("Introduce la canción (<canción>-<artista>): ")
        cancion = Cancion(*cancion.split("-"))
        self.eliminar_cancion(playlist, cancion)

    def agregar_cancion(self, playlist, cancion):
        playlist.agregar_cancion(cancion)

    def eliminar_cancion(self, playlist, cancion):
        playlist.eliminar_cancion(cancion)

    def menu_fusionar_playlists(self):
        if len(self.playlists) > 1:
            print("\n")
            print("-" * 40)
            print("Playlist 1")
            playlist1 = self.playlists[self.elegir_playlists()]
            print("Playlist 2")
            playlist2 = self.playlists[self.elegir_playlists()]
            self.fusionar_playlists(playlist1, playlist2)
        else:
            print("-" * 40)
            print("No tienes suficientes playlists aún")
            print("-" * 40 + "\n")
            return


# Flujo del programa
canciones = IIC2233Tunes()
canciones.ejecutar()
