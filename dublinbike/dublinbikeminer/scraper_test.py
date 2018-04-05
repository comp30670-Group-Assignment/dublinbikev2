import mysql.connector

conex = mysql.connector.connect(user='root', password='Rugby_777', database='dublinbikes', host='0.0.0.0')

cursor = conex.cursor()

dataset_query = "SELECT MAX(data_set_id) FROM data"
    
cursor.execute(dataset_query)

    # Set ID value for each time a fresh set of JSON data is pulled from the API
dataSet = cursor.fetchall()[0][0]

print(dataSet)