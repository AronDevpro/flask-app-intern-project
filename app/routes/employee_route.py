from flask import jsonify, request

from app import app, db
from app.models.employee_model import Employee
from app.schemas import employee_schema, employees_schema


@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    employee = employee_schema.load(data)

    db.session.add(employee)
    db.session.commit()

    return jsonify({'message': 'Data added successfully'}), 201


@app.route('/employees', methods=['GET'])
def fetch_employee():
    data = Employee.query.all()
    employee = employees_schema.dump(data)

    return jsonify({'data': employee}), 200


@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id):
    data = Employee.query.get(id)

    if not data:
        return jsonify({'message': 'Employee not found'}), 404

    employee = employee_schema.dump(data)

    return jsonify({'data': employee}), 200


@app.route('/employees/<int:id>', methods=['PUT'])
def put_employee(id):
    employee = Employee.query.get(id)
    if employee:
        data = request.get_json()
        employee.firstName = data['firstName']
        employee.lastName = data['lastName']
        employee.address = data['address']
        employee.phoneNumber = data['phoneNumber']
        employee.dob = data['dob']
        employee.nic = data['nic']
        employee.position = data['position']
        employee.salary = data['salary']
        db.session.commit()
        return jsonify({'message': 'Data updated successfully'}), 200
    else:
        return jsonify({'message': 'Employee not found'}), 404


@app.route('/employees/<int:id>', methods=['DELETE'])
def del_employee(id):
    employee = Employee.query.get(id)

    if not employee:
        return jsonify({'message': 'Employee not found'}), 404

    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Data deleted successfully'}), 200
