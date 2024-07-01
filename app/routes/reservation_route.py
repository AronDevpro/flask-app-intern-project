from flask import jsonify, request

from app import app, db
from app.models.customer_model import Customer
from app.models.reservation_model import Reservation
from app.schemas import reservation_schema, reservations_schema


@app.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()

    customer_id_exists = Customer.query.get(data['customer_id'])
    if not customer_id_exists:
        return jsonify({'message': 'Customer not found'}), 404
    reservation = reservation_schema.load(data)

    db.session.add(reservation)
    db.session.commit()

    return jsonify({'message': 'Data added successfully'}), 201


@app.route('/reservations', methods=['GET'])
def fetch_reservation():
    data = Reservation.query.all()
    reservation = reservations_schema.dump(data)

    return jsonify({'data': reservation}), 200


@app.route('/reservations/<int:id>', methods=['GET'])
def get_reservation_by_id(id):
    data = Reservation.query.get(id)

    if not data:
        return jsonify({'message': 'Reservation not found'}), 404

    reservation = reservation_schema.dump(data)

    return jsonify({'data': reservation}), 200


@app.route('/reservations/<int:id>', methods=['PUT'])
def put_reservation(id):
    reservation = Reservation.query.get(id)
    if reservation:
        data = request.get_json()
        reservation.reservation_date = data['reservation_date']
        reservation.reservation_time = data['reservation_time']
        reservation.numberOfPeople = data['numberOfPeople']
        reservation.customer_id = data['customer_id']
        db.session.commit()
        return jsonify({'message': 'Data updated successfully'}), 200
    else:
        return jsonify({'message': 'Reservation not found'}), 404


@app.route('/reservations/<int:id>', methods=['DELETE'])
def del_reservation(id):
    reservation = Reservation.query.get(id)

    if not reservation:
        return jsonify({'message': 'Reservation not found'}), 404

    db.session.delete(reservation)
    db.session.commit()
    return jsonify({'message': 'Data deleted successfully'}), 200
