import time

from celery import Celery


app = Celery('tasks', broker='redis://localhost:6379')


@app.task
def hello(name):
    time.sleep(5)
    return f'Hello, {name}'
