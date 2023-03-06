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

class Ticket(db.Model):
    __tablename__ = 'ticket'
    id = db.Column(db.Integer, primary_key=True)
    ids = db.Column(db.String(200), index=True)
    date = db.Column(db.DateTime)
    groups = db.Column(db.String(40))
    datas = db.Column(db.String(40))

    def __init__(self, ids, date, groups):
        self.ids = ids
        self.date = date
        self.groups = groups

    def __repr__(self):
        return f'{self.ids}'