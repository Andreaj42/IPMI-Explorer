from logging import INFO, Formatter, StreamHandler, getLogger
from traceback import format_exc
from datetime import datetime

import subprocess
import pandas as pd
import numpy as np

from lib.database import DatabaseConnector

from config.config import IPMI_HOST, IPMI_PORT, IPMI_USER, IPMI_PASSWORD


class IPMIConnector():
    
    def __init__(self) -> None:
        self.logger = self.__configure_logger()
        self.host = IPMI_HOST
        self.port = IPMI_PORT
        self.user = IPMI_USER 
        self.password = IPMI_PASSWORD
        self.db = DatabaseConnector()

    def __configure_logger(self):
        logger = getLogger(__name__)

        if not logger.hasHandlers():
            logger.setLevel(INFO)
            formatter = Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch = StreamHandler()
            ch.setFormatter(formatter)
            logger.propagate = False
            logger.addHandler(ch)

        return logger
        
    def __sanitize_data(self, df : pd.DataFrame) -> pd.DataFrame:
        df.columns = df.columns.str.strip()
        df = df.replace({' ':''}, regex=True)
        df['unit'] = df['metric'].str.extract(r'([^0-9.,]+)$')
        df['metric'] = df['metric'].str.replace(r'[^\d,.]', '', regex=True)
        df['metric'] = df['metric'].replace('', np.nan)
        df = df.dropna(subset=['metric'])
        df['metric'] = df['metric'].str.replace(",", '.')
        self.logger.info(f"Affichage du df nettoyé:\n {df.head()}")
        return df
        
    def get_metrics(self) -> pd.DataFrame:
        command = f"ipmitool -I lanplus -H {self.host} -p {self.port} -U {self.user} -P {self.password} sdr elist full > temp.csv"
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
        command = f"sed -i '1i\ name | ID | status | group | metric' temp.csv"
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
        df = pd.read_csv("temp.csv", delimiter="|")
        self.logger.info(f"Affichage du df:\n {df.head()}")
        command = f"rm temp.csv"
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
        df = self.__sanitize_data(df)
        return df

    def insert_data(self):
        try:
            df = self.get_metrics()
            for _, row in df.iterrows():
                values =(row['name'], row['ID'], row['group'], row['metric'], row['unit'], datetime.now())
                self.db.insert_new_metric(values)
        except:
            self.logger.critical(
                "Impossible d'insérer une nouvelle metric.", exc_info=format_exc())
            exit(-1)