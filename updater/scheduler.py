from apscheduler.schedulers.blocking import BlockingScheduler

#@sched.scheduled_job('cron', day_of_week='mon-fri', hour=21)
from datetime import datetime
import os
from updater import update
from apscheduler.schedulers.background import BackgroundScheduler



def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update.getZip, 'cron',day_of_week='mon-fri',hour=12 ,minute = 30)
    scheduler.start()
