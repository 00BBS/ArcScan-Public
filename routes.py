from flask import Flask, request, render_template, session
from flask_sqlalchemy import SQLAlchemy
from random_key import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Societies, Events, Users
#this would be login
@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

'''
@app.route('/profile/<user>', methods = ['GET']
        if:
                return render_template('profSoc.html')
        else:
                return render_template('profInd.html')
'''
@app.route('/soclogin')
def soclogin():
    if request.method == "POST":
        username_check = request.form['username']
        password_check = request.form['password']
        # query based on username
        society = Societies.query.filter_by(username = username_check).first()
        if (password == society.password):
            return "Logged in, welcome back " + society.name
    return render_template('soclogin.html')

@app.route('/stulogin')
def stulogin():
    if request.method == "POST":
        zid_check = request.form['zid']
        password_check = request.form['password']
        # query based on username
        user = Users.query.filter_by(zid = zid_checl).first()
        if (password == user.password):
            return "Logged in, welcome back " + user.name
    return render_template('stulogin.html')

@app.route('/sturegister')
def sturegister():
    if request.method == "POST":
        new_user = Users(zid = request.form['zid'],
                    name = request.form['name'],
                    arc = request.form['arc'],
                    password = request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        ### TODO: REDIRECT TO LOGIN DASHBOARD
        return "Thanks for registering, " + new_user.name
    return render_template('sturegister.html')

@app.route('/socregister')
def socregister():
    if request.method == "POST":
        new_soc = Societies(name = request.form['name'],
                    username = request.form['username'],
                    password = request.form['password'],
        db.session.add(new_soc)
        db.session.commit()
        ### TODO: REDIRECT TO LOGIN DASHBOARD
        return "Thanks for registering, " + new_soc.name
    return socregister('socregister.html')

