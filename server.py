from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='hjkfjkhadfhjadfshjadshjkdsjhksdjkh'

import random

@app.route('/')
def index():
	if not session.has_key('number'):
		session['number'] = random.randint(1,100)
	print 'Random number is', session['number']
	number = session['number']
	return render_template('index.html', number=number)

@app.route('/submit', methods=['POST'])
def submit():
	if session['number'] == int(request.form['guess']):
		print 'Your Guess is Correct'
		showme3 = 'showme'
	elif int(request.form['guess']) > session['number']:
		print 'Your Guess is Too High'
		showme2='showme'
	elif int(request.form['guess']) < session['number']:
		print 'Your Guess is Too Low'
		showme1='showme'
	return redirect('/')
# @app.route('/')
# def clear():
# 	session.clear()
# 	return redirect('/')
app.run(debug=True)