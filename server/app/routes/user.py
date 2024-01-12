from ..app import app, db
from flask import make_response

@app.route('/info')
def get_info():
    header = {
        'Access-Control-Allow-Origin': "*"
    }
    data = {
        'name': 'ToDo',
        'dev': 'Yao'
    }
    response = make_response(data)
    response.headers = header
    response.status_code = 200
    return response
    