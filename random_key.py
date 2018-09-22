from flask import Flask, render_template
import random
import string

def verify_key():
	
	key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))

	return key

