import requests
import json
import time
import datetime

# Import MySQl
from mysql.connector import (connection, cursor)
from gevent.libev.corecext import stat


class Extractor:
     
    avg_available_stand_dict = {}
    avg_available_bike_dict = {}
    lat_long = {}
    json = 0
    
    def __init__(self):
        
        
        
        """
        Aim of this class is to return a dictionary that holds an entry for every station.
        This entry will consist of a bi-dimensional dictionary. The first level of this 
        dictionary will hold entries for each hour of the day (from 0 to 23). Each hour
        entry will correspond to an average value for that period.
        """
        
        #constructor sets up database connection and creates tuple that holds all station names
        
        self.conex = connection.MySQLConnection(user='root', password='******', host='0.0.0.0', database='dublinbikes')
        # MySQL object
        self.cursor = self.conex.cursor()
        
        station_names_query = "SELECT distinct(Name) FROM data"
        
        self.cursor.execute(station_names_query)
        
        self.station_names = self.cursor.fetchall()
        
        
    
    def avg_available_stand(self):
        
        #loop through all station names
        
        for j in self.station_names:
            #tell the computer that the dictionary is multidimensional and declare a new inner dict
            self.avg_available_stand_dict[j[0]] = {}
            #for each station name 
            for i in range(0, 24):
                total_tuple = self.selectHour(i, "available_bike_stands")
                #returns tuple with all values relevant to the selected time period
                total = 0
                for x in total_tuple:
                    total += int(x[0])
                avg = total / len(total_tuple)
                self.avg_available_stand_dict[j[0]][i] = avg
                
            
            
    def avg_available_bike(self):
        
        for j in self.station_names:
            
            self.avg_available_bike_dict[j[0]] = {}
        
            for i in range(0, 24):
                
                total_tuple = self.selectHour(i, "available_bikes")
                
                #returns tuple with all values relevant to the selected time period
                total = 0
                for x in total_tuple:
                    total += int(x[0])
                avg = total / len(total_tuple)
        
                self.avg_available_bike_dict[j[0]][i] = avg
                
    def selectStation(self, x, h):
        
        query = 'SELECT distinct(%s) FROM dublinbikes.data WHERE name = "%s"' % (x , h)
        
        self.cursor.execute(query)
        
        output = self.cursor.fetchall()
        
        return output
                
    def getLatAndLong(self):
        
        #method queries the latitude and longitude of each station and appends
        #a dictionary containing the lat and long onto a dictionary that holds
        #information for each station (lat&long)
        
        for j in self.station_names:
    
            lat = self.selectStation("position_lat", j[0])
            long = self.selectStation("position_lng", j[0])
            
            self.lat_long["%s" % j[0]] = {"%s" % "latitude":float(lat[0][0]), "%s" % "longitude":float(long[0][0])}
            
        self.json = json.dumps(self.lat_long)
        
            
    def selectHour(self, h, x):
        
        #query needs completion
        query = 'SELECT %s FROM dublinbikes.data WHERE HOUR(timestamp) = %d' % (x , h)
        
        self.cursor.execute(query)
        
        output = self.cursor.fetchall()
        
        return output
    
    
    
    def closeConex(self):
        
        self.conex.close()
        
