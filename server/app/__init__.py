from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
app = Flask(__name__)

def create_app():
    # Database Configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/yao'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Database Initializations
    db.init_app(app)
    # Database Migrations
    from .models import Dealer, User, Order, Product
    migrate = Migrate(app, db)

    return app