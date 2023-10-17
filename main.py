__author__ = "Andréa Joly"
__date__ = "15-10-2023"

import time


"""
from apscheduler.schedulers.blocking import BlockingScheduler

from functions import retrieve

if __name__ == "__main__":
    scheduler = BlockingScheduler(timezone='Europe/Paris')
    scheduler.add_job(retrieve, "interval", seconds=60)
    scheduler.start()
"""


from retrieve import retrieve_data

while (True) : 
    retrieve_data('192.168.1.66', 'root', 'calvin')
    time.sleep(600)
