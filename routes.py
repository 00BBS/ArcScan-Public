from flask import Flask, request, render_template, session

app = Flask(__name__)


#this would be login
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/profile/<user>', methods = ['GET']
		if:
			return render_template('')
		else:
			return render_template('')
