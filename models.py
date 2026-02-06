from db import db

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<item {self.id} - {self.name} - {self.description}"