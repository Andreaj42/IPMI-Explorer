import subprocess
import pandas as pd
import numpy as np
from datetime import datetime

   
def retrieve_data(host : str, user : str, pwd : str, port : int = 623):
    command = f"ipmitool -I lanplus -H {host} -p {port} -U {user} -P {pwd} sdr elist full > temp.csv"
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    command = f"sed -i '1iname | ID | status | group | metric' temp.csv"
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)

    df = pd.read_csv('temp.csv', delimiter='|')
    df.columns = df.columns.str.strip()
    df = df.replace({' ':''}, regex=True)
    df['unit'] = df['metric'].str.extract(r'([^0-9.,]+)$')
    df['metric'] = df['metric'].str.replace(r'[^\d,.]', '', regex=True)
    df['metric'] = df['metric'].replace('', np.nan)
    df = df.dropna(subset=['metric'])
    date = datetime.strftime(datetime.now(), '%m-%d-%Y %H:%M:%S')
    df['date'] = date
    df.to_csv(f'data/{date}.csv', index=False)


