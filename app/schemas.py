from flask_marshmallow import Marshmallow, fields
from marshmallow import post_load

from app.models.customer_model import Customer
from app.models.employee_model import Employee
from app.models.inventory_model import Inventory
from app.models.menu_model import Menu
from app.models.order_model import Order
from app.models.orderItem_model import OrderItem
from app.models.reservation_model import Reservation
from app.models.restaurant_model import Restaurant
from app.models.supplierModel import Supplier

ma = Marshmallow()


class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('customerId', 'name', 'email', 'phone')
        model = Customer
        load_instance = True
        include_fk = True

    @post_load
    def make_customer(self, data, **kwargs):
        return Customer(**data)


class SupplierSchema(ma.Schema):
    class Meta:
        fields = ('supplierId', 'name', 'contactNumber', 'address')
        model = Supplier
        load_instance = True
        include_fk = True

    @post_load
    def make_supplier(self, data, **kwargs):
        return Supplier(**data)


class OrderSchema(ma.Schema):
    orderItems = ma.Nested('OrderItemSchema', many=True)

    class Meta:
        fields = ('orderId', 'customerId', 'orderDate', 'totalAmount', 'orderItems')
        model = Order
        include_relationships = True
        load_instance = True
        include_fk = True

    @post_load
    def make_order(self, data, **kwargs):
        return Order(**data)


class OrderItemSchema(ma.Schema):
    class Meta:
        fields = ('orderItemId', 'orderId', 'menuId', 'quantity')
        model = OrderItem
        include_fk = True

    @post_load
    def make_order_items(self, data, **kwargs):
        return OrderItem(**data)


class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ('employeeId', 'firstName', 'lastName', 'address', 'phoneNumber', 'dob', 'nic', 'position', 'salary')
        model = Employee
        load_instance = True

    @post_load
    def make_employee(self, data, **kwargs):
        return Employee(**data)


class MenuSchema(ma.Schema):
    class Meta:
        fields = ('menuId', 'itemName', 'price')
        model = Menu
        load_instance = True

    @post_load
    def make_menu(self, data, **kwargs):
        return Menu(**data)


class InventorySchema(ma.Schema):
    class Meta:
        fields = ('inventoryId', 'itemName', 'quantity')
        model = Inventory
        load_instance = True

    @post_load
    def make_inventory(self, data, **kwargs):
        return Inventory(**data)


class ReservationSchema(ma.Schema):
    class Meta:
        fields = ('reservationId', 'reservation_date', 'reservation_time', 'numberOfPeople', 'customer_id')
        model = Reservation
        load_instance = True
        include_fk = True

    @post_load
    def make_reservation(self, data, **kwargs):
        return Reservation(**data)


class RestaurantSchema(ma.Schema):
    class Meta:
        fields = ('restaurantId', 'name', 'address', 'phoneNumber')
        model = Restaurant
        load_instance = True
        include_fk = True

    @post_load
    def make_restaurant(self, data, **kwargs):
        return Restaurant(**data)


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

supplier_schema = SupplierSchema()
suppliers_schema = SupplierSchema(many=True)

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

order_item_schema = OrderItemSchema()
order_items_schema = OrderItemSchema(many=True)

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

menu_schema = MenuSchema()
menus_schema = MenuSchema(many=True)

reservation_schema = ReservationSchema()
reservations_schema = ReservationSchema(many=True)

inventory_schema = InventorySchema()
inventories_schema = InventorySchema(many=True)

restaurant_schema = RestaurantSchema()
restaurants_schema = RestaurantSchema(many=True)
