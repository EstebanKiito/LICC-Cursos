def print_opciones_menu() -> None:
    opciones = '''
    Selecciona una de las siguientes opciones de usuarioBasket:
    a) Crear perfil de usuario
    b) Agregar items a la canasta
    c) Mostrar la canasta
    d) Realizar compra
    e) Salir
    '''
    print(opciones)


def print_usuario(usuario) -> None:
    if usuario.sub == True:
        print(f"> Usuario con suscripcion. Puntos: {usuario.puntos}")
    else:
        print(f"> Usuario sin suscripcion. Puntos: {usuario.puntos}")

def print_canasta(usuario) -> None:
    print("> Canasta actual del usuario:")
    for i in range(len(usuario.canasta)):
        print(f'\t{i+1}) {usuario.canasta[i].nombre}: ${usuario.canasta[i].precio} / {usuario.canasta[i].puntos} puntos')

def print_items(items) -> None:
    print("> Items para elegir:")
    for i in range(len(items)):
        print(f'{i+1}) {items[i].nombre}: ${items[i].precio} / {items[i].puntos} puntos')

def print_opcion_invalida() -> None:
    print("> La opción ingresada es inválida")

def print_salida() -> None:
    print("> Gracias por usar DCCompras")