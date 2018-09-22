#This function generates a security key
from random import randint

def generate_security_key():
	digit_1 = str(randint(0,9))
	digit_2 = str(randint(0,9))
	digit_3 = str(randint(0,9))
	digit_4 = str(randint(0,9))
	digit_5 = str(randint(0,9))
	digit_6 = str(randint(0,9))

	random_security_key = int(digit_1 + digit_2 + digit_3 + digit_4 + digit_5 + digit_6)

	return random_security_key

