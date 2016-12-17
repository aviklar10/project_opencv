"""
cd ~projects/prospector
NUMBER_WORKERS=5 ; for ((c=0;c<$NUMBER_WORKERS;c++)) ; do nohup celery -Q scraper -A scraper worker -l info >>
/var/log/celery_pixel.log & done

run celery by :
celery -Q web -A web._celery worker --loglevel=INFO --concurrency=1
celery -Q csvupload -A web._celery worker --loglevel=INFO --concurrency=1
celery worker -A web._celery  --loglevel=INFO --concurrency=1 -B -l info
celery -Q emailverifier -A web._celery worker --loglevel=INFO --concurrency=1
"""
from __future__ import absolute_import
from celery import Celery

# CELERY_IMPORTS = ("tasks",)

app = Celery('tasks', broker='amqp://', backend='amqp://', include=['tasks'])

# app.conf.update(
#     CELERY_ACCEPT_CONTENT=['pickle', 'myser'],
#     CELERY_TASK_SERIALIZER='myser',
#     CELERY_RESULT_SERIALIZER='pickle'
#
# )

if __name__ == '__main__':
    app.start()
