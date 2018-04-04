from flask import Flask, render_template, jsonify
#from extractor import *

app = Flask(__name__)

@app.route('/_add_numbers')
def add_numbers():
	#a = request.args.get('a', 0, type=int)
	#b = request.args.get('b', 0, type=int)
	a = 10;
	b = 10;
	return jsonify(result=a + b)

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

