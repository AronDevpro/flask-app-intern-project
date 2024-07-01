from app import db


class Employee(db.Model):
    employeeId = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(40), nullable=False)
    lastName = db.Column(db.String(40), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phoneNumber = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.String(100), nullable=False)
    nic = db.Column(db.String(20), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    salary = db.Column(db.Float, nullable=False)