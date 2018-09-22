from server import app, system
from flask import request, render_template, session

@app.route('/', methods = ['GET', 'POST'])


@app.route('/profile/<user>', methods=['GET'])
def profile(user):


@app.route()