from app import db


class Order(db.Model):
    orderId = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.customerId'), nullable=False)
    orderDate = db.Column(db.String(100), nullable=False)
    totalAmount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(100), nullable=False, default="completed")
    orderItems = db.relationship('OrderItem', backref='order', lazy=True)