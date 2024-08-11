from wsgiref.simple_server import make_server, WSGIRequestHandler
import threading
import json
from urllib.parse import parse_qs
from datetime import date

# CONSTANTES
OK = "200 "
BAD = "400 "
NOT_FOUND = "404 "

# Endpoints
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
        # database es la base de datos que ocupará la API
        # mode es literal un "modo" de la API, así podemos decir que en mode=1 entregue una
        # respuesta. Y en mode=2 o mode=3 entregue otra respuesta, esto servirá para el
        # tema de tests.

        self.database = database
        self.host = host
        self.port = port
        self.mode = mode
        self.daemon = True

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

        # response headers
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
        self.w_s.serve_forever()

    def stop(self):
        self.w_s.server_close()

    ###########################################################################
    # Editar de aquí la función que verifica los "permisos".
    ###########################################################################
    def check_autorization(self, environ):
        # Verifica que manden un token, si lo manda, se verifica que sea
        # igual al valor esperado.
        if "HTTP_AUTHORIZATION" not in environ:
            return False
        token_alumno = environ["HTTP_AUTHORIZATION"]
        token_esperado = "pepaiic2233" if self.mode == 1 else "morenoiic2233"
        if token_alumno != token_esperado:
            return False

        return True

    ###########################################################################
    # Editar de aquí en adelante con los "endpoint" que la API va a tener
    ###########################################################################
    # params es diccionario con los parámetros que se mandaron junto a la URL.
    # Cada valor SIEMPRE será una lista, aunque sea de 1 elemento.

    # body es un diccionario con los datos que se mandaron en "data" al hacer
    # la request. Cada valor SIEMPRE será una lista, aunque sea de 1 elemento.

    @endpoint("/", "GET")
    def get_index(self, params, body, *args, **kwargs):
        today = str(date.today())
        if self.mode == 1:
            response = {
                "result": f"Hoy es {today} y es un hermoso día para recibir un horóscopo"
            }
        else:
            response = {"result": f"Hoy es {today} y me da gusto escribir horóscopos"}

        return response, OK

    @endpoint("/horoscopo", "GET")
    def get_horospoco(self, params, body, *args, **kwargs):
        response = {"result": ""}
        if "signo" not in params:
            response["result"] = "Falta información en la consulta"
            return response, BAD

        # Recordar que siempre el "valor" del diccionario será una lista
        # aunque sea de 1 elemento.

        signo = params["signo"][0]
        response["signo"] = signo
        if signo not in self.database:
            response["result"] = "El signo no existe"
            return response, BAD

        response["result"] = self.database[signo]
        return response, OK

    @endpoint("/aleatorio", "GET")
    def get_signo_aleatorio(self, params, body, *args, **kwargs):
        if self.mode == 3:
            return {"result": "ups, no pude"}, "500 "
        index = 0 if self.mode == 1 else -1
        signo = list(self.database.keys())[index]
        response = {"result": f"http://{self.host}:{self.port}/horoscopo?signo={signo}"}
        return response, OK

    @endpoint("/signos", "GET")
    def get_signos(self, params, body, *args, **kwargs):
        response = {"result": list(self.database.keys())}
        return response, OK

    @endpoint("/update", "POST")
    def update_signo_post(self, params, body, *args, **kwargs):
        response = {"result": ""}
        if "signo" not in body or "mensaje" not in body:
            response["result"] = "Falta información en la consulta"
            return response, BAD

        # Recardar que siempre el "valor" del diccionario será una lista
        # aunque sea de 1 elemento.
        mensaje = body["mensaje"][0]
        signo = body["signo"][0]

        if len(mensaje) < 5:
            response["result"] = "El mensaje debe tener más de 4 caracteres"
            return response, BAD

        if signo not in self.database:
            self.database[signo] = mensaje
            response["signos"] = list(self.database.keys())
            response["result"] = "Información agregada con éxito"
            return response, OK

        response["result"] = "El signo ya existe, no puedes modificarlo"
        return response, BAD

    @endpoint("/update", "PUT")
    def update_signo_put(self, params, body, *args, **kwargs):
        response = {"result": ""}

        if "signo" not in body or "mensaje" not in body:
            response["result"] = "Falta información en la consulta"
            return response, BAD

        # Recardar que siempre el "valor" del diccionario será una lista
        # aunque sea de 1 elemento.
        mensaje = body["mensaje"][0]
        signo = body["signo"][0]

        if len(mensaje) < 5:
            response["result"] = "El mensaje debe tener más de 4 caracteres"
            return response, BAD

        if signo not in self.database:
            response["result"] = "El signo no existe"
            return response, BAD

        self.database[signo] = mensaje
        response["result"] = "Información actualizada con éxito"
        return response, OK

    @endpoint("/remove", "DELETE")
    def remove_signo(self, params, body, *args, **kwargs):
        response = {"result": ""}

        if "signo" not in body:
            response["result"] = "Falta información en la consulta"
            return response, BAD

        # Recardar que siempre el "valor" del diccionario será una lista
        # aunque sea de 1 elemento.
        signo = body["signo"][0]

        if signo not in self.database:
            response["result"] = "El signo no existe"
            return response, BAD

        del self.database[signo]
        response["result"] = "Información eliminada con éxito"
        response["signos"] = list(self.database.keys())
        return response, OK


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 4444
    print("Escuchando... http://{}:{}/".format(HOST, PORT))
    DATABASE = {
        "acuario": "Hoy será un hermoso día",
        "leo": "No salgas de casa... te lo recomiendo",
    }
    thread = Server(HOST, PORT, DATABASE)
    thread.start()
    print("Endpoints")
    for endpoint in ENDPOINTS:
        method, rute = endpoint.split("|")
        print("[{}] http://{}:{}{}".format(method, HOST, PORT, rute))
    input("Presiona [ENTER] para cerrar el servidor\n")
