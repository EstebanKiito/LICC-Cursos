"""
API que NO utiliza frameworks como Flask o Django para implementar
los distintos endpoints, el manejo de consultas y la generación de respuestas.  
"""

from wsgiref.simple_server import make_server
import threading
import json


def application(environ, start_response):
    path = environ["PATH_INFO"]

    response = {"mensaje": "Hello World"}
    if path.startswith("/goodbye"):
        response["mensaje"] = "Que la fuerza esté contigo"

    status = "200 OK"
    content_type = "application/json"

    # response headers
    response = json.dumps(response).encode()
    headers = [("Content-Type", content_type), ("Content-Length", str(len(response)))]

    start_response(status, headers)
    return [response]


if __name__ == "__main__":
    w_s = make_server(host="localhost", port=4444, app=application)
    print("Escuchando....")
    thread = threading.Thread(target=w_s.serve_forever, daemon=True)
    thread.start()
    input("Presiona [ENTER] para cerrar el servidor")
