from app import app
from flask import request

@app.route('/', methods = ['GET'])
def hello():
    if request.method == 'GET':
        return 'Hello, World!'
    else:
        return '405'