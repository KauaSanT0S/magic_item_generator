from flask import Blueprint, render_template, request, redirect, url_for
from models import Item
from magic_item_generator import generate_itens

routes = Blueprint("routes", __name__)

@routes.route("/")
def homepage():
    items = Item.query.all()
    return render_template("index.html", items=items)

@routes.route("/generate-items", methods=["GET", "POST"])
def generate_items():
    if request.method == "POST":
        itemQtd = request.form.get("itemQtd")
        item_dicts = generate_itens(itemQtd)

        print(item_dicts)

        return redirect(url_for("routes.homepage"))

    return render_template("generate-items.html")

@routes.route("/delete-item", methods=["GET", "DELETE"])
def delete_item():
    if request.method == "DELETE":
        print("deletano tano tano")