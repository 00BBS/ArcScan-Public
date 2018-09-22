from flask import Flask, render_template
import random
from generate_key import *
import string

#Generate a random 6 digit key:

app = Flask(__name__)

@app.route("/")
def verify_key():
	
	key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))

	return render_template('random_key.html', security_key = key)


if __name__ == "__main__":
	app.run(debug = True, port = 8080)
