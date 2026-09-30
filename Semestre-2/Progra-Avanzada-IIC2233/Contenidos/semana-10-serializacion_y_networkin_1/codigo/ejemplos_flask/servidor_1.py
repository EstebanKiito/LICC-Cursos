from flask import Flask, request
import random

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return {"texto": "Hello, World!"}


@app.route("/numero_aleatorio", methods=["GET", "POST"])
def numero_aleatorio():
    if request.method == "POST":
        numero = random.randint(0, 6)
        return {"texto": f"Tu número es: {numero}", "método": "POST"}

    numero = random.randint(-4444, -11)
    return {"texto": f"Tu número es: {numero}", "método": "GET"}


if __name__ == "__main__":
    app.run(host="localhost", port=4444)
