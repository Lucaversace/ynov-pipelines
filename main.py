from bottle import route, run, template
from functions import addition


@route("/<name>")
def index(name):
    return template("<b>Hello {{name}}</b>!", name=name)


@route("/add/<a>/<b>/")
def add(a, b):
    return template(addition(a, b), a=a, b=b)


run(host="localhost", port=8080)
