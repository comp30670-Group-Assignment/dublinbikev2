from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

Articles = Articles()

#placeholder for current file
@app.route('/')
def index():
# Normally we return a template, not a string.
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/stations')
def stations():
	return render_template('stations.html')

@app.route('/full-map')
def fullMap():
	return render_template('full-map.html')

@app.route('/articles')
def articles():
	return render_template('articles.html', articles = Articles)

#string.id is a dynamic value
@app.route('/article/<string:id>/')
def article(id):
	return render_template('article.html', id=id)

if __name__ == '__main__':
	app.run(debug=True)

