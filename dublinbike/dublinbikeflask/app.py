from flask import Flask, render_template, jsonify
from dublinbikeflask.extractor import extractorv1

app = Flask(__name__)

@app.route('/_add_numbers')
def add_numbers():
	recent = extractorv1.Extractor()
	return jsonify(recent.getRecent())

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/weather')
def weather():
	return render_template('weather.html')

@app.route('/stations')
def stations():
	return render_template('stations.html')

if __name__ == '__main__':
	app.run(debug=True)

