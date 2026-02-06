from flask import Blueprint

routes = Blueprint("routes", __name__)

@routes.route("/")
def homepage():
    return "Essa é a homepage"

@routes.route("/profile")
def profile():
    return "Esse é seu perfil"

@routes.route("/blog")
def blog():
    return "Esse é o blog"