from extractorv1 import *

new_conex = Extractor()

print(new_conex.station_names)

new_conex.getLatAndLong()

fh = open("stations.json", "w")

fh.write(new_conex.json)

print(new_conex.json)

#new_conex.avg_available_bike()

#print(new_conex.avg_available_bike_dict)

#new_conex.avg_available_stand()

#print(new_conex.avg_available_stand_dict)

#print(new_conex.avg_available_bike_dict['BARROW STREET'][0])

#print(new_conex.avg_available_stand_dict['BARROW STREET'][0])



