from flask import Flask, render_template, jsonify
from extractor import extractorv1
import functools
import os

app = Flask(__name__)

@app.route('/')
@functools.lru_cache(maxsize=256)
def index():
	return render_template('home.html', x=os.path.join(app.instance_path))

@app.route('/_map_data')
def add_numbers():
	recent = extractorv1.Extractor()
	return jsonify(recent.getRecent())

if __name__ == '__main__':
	app.run(debug=True)