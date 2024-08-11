from wsgiref.simple_server import make_server
import threading
import random
import json


list_of_users = []
_id = 0


def application(environ, start_response):
    path = environ[ 'PATH_INFO']
    status = "200 OK"
    content_type = "application/json"

    response = {"message": "Éxito"}
    # GET
    if environ["REQUEST_METHOD"] == "GET":

        if path.startswith("/users"):
            response["users"] = list_of_users

        elif path.startswith("/group"):
            interes = path.removeprefix("/group/")
            users = list(filter(lambda user: interes in user["intereses"], list_of_users))
            # Get random subset of users
            if len(users) == 0:
                response["message"] = "No hay usuarios registrados con ese interés :("
                status = "404 Not Found"
            users = random.sample(users, min(3, len(users)))
            response["users"] = users

        elif path.startswith("/user/"):
            path = path.removeprefix("/user/")
            username = path
            found = False
            for user in list_of_users:
                if user["username"] == username:
                    response["user"] = user
                    found = True
                    break
            if not found:
                response["message"] = "Usuario no encontrado :("
                status = "404 Not Found"

    # POST
    elif environ["REQUEST_METHOD"] == "POST":
        if path.startswith("/register"):
            content_length = int(environ["CONTENT_LENGTH"])
            try:
                global _id
                body = environ["wsgi.input"].read(content_length)
                user = json.loads(body)
                user["id"] = _id
                _id += 1
                list_of_users.append(user)
                response["user"] = user
            except:
                status = "400 Bad Request"
                response["message"] = "Error al registrar usuario"
        elif path.startswith("/goodbye"):
            response["message"] = "Bai!"

    # PATCH
    elif environ["REQUEST_METHOD"] == "PATCH":
        if path.startswith("/user"):
            path = path.removeprefix("/user/")
            _id = int(path)
            found = False
            for u in list_of_users:
                print("u", u)
                if u["id"] == _id:
                    content_length = int(environ["CONTENT_LENGTH"])
                    body = environ["wsgi.input"].read(content_length)
                    user = json.loads(body)
                    print("user", user)
                    u["intereses"] = user["intereses"]
                    response["user"] = u
                    found = True
                    break
            if not found:
                response["message"] = "Usuario no encontrado :("
                status = "404 Not Found"

    # response headers
    response = json.dumps(response).encode()
    headers = [
        ("Content-Type", content_type),
        ("Content-Length", str(len(response)))
    ]

    start_response(status, headers)
    return [response]


if __name__ == "__main__":
    w_s = make_server(host="localhost", port=4444, app=application)
    print("Escuchando....")
    thread = threading.Thread(target=w_s.serve_forever, daemon=True)
    thread.start()
    input("Presiona [ENTER] para cerrar el servidor")
