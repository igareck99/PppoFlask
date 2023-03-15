from flask import Flask
from flask_migrate import Migrate
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from secretKeys import *

app = Flask(__name__)
app.config.from_object(Configuration)
app.secret_key = secret_key
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Race(db.Model):
    __tablename__ = 'race'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True)
    date = db.Column(db.DateTime)
    organizer = db.Column(db.String(40))
    place = db.Column(db.String(160))

    def __init__(self, name, date, organizer, place):
        self.name = name
        self.date = date
        self.organizer = organizer
        self.place = place

    def __repr__(self):
        return f'{self.ids}'