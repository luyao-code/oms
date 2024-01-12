"""
Relationships:
- One-to-many relationship with the User model class.
- One-to-many relationship with the Order model class.
"""
from datetime import datetime
from .. import db

class Dealer(db.Model):
    __tablename__ = 'dealers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    manager = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    street = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    zipcode = db.Column(db.String(10), nullable=False)
    sales = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)
    # deleted_by = db.Column(db.Integer, db.ForeignKey('users.id'))
