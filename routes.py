from flask import Flask, request, render_template, session
from flask_sqlalchemy import SQLAlchemy
from models import Societies, Events, Users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#this would be login
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/profile/<user>', methods = ['GET']
	if:
		return render_template('profSoc.html')
	else:
		return render_template('profInd.html')

