import os
import sys
curr_path = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.dirname(curr_path)
sys.path.append(parent_path)
from app.models import User, Dealer, Order, Product
from app.models import RoleType, ShippingType, StatusType, CategoryType
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def seed_sample_data(db):
    # Create a dealer
    dealer = Dealer(
        name = 'Best Dealer',
        manager = 'Jane Doe',
        phone = '0987654321',
        street = '123 Main St',
        city = 'Springfield',
        state = 'IL',
        zipcode = '62701',
        created_at = datetime.utcnow()
    )

    # Create a user
    user = User(
        email = 'johndoe@example.com',
        first_name = 'John',
        last_name = 'Doe',
        mobile = '1234567890',
        username = 'johndoe',
        password = 'securepassword',
        role = RoleType.ADMIN,
        dealer_id = 1,
        created_at = datetime.utcnow()
    )

    # Create a product
    product = Product(
        name = 'Mars',
        sku = 'MA501',
        category = CategoryType.SPC,
        series = 'Planets',
        length = 10.0,
        width = 5.0,
        thickness = 1.0,
        weight = 60,
        inventory_sqf = 100.0,
        inventory_box = 20000,
        sqf_per_box = 50,
        box_price = 3.0,
        pallet_price = 2.0
    )

    # Create an order
    order = Order(
        order_id='202401080001',
        delivery_address='123 Main St, Springfield, IL 62701',
        status = StatusType.PENDING,
        sqf = 100.0,
        box = 2,
        sales_tax = 0.0625,
        total = 105.0,
        discount = 0.0,
        shipping = ShippingType.PICKUP,
        shipping_fee = 0.0,
        dealer_id = 1
    )

    # Add the sample data to the session
    db.session.add(user)
    db.session.add(dealer)
    db.session.add(order)
    db.session.add(product)

    # Commit the changes
    db.session.commit()

if __name__ == '__main__':
    # Create the Flask app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/yao'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Database Initializations
    db = SQLAlchemy()
    db.init_app(app)

    # Seed the sample data
    with app.app_context():
        seed_sample_data(db)

