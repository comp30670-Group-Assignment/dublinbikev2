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
	
	for i in range(1,101):
		
		df_reg = pd.read_sql_query("SELECT available_bikes, timestamp, temp, main , pressure, humidity, HOUR(FROM_UNIXTIME(dt)) as hour FROM dublinbikes.data as dd join dublinbikes.dublin_weather as dw where hour(dd.timestamp) = hour(from_unixtime(dw.dt)) and day(dd.timestamp) = day(from_unixtime(dw.dt)) and month(dd.timestamp) = month(from_unixtime(dw.dt)) and dd.number = %d" % (i), conex)
        df_reg['day'] = [0] * len(df_reg)
	
        for j, row in df_reg.iterrows():
        	
        	df_reg.loc[j, 'day'] = pd.to_datetime(row['timestamp']).weekday_name

        dummy= pd.get_dummies(df_reg['day'])
        df_reg = pd.concat([dummy, df_reg], axis = 1)

        dummy = pd.get_dummies(df_reg['main'])
        df_reg = pd.concat([df_reg,dummy], axis = 1) 

        df_reg_ready = df_reg.drop(['timestamp','available_bikes','day','main'], axis = 1)
        
        rf = pickle.load(open("%d.pkl" %i, 'rb'))
        
        predicted_test = rf_test.predict(df_reg['available_bikes'])
        
        predictions[i] = predicted_test
     
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