from flask import jsonify, request

from app import app, db
from app.models.inventory_model import Inventory
from app.schemas import inventory_schema, inventories_schema


@app.route('/inventories', methods=['POST'])
def create_inventory():
    data = request.get_json()
    inventory = inventory_schema.load(data)

    db.session.add(inventory)
    db.session.commit()

    return jsonify({'message': 'Data added successfully'}), 201


@app.route('/inventories', methods=['GET'])
def fetch_inventory():
    data = Inventory.query.all()
    inventory = inventories_schema.dump(data)

    return jsonify({'data': inventory}), 200


@app.route('/inventories/<int:id>', methods=['GET'])
def get_inventory_by_id(id):
    data = Inventory.query.get(id)

    if not data:
        return jsonify({'message': 'Inventory not found'}), 404

    inventory = inventory_schema.dump(data)

    return jsonify({'data': inventory}), 200


@app.route('/inventories/<int:id>', methods=['PUT'])
def put_inventory(id):
    inventory = Inventory.query.get(id)
    if inventory:
        data = request.get_json()
        inventory.itemName = data['itemName']
        inventory.quantity = data['quantity']
        db.session.commit()
        return jsonify({'message': 'Data updated successfully'}), 200
    else:
        return jsonify({'message': 'Inventory not found'}), 404


@app.route('/inventories/<int:id>', methods=['DELETE'])
def del_inventory(id):
    inventory = Inventory.query.get(id)

    if not inventory:
        return jsonify({'message': 'Inventory not found'}), 404

    db.session.delete(inventory)
    db.session.commit()
    return jsonify({'message': 'Data deleted successfully'}), 200
