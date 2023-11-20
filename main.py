__author__ = "Andréa Joly"
__date__ = "15-10-2023"

from apscheduler.schedulers.blocking  import BlockingScheduler
from datetime import datetime

from config.config import SCAN_INTERVAL
from lib.retrieve import retrieve

if __name__ == "__main__":
    scheduler = BlockingScheduler(timezone='Europe/Paris')
    job = scheduler.add_job(retrieve, "interval", seconds=SCAN_INTERVAL)
    try:
        job.modify(next_run_time=datetime.now())
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown()