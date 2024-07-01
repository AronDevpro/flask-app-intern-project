from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)

from app.models import customer_model
from app.models import inventory_model
from app.models import employee_model
from app.models import menu_model
from app.models import order_model
from app.models import orderItem_model
from app.models import reservation_model
from app.models import supplierModel
from app.routes import customer_route
from app.routes import supplier_route
from app.routes import menu_route
from app.routes import employee_route
from app.routes import reservation_route
from app.routes import inventory_route
from app.routes import restaurant_route
from app.routes import order_route

with app.app_context():
    db.create_all()
