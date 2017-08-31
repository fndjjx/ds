
from celery import Celery
from celery import group
from celery.result import allow_join_result
from capp import app
import time




@app.task(bind=True)
def add(ctask,x,y):
    print("task")
    print(ctask)
    time.sleep(10)
    return x+y
