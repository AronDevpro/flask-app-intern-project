from app import db


class Supplier(db.Model):
    supplierId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contactNumber = db.Column(db.String(100))
    address = db.Column(db.String(200))