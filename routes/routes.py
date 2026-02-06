from flask import Blueprint, render_template, request, redirect, url_for
from models import Item
from magic_item_generator import generate_itens
from db import db

routes = Blueprint("routes", __name__)

@routes.route("/")
def homepage():
    items = Item.query.all()
    return render_template("index.html", items=items)

@routes.route("/generate-items", methods=["GET", "POST"])
def generate_items():
    if request.method == "POST":
        itemQtd = max(1, min(int(request.form.get("itemQtd", 0)), 20))
        item_dicts = generate_itens(itemQtd)

        for item in item_dicts:
            db.session.add(
                Item(name=item["name"], description=item["description"]))
        
        db.session.commit()

        return redirect(url_for("routes.homepage"))

@routes.route("/delete-item", methods=["POST"])
def delete_item():
    item_id = request.form.get("item_id")

    if not item_id:
        return redirect(url_for("routes.homepage"))
    
    item = Item.query.get(item_id)

    if item:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for("routes.homepage"))