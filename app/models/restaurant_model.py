from app import db


class Restaurant(db.Model):
    restaurantId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phoneNumber = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)