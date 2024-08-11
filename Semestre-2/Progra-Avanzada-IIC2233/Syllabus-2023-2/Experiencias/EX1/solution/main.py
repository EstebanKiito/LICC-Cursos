# Importamos cada función del archivo "pretty_print"
from utils.pretty_print import (
    print_opciones_menu,
    print_usuario,
    print_salida,
    print_canasta,
    print_items,
    print_opcion_invalida,
)

# Importamos la función de cargar_items
from utils.loader import cargar_items

# Importamos nuestra clase Usuario
from entities import Usuario


# Definimos una función para generar un menú
def menu():
    # Cargamos todos los items del archivo "items.dcc"
    items = cargar_items()

    # Imprimimos las opciones del menú
    print_opciones_menu()

    # Le pedimos un input al usuario de la consola para interactuar con el menú
    opcion = input("Indique su opcion: ")

    # Mientras la respuesta del usuario no sea "e",
    while opcion != "e":
        """
        # Este es el menú que se ve en pantalla
        Selecciona una de las siguientes opciones de DCCompra:
        a) Crear perfil de usuario
        b) Agregar items a la canasta
        c) Mostrar la canasta
        d) Realizar compra
        e) Salir
        """
        # a) Crear perfil de usuario
        if opcion == "a":
            # Preguntamos si el usuario tiene o no subscripción
            sub = input("Usuario con suscripción? [S/N]: ")
            if sub == "S":
                usuario = Usuario(True)
            elif sub == "N":
                usuario = Usuario(False)
            # Imprimimos la información del usuario recién creado
            print_usuario(usuario)

        # b) Agregar items a la canasta
        elif opcion == "b":
            # Imprimimos todos los items
            print_items(items)
            # Pedimos el número del item a comprar
            indice = int(input("> Agregar item a la compra: "))

            # Agregamos dicho item a la canasta de usuario
            usuario.agregar_item(items[indice - 1])

            # Eliminamos el item de la lista de todos los items posibles a comprar
            items.pop(indice - 1)

        # c) Mostrar la canasta
        elif opcion == "c":
            # Imprimir toda la canasta del usuario
            print_canasta(usuario)

        # d) Realizar compra
        elif opcion == "d":
            # Hacemos que nuestro usuario compre su canasta
            # y mostramos su información actualizada
            usuario.comprar()
            print_usuario(usuario)

        # Ninguna de las letras anteriores
        else:
            # Indicamos que la respuesta dada no es ninguna letra válida
            print_opcion_invalida()

        # Una vez procesada la respuesta, volvemos a imprimir las opciones del menú
        # y le pedimos nuevamente un input al usuario para interactuar con el menú
        print_opciones_menu()
        opcion = input("Indique su opcion: ")

    # Imprimimos un mensaje de despedida
    print_salida()


# El siguiente código solo se ejecuta cuando este archivo es ejecutado
# directamente en la consola "python3 main.py"
if __name__ == "__main__":
    menu()
