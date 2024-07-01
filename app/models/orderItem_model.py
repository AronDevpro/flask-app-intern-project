from app import db


class OrderItem(db.Model):
    orderItemId = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer, db.ForeignKey('order.orderId'), nullable=False)
    menuId = db.Column(db.Integer, db.ForeignKey('menu.menuId'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)