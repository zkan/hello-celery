import time

from celery import Celery
from celery import shared_task


app = Celery('gatuk', broker='redis://localhost:6379')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, hello.s('Kan'), name='add every 10')


@shared_task
def hello(name):
    time.sleep(5)
    return f'Hello, {name}'
