import requests
import json
import time

# Import MySQl
from mysql.connector import (connection, cursor)
from gevent.libev.corecext import stat

def main():
    
    # Connection to local database
    conex = connection.MySQLConnection(user='root', password='Rugby_777', host='0.0.0.0', database='dublinbikes')
    # MySQL object
    cursor = conex.cursor()
    
    
    while True:

        link = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&&apiKey=4dc48c410fefd7a42d52cdc4a9c6eb7ce0f67ae0"
        
        r = requests.get(link)
        jTxt = json.loads(r.text)
        
        if r.status_code == 200:
            
            try:
                
                for i in jTxt:
                
                    number = i['number']
                    name = i['name']
                    address = i['address']
                    position_lat = i['position']['lat']
                    position_lng = i['position']['lng']
                    bike_stands = i['bike_stands']
                    status = i['status']
                    available_bike_stands = i['available_bike_stands']
                    available_bikes = i['available_bikes']
                    last_update = i['last_update']
                    
                    
                    sqlQuery = "INSERT INTO data(Number, Name, Address, Position_Lat, Position_Lng, Status, Bike_Stands, Available_Bike_Stands, Available_bikes, Last_Update) \
                    VALUES('%d', '%s', '%s', '%f', '%f', '%s', '%d', '%d', '%d', '%d')" % \
                    (number, name, address, position_lat, position_lng, status, bike_stands, available_bike_stands, available_bikes, last_update)
                    
                    cursor.execute(sqlQuery)
                    
                    conex.commit()
        
                pass
            except:
                print("except")
                pass
            
        else:
            print("api connection failed")
            # Error occurred 
            pass
        
        
    
        time.sleep(300)

        
    conex.close()
    print("connection closed")
    
main()
     

