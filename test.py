from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)
if 'ipmi_metrics' not in client.get_list_database():
    client.create_database('ipmi_metrics')

client.switch_database('ipmi_metrics')

query = 'SHOW MEASUREMENTS'

query = 'SELECT * FROM voltage LIMIT 10' 

result = client.query(query)

data = [
    {
        "measurement": "voltage", 
        "fields": {
            "value": 12.0  
        }
    }
]

client.write_points(data)

for measurement in result:
    for point in measurement:
        print(point)



#print(client.get_list_database())