from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from random_key import *
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Meme'
db = SQLAlchemy(app) 

from models import Societies, Events, Users

## Flask-Login configs ##
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='/'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

#########################

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
@app.route('/soclogin', methods=['GET','POST'])
def soclogin():
    if request.method == "POST":
        username_check = request.form.get('username')
        print (username_check)
        password_check = request.form.get('password')
        # query based on username
        society = Societies.query.filter_by(username = username_check).first()
        if (password_check == society.password):
            login_user(society)
            return "Logged in, welcome back " + str(society.name)
    return render_template('soclogin.html')

@app.route('/stulogin', methods=['GET','POST'])
def stulogin():
    if request.method == "POST":
        zid_check = request.form.get('zid')
        password_check = request.form.get('password')
        # query based on username
        user = Users.query.filter_by(zid = zid_check).first()
        if (password_check == user.password):
            login_user(user)
            return "Logged in, welcome back " + str(user.name)
    return render_template('stulogin.html')

@app.route('/sturegister', methods=['GET','POST']  )
def sturegister():
    if request.method == "POST":
        new_user = Users(zid = request.form.get('zid'),
                    name = request.form.get('name'),
                    arc = request.form.get('arc'),
                    password = request.form.get('password'))
        db.session.add(new_user)
        db.session.commit()
        ### TODO: REDIRECT TO LOGIN DASHBOARD
        return "Thanks for registering, " + str(new_user.name)
    return render_template('sturegister.html')

@app.route('/socregister', methods = ['GET', 'POST'])
def socregister():
    if request.method == "POST":
        new_soc = Societies(name = request.form.get('name'),
                    username = request.form.get('username'),
                    password = request.form.get('password'))
        db.session.add(new_soc)
        db.session.commit()

        ### TODO: REDIRECT TO LOGIN DASHBOARD
        return "Thanks for registering, " + str(new_soc.name)
    return render_template('socregister.html')

@app.route('/event/<int:event_id>', methods = ['GET', 'POST'])
def event(event_id):
    event = Events.query.filter_by(id = event_id).one()

    # handles POST method (play button to generate 6 digit code)
    if request.method == "POST":
        pushing_code = Events(secret_code = verify_key())
        db.session.add(pushing_code)
        db.session.commit()

    # returns event specific page
    return render_template('event.html', event = event) 

@app.route('/create', methods = ['GET','POST'])
def create():
    new_event = Events(name = request.form.get('name'),
                location = request.form.get('location'),
                starttime = request.form.get('starttime'),
                date = request.form.get('date'),
                secret_code = "000000",
                society =  current_user.name)
    db.session.add(new_event)
    db.session.commit()
    return render_template('create.html')

@app.route('/socdash', methods=['GET','POST'])
def socdash():
    # query events based on society that's logged in
    curr_soc_events = Events.query.filter_by(society=current_user.id).all()
    return render_template('socdash.html', events=curr_soc_events, society = current_user.name)

@app.route('/logout')
def logout():
    logout_user
    return redirect('/index')







