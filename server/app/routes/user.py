from database import Client
from app import db
from flask import make_response, Blueprint

bp = Blueprint('user', __name__)
client = None

def get_client():
    global client
    if client is None:
        client = Client(db)
    return client

@bp.route('/users')
def get_all_users():
    header = {
        'Access-Control-Allow-Origin': "*"
    }
    data = client.get_all_items('users')
    response = make_response(data)
    response.headers = header
    response.status_code = 200
    return response
    