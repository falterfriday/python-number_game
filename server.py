from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='hjkfjkhadfhjadfshjadshjkdsjhksdjkh'

import random

@app.route('/')
def index():
	if not session.has_key('number'):
		session['number'] = random.randint(1,100)
	print 'Random number is', session['number']
	return render_template('index.html')


# @app.route('/')
# def clear():
# 	session.clear()
# 	return redirect('/')
app.run(debug=True)