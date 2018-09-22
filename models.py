from routes import db

class Societies(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(15))
    password = db.Column(db.String(20))
    events = db.relationship("Events", backref="eventOwner")

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60))
    arc = db.Boolean()
    zID = db.Column(db.String(8))

class Events(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(30))
    starttime = db.Column(db.Time)
    date = db.Column(db.Date)
    society = db.Column(db.Integer,db.ForeignKey("societies.id"))
