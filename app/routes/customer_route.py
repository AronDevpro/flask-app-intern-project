from flask import jsonify, request

from app import app, db
from app.models.customer_model import Customer
from app.schemas import customer_schema, customers_schema


@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    new_customer = customer_schema.load(data)

    db.session.add(new_customer)
    db.session.commit()

    return jsonify({'message': 'Data added successfully'}), 201


@app.route('/customers', methods=['GET'])
def fetch_customer():
    data = Customer.query.all()
    customer_data = customers_schema.dump(data)

    return jsonify({'data': customer_data}), 200


@app.route('/customers/<int:id>', methods=['GET'])
def get_customer_by_id(id):
    data = Customer.query.get(id)

    if not data:
        return jsonify({'message': 'Customer not found'}), 404

    customer_data = customer_schema.dump(data)

    return jsonify({'data': customer_data}), 200


@app.route('/customers/<int:id>', methods=['PUT'])
def put_customer(id):
    customer = Customer.query.get(id)
    if customer:
        data = request.get_json()
        customer.name = data['name']
        customer.email = data['email']
        customer.phone = data['phone']
        db.session.commit()
        return jsonify({'message': 'Data updated successfully'}), 200
    else:
        return jsonify({'message': 'Customer not found'}), 404


@app.route('/customers/<int:id>', methods=['DELETE'])
def del_customer(id):
    customer_exists = Customer.query.get(id)

    if not customer_exists:
        return jsonify({'message': 'Customer not found'}), 404

    db.session.delete(customer_exists)
    db.session.commit()
    return jsonify({'message': 'Data deleted successfully'}), 200
