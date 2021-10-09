from flask_apscheduler import APScheduler
import datetime

scheduler = APScheduler()

# cron examples
@scheduler.task('cron', id='do_job_2', minute='*')
def job2():
    print(str(datetime.datetime.now()) + ' Job 2 executed')

