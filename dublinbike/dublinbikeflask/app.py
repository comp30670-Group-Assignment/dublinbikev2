from flask import Flask, render_template, jsonify
from extractor import extractorv1
import functools
import os
import sqlalchemy as sql
import pandas as pd
import datetime
import pickle


def predictions():
	
	conex = sql.create_engine("mysql+pymysql://root:Rugby_777@localhost/dublinbikes")
	
	now = datetime.datetime.now()
	        
	day = now.day
	
	query_weather = "select * from weatherForecast where day(from_unixtime(dt)) = %d" % (day)
	
	df_weather = pd.read_sql_query(query_weather, conex)
	
	predictions = {}
	
	
	
	for a in range(1,103):
			
		try:
			
			predictions[a] = []
			
			
			df_bikes_test = pd.read_sql_query("SELECT AVG(available_bikes) as available_bikes, HOUR(timestamp) as hour from data where number = %d group by hour" % a, conex)
			df_weather = pd.read_sql_query("SELECT temp, humidity, pressure, hour, dt_txt, description from weatherForecast where DAY(dt_txt) = %d" % day, conex)
			
			for j, row in df_weather.iterrows():
	
			    df_weather.loc[j, 'day'] = pd.to_datetime(row['dt_txt']).weekday_name
			
			#make dummy variables for each day of the week
			dummy = pd.get_dummies(df_weather['day'])
			df_weather = pd.concat([dummy, df_weather], axis = 1)
			days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
			for x in days:
			    if df_weather['day'][0] != x:
			
			        df_weather[x] = [0] * len(df_weather)
			
			
			
			#construct weather dummy variables by getting all unique weather descriptions from the database
			dummy = pd.get_dummies(df_weather['description'])
			df_weather = pd.concat([df_weather,dummy], axis = 1) 
			unique_weather = pd.read_sql_query("SELECT DISTINCT(main) FROM dublin_weather", conex)
			for y, row2 in unique_weather.iterrows():
			
			    if not row2['main'] in df_weather['description'].values:
			
			        df_weather[row2['main']] = [0] * len(df_weather)
			        
			df_weather = df_weather.drop(['day','description','dt_txt'], axis = 1)
			
			df_weather = df_weather[['Friday','Saturday','Sunday','Thursday','Tuesday','Wednesday','temp','pressure','humidity','hour','Monday','Clear','Clouds','Drizzle','Mist','Rain','Snow','Fog']]
			
			rf_test = pickle.load(open("static/%d.pkl" % a, 'rb'))
			
			prediction = rf_test.predict(df_weather.values)
			
			prediction = prediction.tolist()
			
			predictions[a] = prediction
		
		except:
		
			print("except")
			predictions[a] = 0
			pass
			
	return predictions

	
	

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