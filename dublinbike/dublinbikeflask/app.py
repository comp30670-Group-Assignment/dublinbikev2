from flask import Flask, render_template, jsonify
from dublinbikeflask.extractor import extractorv1
import functools

app = Flask(__name__)

@app.route('/_map_data')
def add_numbers():
	recent = extractorv1.Extractor()
	return jsonify(recent.getRecent())

@app.route('/')
@functools.lru_cache(maxsize=256)
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

