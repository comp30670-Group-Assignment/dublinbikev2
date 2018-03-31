import requests
import json
import time

# Import MySQl
from mysql.connector import (connection, cursor)

def main():
    
    # Connection to local database
    conex = connection.MySQLConnection(user='hugh', password='password', host='0.0.0.0', database='dublinbikes')
    # MySQL object
    cursor = conex.cursor()
    
    
    while True:

        link = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&&apiKey=4dc48c410fefd7a42d52cdc4a9c6eb7ce0f67ae0"
        
        r = requests.get(link)
        jTxt = json.loads(r.text)
        
        if r.status_code == 200:
            
            try:
        
                number = jTxt['number']
                name = jTxt['name']
                address = jTxt['address']
                position_lat = jTxt['position']['lat']
                position_lng = jTxt['position']['lng']
                bike_stands = jTxt['bike_stands']
                status = jTxt['status']
                available_bike_stands = jTxt['available_bike_stands']
                available_bikes = jTxt['available_bikes']
                last_update = jTxt['last_update']
                
                
                sqlQuery = "INSERT INTO dublinBikes(Number, Name, Address, Position_Lat, Position_Lng, Status, Bike_Stands, Available_Bike_Stands, Available_bikes, Last_Update) \
                VALUES('%d', '%s', '%s', '%f', '%f', '%s', '%d', '%d', '%d', '%d')" % \
                (number, name, address, position_lat, position_lng, status, bike_stands, available_bike_stands, available_bikes, last_update)
                
                cursor.execute(sqlQuery)
                
                cursor.commit()
        
                pass
            except:
                pass
            
        else:
            print("api connection failed")
            # Error occurred 
            pass
        
        
    
        time.sleep(300)

        
    conex.close()
    print("connection closed")
    
main()
     

