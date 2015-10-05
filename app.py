from flask import Flask, render_template, url_for, redirect,\
	request, flash, jsonify 
from sqlalchemy import create_engine, and_, asc, desc, func, update
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

@app.route('/')
def homepage():
	"""Takes user to index"""
	return redirect(url_for('index'))

@app.route('/index/')
def index():
	"""Main page displaying restaurants"""
	return render_template('index.html')


if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)