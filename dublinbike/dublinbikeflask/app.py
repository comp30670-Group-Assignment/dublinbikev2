from flask import Flask, render_template
#from extractor import *

app = Flask(__name__)

#placeholder for current file
@app.route('/')
def index():
# Normally we return a template, not a string.
	return render_template('home.html')

@app.route('/weather')
def weather():
	return render_template('weather.html')

@app.route('/stations')
def stations():
	return render_template('stations.html')

if __name__ == '__main__':
	app.run(debug=True)

