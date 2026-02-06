from flask import Blueprint, render_template, request, redirect, url_for

routes = Blueprint("routes", __name__)

@routes.route("/")
def homepage():
    return render_template("index.html")

@routes.route("/profile")
def profile():
    return "Esse é seu perfil"

@routes.route("/generate-items", methods=["GET", "POST"])
def generate_items():
    if request.method == "POST":
        data = request.get_data("/generate_items")
        print(data)
        return redirect(url_for("routes.homepage"))

    return render_template("generate-items.html")
