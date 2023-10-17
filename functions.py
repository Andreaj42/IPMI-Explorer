from collections import defaultdict
import subprocess
import os
import csv
import pandas as pd
import numpy as np


class IPMIConnector:
    def __init__(self, host : str, user : str, pwd : str, port : int = 623):
        self.host = host
        self.user = user 
        self.password = pwd
        self.port = port
        self
    
    def retrieve_data(self) -> pd.DataFrame:
        try : 
            command = f"ipmitool -I lanplus -H {self.host} -p {self.port} -U {self.user} -P {self.pwd} sdr elist full > temp.csv"
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
            command = f"sed -i 'name | ID | status | group | metric' temp.csv"
            self.df = pd.read_csv("temp.csv", delimiter="|")

            return result.stdout
        except Exception as e:
            return e
    
    def sanitize_data(self):
        df = pd.read_csv("temp.csv", delimiter="|")
        df.columns = df.columns.str.strip()
        df = df.replace({' ':''}, regex=True)
        df['unit'] = df['metric'].str.extract(r'([^0-9.,]+)$')
        df['metric'] = df['metric'].str.replace(r'[^\d,.]', '', regex=True)
        df['metric'] = df['metric'].replace('', np.nan)
        df = df.dropna(subset=['metric'])



def sanitize_data():




    print(df.head(20))
    print(df.columns)


def process_data():
    with open('temp.csv','w') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='|')
        for row in csv_reader:
            send_data(row)
            for item in row:
                item = item.replace(" ", "")
                print(item)
            print(row)


sanitize_data()

#process_data(retrieve_data('192.168.1.66', 'root', 'calvin'))
