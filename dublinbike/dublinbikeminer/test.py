import requests
import json
import time
#import datetime
import mysql.connector
from numbers import Number
import re
from h5py._hl import dataset

def main():
    
    conex = mysql.connector.connect(user='root', password='Rugby_777', database='dublinbikes', host='0.0.0.0')
    
    cursor = conex.cursor()
    
    query = "SELECT * FROM data;"
    
    cursor.execute(query)
    
    output = cursor.fetchall()

    for row in output:
        
        date = 
    
    
if __name__ == "__main__":
    main()