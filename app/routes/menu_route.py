from flask import jsonify, request

from app import app, db
from app.models.menu_model import Menu
from app.schemas import menus_schema, menu_schema


@app.route('/menus', methods=['POST'])
def create_menu():
    data = request.get_json()
    menu = menu_schema.load(data)

    db.session.add(menu)
    db.session.commit()

    return jsonify({'message': 'Data added successfully'}), 201


@app.route('/menus', methods=['GET'])
def fetch_menu():
    data = Menu.query.all()
    menu = menus_schema.dump(data)

    return jsonify({'data': menu}), 200


@app.route('/menus/<int:id>', methods=['GET'])
def get_menu_by_id(id):
    data = Menu.query.get(id)

    if not data:
        return jsonify({'message': 'Menu not found'}), 404

    menu = menu_schema.dump(data)

    return jsonify({'data': menu}), 200


@app.route('/menus/<int:id>', methods=['PUT'])
def put_menu(id):
    menu = Menu.query.get(id)
    if menu:
        data = request.get_json()
        menu.itemName = data['itemName']
        menu.price = data['price']
        db.session.commit()
        return jsonify({'message': 'Data updated successfully'}), 200
    else:
        return jsonify({'message': 'Menu not found'}), 404


@app.route('/menus/<int:id>', methods=['DELETE'])
def del_menu(id):
    menu = Menu.query.get(id)

    if not menu:
        return jsonify({'message': 'Menu not found'}), 404

    db.session.delete(menu)
    db.session.commit()
    return jsonify({'message': 'Data deleted successfully'}), 200
