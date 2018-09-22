from flask import Flask, request, render_template, session
from flask_sqlalchemy import SQLAlchemy

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
        return "Registered"
        '''
        # find user
        user_check = Users.query.filter_by(zid=request.form['zid']).first()
        if user_check:
            if user_check.password == request.form['password']:
                return "registered"
        '''
    return render_template('index.html')

'''
@app.route('/profile/<user>', methods = ['GET']
	if:
		return render_template('profSoc.html')
	else:
		return render_template('profInd.html')
'''
