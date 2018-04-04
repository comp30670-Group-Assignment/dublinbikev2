from extractorv1 import *
import time
import json

new_conex = Extractor()

while True:
    
    fhb = open("/home/hugh/git/dublinbikev2/dublinbike/dublinbikeflask/static/av_bike.json", "w")
    fhs = open("/home/hugh/git/dublinbikev2/dublinbike/dublinbikeflask/static/av_stand.json","w")
    
    new_conex.avg_available_bike()
    new_conex.avg_available_stand()
    
    avg_bike = new_conex.avg_available_bike_dict
    avg_stand = new_conex.avg_available_stand_dict
    
    avg_bike_json = json.dumps(avg_bike)
    avg_stand_json = json.dumps(avg_stand)
    
    print("writing")
    fhb.write(avg_bike_json)
    
    fhs.write(avg_stand_json)
    fhb.close
    fhs.close
    print("sleeping")
    time.sleep(86400)
    
    
    
    