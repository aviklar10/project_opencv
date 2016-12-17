#!/bin/bash
LOG="/var/co/project_opencv/logs/task.log"
#. $HOME/.bashrc
cd "$(dirname "$0")"
pgrep -f celery | xargs kill -9
# need to define concurrency according to number of required processes.
nohup celery -Q resize_api -A _celery worker --loglevel=INFO --concurrency=5 >> $LOG &
