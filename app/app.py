from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>To Do</h1>'

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