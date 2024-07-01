from app import db


class Reservation(db.Model):
    reservationId = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customerId'), nullable=False)
    reservation_date = db.Column(db.String(20), nullable=False)
    reservation_time = db.Column(db.String(20), nullable=False)
    numberOfPeople = db.Column(db.Integer, nullable=False)