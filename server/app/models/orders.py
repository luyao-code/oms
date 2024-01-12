"""
Relationships:
- Many-to-one relationship with the Dealer model class.
"""
from datetime import datetime
from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import relationship
from .shippings import ShippingType
from .status import StatusType
from .. import db

class Order(db.Model):
    __tablename__ = 'orders'

    # Basic info
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.String(255), unique=True, nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow())
    delivery_date = db.Column(db.DateTime, nullable=True)
    delivery_address = db.Column(db.String(255), nullable=False)
    status = db.Column(Enum(StatusType), nullable=False)
    sqf = db.Column(db.Float, nullable=False)
    box = db.Column(db.Integer, nullable=False)
    sales_tax = db.Column(db.Float, nullable=False, default=0)
    total = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, nullable=False, default=0)
    shipping = db.Column(Enum(ShippingType), nullable=False, default=ShippingType.PICKUP)
    shipping_fee = db.Column(db.Float, nullable=False, default=0)

    # Relationships
    dealer_id = db.Column(db.Integer, ForeignKey('dealers.id'), nullable=True) 
    dealer = relationship('Dealer', backref='users')
    # products = db.Column(db.arrays(db.Integer), nullable=False)

    
    