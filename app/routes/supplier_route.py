from flask import jsonify, request

from app import app, db
from app.models.supplierModel import Supplier
from app.schemas import suppliers_schema, supplier_schema


@app.route('/suppliers', methods=['POST'])
def create_supplier():
    data = request.get_json()
    supplier = supplier_schema.load(data)

    db.session.add(supplier)
    db.session.commit()

    return jsonify({'message': 'Data added successfully'}), 201


@app.route('/suppliers', methods=['GET'])
def fetch_supplier():
    data = Supplier.query.all()
    supplier = suppliers_schema.dump(data)

    return jsonify({'data': supplier}), 200


@app.route('/suppliers/<int:id>', methods=['GET'])
def get_supplier_by_id(id):
    data = Supplier.query.get(id)

    if not data:
        return jsonify({'message': 'Supplier not found'}), 404

    customer_data = supplier_schema.dump(data)

    return jsonify({'data': customer_data}), 200


@app.route('/suppliers/<int:id>', methods=['PUT'])
def put_supplier(id):
    supplier = Supplier.query.get(id)
    if supplier:
        data = request.get_json()
        supplier.name = data['name']
        supplier.contactNumber = data['contactNumber']
        supplier.address = data['address']
        db.session.commit()
        return jsonify({'message': 'Data updated successfully'}), 200
    else:
        return jsonify({'message': 'Supplier not found'}), 404


@app.route('/suppliers/<int:id>', methods=['DELETE'])
def del_supplier(id):
    supplier = Supplier.query.get(id)

    if not supplier:
        return jsonify({'message': 'Supplier not found'}), 404

    db.session.delete(supplier)
    db.session.commit()
    return jsonify({'message': 'Data deleted successfully'}), 200
