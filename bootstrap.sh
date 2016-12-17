#!/bin/bash

. $HOME/.bashrc

pgrep -f celery | xargs kill -9
# need to define concurrency according to number of required processes.
nohup celery -Q resize_api -A _celery worker --loglevel=INFO --concurrency=5
