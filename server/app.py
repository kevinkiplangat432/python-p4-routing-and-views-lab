#!/usr/bin/env python3

from flask import Flask
from flask import Response, abort

app = Flask(__name__)

@app.get("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.get("/print/<string:name>")
def print_string(name):
    print(name)
    return name

@app.get("/count/<int:number>")
def count(number):
    numbers ="\n".join(str(i) for i in range(number)) + "\n"
    return Response(numbers, mimetype="text/plain")

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num2 == 0:
            abort(400, description="Division by zero")
        result = num1 / num2
    elif operation == "%":
        if num2 == 0:
            abort(400, description="Modulo by zero")
        result = num1 % num2
    else:
        abort(404, description="Invalid operation")

    return str(result)



if __name__ == '__main__':
    app.run(port=5555, debug=True)
