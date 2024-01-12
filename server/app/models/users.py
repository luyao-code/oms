"""
Relationships:
- Many-to-one relationship with the Dealer model class.
"""
from .. import db
from sqlalchemy import Enum, ForeignKey
from .types import RoleType

class User(db.Model):
    __tablename__ = 'users'

    # Basic info
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name  = db.Column(db.String(20), nullable=False)
    mobile = db.Column(db.String(20), nullable=False)

    # Authentication info
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    # Roles
    role = db.Column(Enum(RoleType), nullable=False)

    # Relationships
    dealer_id = db.Column(db.Integer, ForeignKey('dealers.id')) 

    # Timestamps Records
    created_at = db.Column(db.DateTime, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)
    deleted_by = db.Column(db.Integer, ForeignKey('users.id'))
    
    def __repr__(self):
        return f'<User {self.name}>'
    