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
    if request.method == "POST":
        new_user = Users(zid = request.form['zid'],
                    name = request.form['name'],
                    arc = request.form['arc'],
                    password = request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        if user_check.password == request.form['password']:
                return "registered" ### TODO: REDIRECT TO LOGIN DASHBOARD
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
    return render_template('soclogin.html')

@app.route('/stulogin')
def stulogin():
    return render_template('stulogin.html')

