from collections import defaultdict
import subprocess
import os
import csv


def retrieve_data(host : str, user : str, pwd : str, port : int = 623) -> str:
    try : 
        command = f'ipmitool -I lanplus -H {host} -p {port} -U {user} -P {pwd} sdr elist full > temp.csv'
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
        return result.stdout
    
    except Exception as e :
        return e


def process_data(data) -> dict :
    with open('temp.csv') as csv_file : 
        csv_reader = csv.reader(csv_file, delimiter='|')
        for row in csv_reader: 
            print(row)


process_data(retrieve_data('192.168.1.66', 'root', 'calvin'))
