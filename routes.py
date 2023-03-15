from app import app, Race, db
from flask import request, jsonify
from datetime import datetime

@app.route('/', methods = ['GET'])
def hello():
    if request.method == 'GET':
        return 'Hello, World!'
    else:
        return '405'


@app.route('/create', methods = ['POST'])
def createRace():
    content = request.get_json()
    date = content["date"].split()[0]
    time = content["date"].split()[1]
    d = datetime(year=int(date.split('.')[2]), month= int(date.split('.')[1]),
                 day= int(date.split('.')[0]), hour=int(time.split(':')[0]),
                 minute= int(time.split(':')[1]))
    r = Race(content["name"], d, content["organizer"], content["place"])
    db.session.add(r)
    db.session.commit()
    db.session.close()
    return '200'
