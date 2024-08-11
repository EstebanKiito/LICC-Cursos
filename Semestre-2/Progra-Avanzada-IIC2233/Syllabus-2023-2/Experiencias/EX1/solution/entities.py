class Item:
    # Item necesita un nombre, un precio y los puntos que se ganan cuando es comprado
    # El precio es un atributo "privado"
    def __init__(self, nombre: str, precio: int, puntos: int):
        self.nombre = nombre
        self.puntos = puntos
        self._precio = precio

    # Definimos el getter de una property para acceder al atributo privado "_precio"
    @property
    def precio(self):
        return self._precio

    # Definimos el setter para la property "precio", así podemos condicionar la edición
    @precio.setter
    def precio(self, nuevo_precio: int):
        # Solo podemos cambiar el precio si este es mayor a 500
        if nuevo_precio >= 500:
            self._precio = nuevo_precio


class Usuario:
    # Usuario necesita saber si tiene o no subscripción
    # Además, por defecto tiene una canasta vacía y 0 puntos adquiridos
    # Los puntos serán un atributo privado
    def __init__(self, esta_subscrito: bool):
        self.sub = esta_subscrito
        self.canasta = []
        self._puntos = 0

    # Definimos el getter de una property para acceder al atributo privado "_puntos"
    @property
    def puntos(self):
        return self._puntos

    # Definimos el setter para la property "puntos", aquí no condicionamos nada
    @puntos.setter
    def puntos(self, nuevos_puntos: int):
        self._puntos = nuevos_puntos

    # Definimos un método para agregar un Item a la canasta
    def agregar_item(self, item: Item):
        # Si el usuario está subscrito, el precio del item se reduce a un 90%
        if self.sub:
            item.precio *= 0.9
        # Luego, agregamos el item a la canasta
        self.canasta.append(item)

    # Definimos un método para comprar todos los Items de la canasta
    # y agregar los puntos ganados por la compras
    def comprar(self):
        # Por cada item, aumentamos la cantidad de puntos que tenemos
        for item in self.canasta:
            # Aquí hacemos una interacción entre una instancia Usuario con la instancia Item
            self.puntos += item.puntos
        # Limpiamos nuestra canasta
        self.canasta = []
