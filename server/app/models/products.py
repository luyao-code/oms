from .. import db
from .types import CategoryType

class Product(db.Model):
    __tablename__ = 'products'

    # Basic info
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    sku = db.Column(db.String(255), nullable=False)
    category = db.Column(db.Enum(CategoryType), nullable=False)
    series = db.Column(db.String(255))

    # Dimensions
    length = db.Column(db.Float, nullable=False)
    width = db.Column(db.Float, nullable=False)
    thickness = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    inventory_sqf = db.Column(db.Float, nullable=False, default=0)
    inventory_box = db.Column(db.Integer, nullable=False, default=0)
    sqf_per_box = db.Column(db.Float, nullable=False)
    
    # Prices
    box_price = db.Column(db.Float, nullable=False)
    pallet_price = db.Column(db.Float, nullable=False)
    box_price_on_sales = db.Column(db.Float, nullable=True)
    pallet_price_on_sales = db.Column(db.Float, nullable=True)
    sales_begin = db.Column(db.Date, nullable=True)
    sales_end = db.Column(db.Date, nullable=True)
