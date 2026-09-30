import json
from flask import Flask, Response, request, abort

app = Flask(__name__)


# Caso 1: endpoint dinámico
@app.route("/hi/<string:username>", methods=["GET"])
def saludar(username):
    return {"texto": f"Hola {username}!"}


# Caso 2: argumentos en la URL
@app.route("/argumentos", methods=["GET"])
def argumentos():
    nombre = request.args.get("nombre", default="Guillermo", type=str)
    especie = request.args.get("especie", default="Gato", type=str)
    edad = request.args.get("edad", default=0, type=int)
    return {"texto": f"Hola {especie} {nombre} de {edad} años!"}


# Caso 3: datos en el body
@app.route("/body", methods=["POST"])
def datos_en_body():
    body_data = request.get_json(force=True)
    numero_1 = body_data["var_1"]
    numero_2 = body_data["var_2"]
    resultado = numero_1 + numero_2
    return {"var_1": numero_1, "var_2": numero_2, "result": resultado}


# Caso 4: manejar errores y/o tener más control de las respuestas que se entregan
@app.route("/error/<int:instruccion>", methods=["DELETE"])
def error(instruccion):
    if instruccion == 0:
        abort(400)
    if instruccion == 1:
        return Response(status=418)
    if instruccion == 2:
        return Response(status=200, response='Podemos mandar textos', content_type='text/plain')
    if instruccion == 3:
        respuesta = json.dumps({'mensaje': 'También JSONs'})
        return Response(status=202, response=respuesta, content_type='application/json')



if __name__ == "__main__":
    app.run(host="localhost", port=4444)
