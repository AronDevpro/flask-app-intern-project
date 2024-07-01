from app import db


class Inventory(db.Model):
    inventoryId = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)