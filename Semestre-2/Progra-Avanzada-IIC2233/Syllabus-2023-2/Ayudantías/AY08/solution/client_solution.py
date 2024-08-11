import requests


base_url = 'http://localhost:4444'

'''
Implementar menú de opciones:
'''

while True:
    print("\n")
    print("1. Obtener todos los usuarios")
    print("2. Registrar un usuario")
    print("3. Obtener un grupo aleatorio por interés")
    print("4. Actualizar intereses de un usuario")
    print("5. Registrar usuarios de users.csv")
    print("6. Salir")
    opcion = input("Opción: ")
    print("\n")

    # Obtener todos los usuarios
    if opcion == "1":
        # COMPLETAR
        response = requests.get(base_url + '/users')
        print(response.json()["message"])
        for user in response.json()["users"]:
            print(user)

    # Registrar un usuario
    elif opcion == "2":
        # COMPLETAR

        # Este manejo de errores es opcional
        nombre = input("Nombre: ")
        username = input("Username: ")
        while True:
            try:
                edad = int(input("Edad: "))
                break
            except ValueError:
                print("Edad inválida")
        while True:
            try:
                intereses = input("Intereses (sepáralos por comas): ")
                intereses = intereses.split(",")
                break
            except ValueError:
                print("Intereses inválidos")
        dato_freak = input("Dato freak: ")

        # Lo importante es esto
        response = requests.post(
            base_url + '/register',
            json={
                "nombre": nombre,
                "username": username,
                "edad": edad,
                "intereses": intereses,
                "dato_freak": dato_freak
            }
        )
        print(response.json()["message"])
        if response.status_code == 200:
            print(response.json()["user"])

    # Obtener un grupo aleatorio por interés
    elif opcion == "3":
        # COMPLETAR
        interes = input("Interes: ")
        response = requests.get(base_url + '/group/' + interes)
        print(response.json()["message"])
        if response.status_code == 200:
            print(response.json()["users"])
        else:
            print(response.status_code)

    # Actualizar intereses de un usuario
    elif opcion == "4":
        # COMPLETAR
        # Una consulta para obtener el id del usuario en base a su username
        username = input("username: ")
        response = requests.get(base_url + '/user/' + username)
        print(response.json()["message"])
        if response.status_code == 200:
            # Y luego otra para actualizar los intereses con el id
            _id = response.json()["user"]["id"]
            intereses = input("Intereses: ")
            new_response = requests.patch(
                base_url + '/user/' + str(_id),
                json={
                    "intereses": intereses.split(",")
                }
            )
            print(new_response.json()["message"])
            if new_response.status_code == 200:
                print(new_response.json()["user"])
            else:
                print(new_response.status_code)
        else:
            print(response.status_code)

    # Registrar usuarios de users.csv
    elif opcion == "5":
        # COMPLETAR
        # Básicamente lo mismo que en la opción 2, pero leyendo de un archivo
        # y haciendo un request por cada usuario
        with open("users.csv", "r") as f:
            lines = f.readlines()[1:]
            for line in lines:
                nombre, username, edad, intereses, dato = line.strip().split(",")
                response = requests.post(
                    base_url + '/register',
                    json={
                        "nombre": nombre,
                        "username": username,
                        "edad": int(edad),
                        "intereses": intereses.split(";"),
                        "dato": dato
                    }
                )
                print(response.json()["message"])
    elif opcion == "6":
        break
    else:
        print("Opción inválida")
