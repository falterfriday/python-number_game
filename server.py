from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='hjkfjkhadfhjadfshjadshjkdsjhksdjkh'
import random
random.randrange(0,101)
@app.route('/')
def index():
	return render_template('index.html')


@app.route('/')
def clear():
	session.clear()
	return redirect('/')
app.run(debug=True)