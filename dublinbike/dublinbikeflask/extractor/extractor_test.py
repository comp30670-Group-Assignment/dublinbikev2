from extractorv1 import *

new_conex = Extractor()

new_conex.getLatAndLong()

fh = open("stations.json", "w")

fh.write(new_conex.json)

output = new_conex.test()



#new_conex.avg_available_bike()

#print(new_conex.avg_available_bike_dict)

#new_conex.avg_available_stand()

#print(new_conex.avg_available_stand_dict)

#print(new_conex.avg_available_bike_dict['BARROW STREET'][0])

#print(new_conex.avg_available_stand_dict['BARROW STREET'][0])



