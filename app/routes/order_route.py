from flask import jsonify, request

from app import app, db
from app.models.customer_model import Customer
from app.models.menu_model import Menu
from app.models.order_model import Order
from app.models.orderItem_model import OrderItem
from app.schemas import OrderItemSchema


@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()

    customer_id_exists = Customer.query.get(data['customerId'])
    if not customer_id_exists:
        return jsonify({'message': 'Customer not found'}), 404

    total_amount = 0

    for item in data.get('orderItems', []):
        menu_item = Menu.query.get(item['menuId'])
        if not menu_item:
            return jsonify({'message': f'Menu item with ID {item["menuId"]} not found'}), 404
        total_amount += menu_item.price * item['quantity']

    order = Order(
        customerId=data['customerId'],
        orderDate=data['orderDate'],
        totalAmount=total_amount
    )
    db.session.add(order)
    db.session.commit()

    for item in data.get('orderItems', []):
        order_item = OrderItem(orderId=order.orderId, menuId=item['menuId'], quantity=item['quantity'])
        db.session.add(order_item)
    db.session.commit()
    return jsonify({'message': 'Data added successfully'}), 201


@app.route('/orders', methods=['GET'])
def fetch_order():
    data = Order.query.all()
    orders_data = []
    for order in data:
        order_dict = {
            'orderId': order.orderId,
            'orderDate': order.orderDate,
            'totalAmount': order.totalAmount,
            'orderItems': [OrderItemSchema().dump(orderItem) for orderItem in order.orderItems]
        }
        orders_data.append(order_dict)

    return jsonify({'data': orders_data}), 200


@app.route('/orders/<int:id>', methods=['GET'])
def get_order_by_id(id):
    data = Order.query.get(id)

    if not data:
        return jsonify({'message': 'Order not found'}), 404

    order_dict = {
        'orderId': data.orderId,
        'orderDate': data.orderDate,
        'totalAmount': data.totalAmount,
        'orderItems': [OrderItemSchema().dump(orderItem) for orderItem in data.orderItems]
    }

    return jsonify({'data': order_dict}), 200


@app.route('/orders/<int:id>', methods=['PUT'])
def put_order(id):
    data = request.get_json()

    order = Order.query.get(id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    if 'customerId' in data:
        customer_id_exists = Customer.query.get(data['customerId'])
        if not customer_id_exists:
            return jsonify({'message': 'Customer not found'}), 404
        order.customerId = data['customerId']

    if 'orderDate' in data:
        order.orderDate = data['orderDate']

    if 'orderItems' in data:
        total_amount = 0
        for item in data['orderItems']:
            menu_item = Menu.query.get(item['menuId'])
            if not menu_item:
                return jsonify({'message': f'Menu item with ID {item["menuId"]} not found'}), 404
            total_amount += menu_item.price * item['quantity']

            order_item = OrderItem.query.filter_by(orderId=id, menuId=item['menuId']).first()
            if order_item:
                order_item.quantity = item['quantity']
            else:
                order_item = OrderItem(orderId=id, menuId=item['menuId'], quantity=item['quantity'])
                db.session.add(order_item)

        order.totalAmount = total_amount

    db.session.commit()

    return jsonify({'message': 'Data updated successfully'}), 200


@app.route('/orders/cancel/<int:id>', methods=['PUT'])
def cancel_order(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    order.status = 'cancelled'

    db.session.commit()

    return jsonify({'message': 'Order Cancelled'}), 200
