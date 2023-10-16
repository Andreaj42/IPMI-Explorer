__author__ = "Andréa Joly"
__date__ = "15-10-2023"

from apscheduler.schedulers.blocking import BlockingScheduler

from functions import retrieve

if __name__ == "__main__":
    scheduler = BlockingScheduler(timezone='Europe/Paris')
    scheduler.add_job(retrieve, "interval", seconds=60)
    scheduler.start()