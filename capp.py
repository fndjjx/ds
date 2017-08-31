from celery import Celery
from celery import group
from celery.result import allow_join_result


broker = 'redis://127.0.0.1:6379'
backend = 'redis://127.0.0.1:6379'


CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
CELERY_RESULT_SERIALIZER = 'pickle'


app = Celery('tasks', broker=broker, backend=backend, task_serializer='pickle')
app.conf.update(CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml'], CELERY_RESULT_SERIALIZER = 'pickle')



