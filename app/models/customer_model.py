from app import db


class Customer(db.Model):
    customerId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    orders = db.relationship('Order', backref='customer', lazy=True)