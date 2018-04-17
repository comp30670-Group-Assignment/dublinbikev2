from flask import Flask, render_template, jsonify
from dublinbikeflask.extractor import extractorv1
import functools
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html', x=os.path.join(app.instance_path));

@app.route('/_map_data')
def add_numbers():
	recent = extractorv1.Extractor();
	return jsonify(recent.getRecent());

@app.route('/_predictions/<int:file_id>')
def prediction_data(file_id):
	predictionList = [];
	file = "/static/predictions/test.json"
	fileOpen  = file(file, "r");
	for line in fileOpen:
		predictionList.append(line);

@functools.lru_cache(maxsize=256)
@app.route('/_drop_data')
def dropdown():
	stations = extractorv1.Extractor();
	return jsonify(stations.stationNames());

if __name__ == '__main__':
	app.run(debug=True)