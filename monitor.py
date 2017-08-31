from capp import app
from celery import Celery
import time
from celery.events import EventReceiver
import threading


def my_monitor(app):
    print(app)
    app.control.enable_events()
    state = app.events.State()

    def receive_tasks(event):
        print("aa")
        print(event)
        state.event(event)
        # task name is sent only with -received event, and state
        # will keep track of this for us.
        #task = state.tasks.get(event['uuid'])
        print(state.tasks)
        print(dir(state.tasks["5"]))
        print(state.tasks["5"].state)
        #app.control.terminate(task_id="1")

    def success_tasks(event):
        print("bb")
        state.event(event)
        print(state.tasks["5"].ready)

    def revoke_tasks(event):
        print("cc")
        state.event(event)
        print(state.tasks["5"].state)


    while True:
        with app.connection() as connection:
            print("begin")
            recv = EventReceiver(connection, handlers={
                    'task-received': receive_tasks,
                    'task-succeeded': success_tasks,
                    'task-revoked': revoke_tasks,
            })
            recv.capture(limit=None, timeout=None, wakeup=True)
        time.sleep(8)



my_monitor(app)
