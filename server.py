from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='hjkfjkhadfhjadfshjadshjkdsjhksdjkh'
import random
@app.route('/')
def index():
	if not session.has_key('number'):
		session['number'] = random.randint(1,100)
	print 'The random number is', session['number']
	number = session['number']
	if not session.has_key('guess'):
		session['guess'] = 0
	print session
	return render_template('index.html', number=number)
@app.route('/submit', methods=['POST'])
def submit():
	guess1 = int(request.form['guess'])
	if session['number'] == int(request.form['guess']):
		print 'Your Guess is Correct'
	elif int(request.form['guess']) > session['number']:
		print 'Your Guess is Too High'
	elif int(request.form['guess']) < session['number']:
		print 'Your Guess is Too Low'
	print 'Your guess was', guess1
	session['guess']=guess1
	print session
	return redirect('/')
@app.route('/clear')
def clear():
	session.clear()
	return redirect('/')
app.run(debug=True)