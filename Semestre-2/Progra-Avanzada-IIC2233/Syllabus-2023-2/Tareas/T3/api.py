from wsgiref.simple_server import make_server, WSGIRequestHandler
import threading
import json
from urllib.parse import parse_qs
from datetime import date

OK = "200 "
BAD = "400 "
NOT_FOUND = "404 "

ENDPOINTS = {}

def endpoint(rute, method):
    def decorator(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        ENDPOINTS[f"{method}|{rute}"] = wrapper
        return wrapper

    return decorator


class NoLoggingWSGIRequestHandler(WSGIRequestHandler):
    def log_message(self, format, *args):
        pass

class Server(threading.Thread):
    def __init__(self, host, port, database, mode=1) -> None:
        super().__init__()

        self.database = database
        self.host = host
        self.port = port
        self.mode = mode
        self.daemon = True
        self.server_started = threading.Event()

    def _run_endpoint(self, params, body, path, method):
        key = f"{method}|{path}"

        if key in ENDPOINTS:
            method_f = ENDPOINTS[key]
            return method_f(self, params=params, body=body)
        response = {"result": "Endpoint no existe"}
        return response, NOT_FOUND

    def _application(self, environ, start_response):
        path = environ["PATH_INFO"]
        method = environ["REQUEST_METHOD"]
        try:
            request_body_size = int(environ.get("CONTENT_LENGTH", 0))
        except ValueError:
            request_body_size = 0

        request_body = environ["wsgi.input"].read(request_body_size)
        body = parse_qs(request_body.decode("utf-8"), encoding="utf-8")
        params = parse_qs(environ["QUERY_STRING"])
        new_body, new_params = {}, {}
        for key in body:
            new_body[key.lower()] = body[key]

        for key in params:
            new_params[key.lower()] = params[key]

        if method != "GET" and not self.check_autorization(environ):
            response = {"result": "No tienes autorización"}
            status = "401 "
        else:
            response, status = self._run_endpoint(new_params, new_body, path, method)
        content_type = "application/json"

        response = json.dumps(response).encode()
        headers = [
            ("Content-Type", content_type),
            ("Content-Length", str(len(response))),
        ]

        start_response(status, headers)
        return [response]

    def run(self):
        self.w_s = make_server(
            host=self.host,
            port=self.port,
            app=self._application,
            handler_class=NoLoggingWSGIRequestHandler,
        )
        self.server_started.set()
        self.w_s.serve_forever()

    def stop(self):
        self.w_s.server_close()

    def check_autorization(self, environ):
        if "HTTP_AUTHORIZATION" not in environ:
            return False
        token_alumno = environ["HTTP_AUTHORIZATION"]
        token_esperado = "tereiic2233" if self.mode == 1 else "juampiiic2233"
        if token_alumno != token_esperado:
            return False

        return True

    @endpoint("/", "GET")
    def get_index(self, params, body, *args, **kwargs):
        today = str(date.today())
        if self.mode == 1:
            response = {
                "result": f"Hoy es {today} y es un gran día para ver una buena película"
            }
        else:
            response = {"result": f"Hoy es {today} y tengo ganas de ver una película"}

        return response, OK

    @endpoint("/informacion", "GET")
    def get_informacion(self, params, body, *args, **kwargs):
        response = {"result": ""}
        if "pelicula" not in params:
            response["result"] = "Falta información en la consulta"
            return response, BAD

        pelicula = params["pelicula"][0]
        response["pelicula"] = pelicula
        if pelicula not in self.database:
            response["result"] = "La pelicula no existe"
            return response, BAD

        response["result"] = self.database[pelicula]
        return response, OK

    @endpoint("/aleatorio", "GET")
    def get_pelicula_aleatorio(self, params, body, *args, **kwargs):
        if self.mode == 3:
            return {"result": "ups, no pude"}, "500 "
        index = 0 if self.mode == 1 else -1
        pelicula = list(self.database.keys())[index]
        response = {"result": f"http://{self.host}:{self.port}/informacion?pelicula={pelicula}"}
        return response, OK

    @endpoint("/peliculas", "GET")
    def get_peliculas(self, params, body, *args, **kwargs):
        response = {"result": list(self.database.keys())}
        return response, OK

    @endpoint("/update", "POST")
    def actualizar_pelicula_post(self, params, body, *args, **kwargs):
        response = {"result": ""}
        if "pelicula" not in body or "sinopsis" not in body:
            response["result"] = "Falta información en la consulta"
            return response, BAD

        sinopsis = body["sinopsis"][0]
        pelicula = body["pelicula"][0]

        if len(sinopsis) < 5:
            response["result"] = "La sinopsis debe tener más de 4 caracteres"
            return response, BAD

        if pelicula not in self.database:
            self.database[pelicula] = sinopsis
            response["peliculas"] = list(self.database.keys())
            response["result"] = "Información agregada con éxito"
            return response, OK

        response["result"] = "La pelicula ya existe, no puedes modificarlo"
        return response, BAD

    @endpoint("/update", "PATCH")
    def actualizar_pelicula_put(self, params, body, *args, **kwargs):
        response = {"result": ""}

        if "pelicula" not in body or "sinopsis" not in body:
            response["result"] = "Falta información en la consulta"
            return response, BAD

        sinopsis = body["sinopsis"][0]
        pelicula = body["pelicula"][0]

        if len(sinopsis) < 5:
            response["result"] = "La sinopsis debe tener más de 4 caracteres"
            return response, BAD

        if pelicula not in self.database:
            response["result"] = "La película no existe"
            return response, NOT_FOUND

        self.database[pelicula] = sinopsis
        response["result"] = "Información actualizada con éxito"
        return response, OK

    @endpoint("/remove", "DELETE")
    def remove_pelicula(self, params, body, *args, **kwargs):
        response = {"result": ""}

        if "pelicula" not in body:
            response["result"] = "Falta información en la consulta"
            return response, BAD

        pelicula = body["pelicula"][0]

        if pelicula not in self.database:
            response["result"] = "La pelicula no existe"
            return response, NOT_FOUND

        del self.database[pelicula]
        response["result"] = "Información eliminada con éxito"
        response["peliculas"] = list(self.database.keys())
        return response, OK


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 4444
    print("Escuchando.... http://{}:{}/".format(HOST, PORT))
    DATABASE = {
        "Mamma Mia": "Comedia musical con ABBA",
        "Monsters Inc": "Monstruos asustan, niños y risas",
        "Incredibles": "Familia de superhéroes salva el mundo",
        "Avengers": "Superhéroes luchan contra villanos poderosos",
        "Titanic": "Amor trágico en el hundimiento del Titanic",
        "Akira": "Ciencia ficción japonesa con poderes psíquicos",
        "High School Musical": "Drama musical adolescente en la escuela East High",
        "The Princess Diaries": "Joven descubre que es princesa de Genovia",
        "Iron Man": "Hombre construye traje de alta tecnología para salvar al mundo",
        "Tarzan": "Hombre criado por simios en la jungla",
        "The Pianist": "Músico judío sobrevive en Varsovia durante el Holocausto",
    }
    thread = Server(HOST, PORT, DATABASE)
    thread.start()
    print("Endpoints")
    for endpoint in ENDPOINTS:
        method, rute = endpoint.split("|")
        print("[{}] http://{}:{}{}".format(method, HOST, PORT, rute))
    input("Presiona [ENTER] para cerrar el servidor\n")
