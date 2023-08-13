"""
@Time :  2023/5/30 16:49
@Auth :  植树的牧羊人
@desc :  定时任务
"""
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler  # pip install apscheduler==3.6.1

def task(name):
    print('%s告诉你现在时间是:%s'.format(name, datetime.datetime.now()))


# 该任务将会在2022-05-20 13:14:52执行一次
scheduler = BlockingScheduler()
scheduler.add_job(task, 'date', run_date=datetime.datetime(2024, 5, 20, 13, 14, 52), args=['autofelix'], id='task')
scheduler.start()