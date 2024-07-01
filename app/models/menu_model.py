from app import db


class Menu(db.Model):
    menuId = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)