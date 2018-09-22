from routes import db
from flask_login import UserMixin

class Societies(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(15))
    password = db.Column(db.String(20))
    events = db.relationship("Events", backref="eventOwner")

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60))
    password = db.Column(db.String(60))
    arc = db.Boolean()
    zid = db.Column(db.String(8))

class Events(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(30))
    starttime = db.Column(db.Time)
    date = db.Column(db.Date)
    secret_code = db.String(6)
    society = db.Column(db.Integer,db.ForeignKey("societies.id"))
