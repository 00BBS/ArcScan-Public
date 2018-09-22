from flask import Flask, request, render_template, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'sqlite:///databases/main.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')
