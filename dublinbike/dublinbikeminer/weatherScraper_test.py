import requests
import json

link = "http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=73281f45f2eec1f97e90acdcbacaf4ee"

r = requests.get(link)
jTxt = json.loads(r.text)

count = 0

for row in jTxt['list']:
    
    print(row['dt'])
    count+=1

print(count)