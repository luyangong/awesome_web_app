from celery.utils.timer2 import Schedule
from time import time, sleep
from celery import task
from threading import Timer
from celery import Celery

def hello():
    print("hello, world")

# t = Schedule()
# print(time())
# x = t.call_after(3, hello)  # after 30 seconds, "hello, world" will be printed
# sleep(5)
#
# @task
# def add(x, y):
#     return x + y
#
# result = add.delay(4, 4)
# print(result)

# t = Timer(3.0, hello)
# t.start()  # after 30 seconds, "hello, world" will be printed

app = Celery()
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://localhost:6379/0'
@app.task
def add(x, y): return x + y

if __name__ == '__main__':
    app.worker_main()