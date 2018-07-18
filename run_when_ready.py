'''
Runs Script When Launch Time!
'''
import schedule
import time


launch_day = ""
launch_time = "00:15"

def job(t):
    print("I'm working...", t)
    return

schedule.every().day.at(launch_time).do(job, "It is 01:00")

while True:
    schedule .run_pending()
    time.sleep(60) #wait one minute
