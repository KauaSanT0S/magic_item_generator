from flask import Flask
from routes.routes import routes
from flask_sqlalchemy import SQLAlchemy
import os
from db import db
from models import Item

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'test.db')
db.init_app(app)
app.register_blueprint(routes)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)