from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)
if 'ipmi_metrics' not in client.get_list_database():
    client.create_database('ipmi_metrics')

def send_data(file_path : str) :
    client = InfluxDBClient(host='localhost', port=8086)
    client.switch_database('ipmi_metrics')

    data = [
        {
            "measurement": "voltage", 
            "fields": {
                "value": 12.0
            }
        }
    ]

    client.write_points(data)

query = 'SELECT * FROM voltage LIMIT 10' 
query = 'SHOW MEASUREMENTS'
result = client.query(query)

for measurement in result:
    for point in measurement:
        print(point)

#print(client.get_list_database())