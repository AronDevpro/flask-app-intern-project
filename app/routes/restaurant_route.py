from flask import jsonify, request

from app import app, db
from app.models.restaurant_model import Restaurant
from app.schemas import restaurant_schema, restaurants_schema


@app.route('/restaurants', methods=['POST'])
def create_restaurant():
    data = request.get_json()
    restaurant = restaurant_schema.load(data)

    db.session.add(restaurant)
    db.session.commit()

    return jsonify({'message': 'Data added successfully'}), 201


@app.route('/restaurants', methods=['GET'])
def fetch_restaurant():
    data = Restaurant.query.all()
    restaurant = restaurants_schema.dump(data)

    return jsonify({'data': restaurant}), 200


@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    data = Restaurant.query.get(id)

    if not data:
        return jsonify({'message': 'Restaurant not found'}), 404

    restaurant = restaurant_schema.dump(data)

    return jsonify({'data': restaurant}), 200


@app.route('/restaurants/<int:id>', methods=['PUT'])
def put_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        data = request.get_json()
        restaurant.name = data['name']
        restaurant.address = data['address']
        restaurant.phoneNumber = data['phoneNumber']
        db.session.commit()
        return jsonify({'message': 'Data updated successfully'}), 200
    else:
        return jsonify({'message': 'Restaurant not found'}), 404


@app.route('/restaurants/<int:id>', methods=['DELETE'])
def del_restaurant(id):
    restaurant = Restaurant.query.get(id)

    if not restaurant:
        return jsonify({'message': 'Restaurant not found'}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return jsonify({'message': 'Data deleted successfully'}), 200
