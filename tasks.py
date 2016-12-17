from __future__ import absolute_import
from _celery import app
import sys, os, json, logging
from video_frames import save_video_frames
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../")
os.chdir(os.path.dirname(os.path.realpath(__file__)) + "/../../")
"""
Running the celery worker server:
celery -A tasks worker --loglevel=info
"""


@app.task
def run_resize_task(video_instance, video_path):
    logging.debug("new run_resize_task job")
    save_video_frames(video_instance, video_path)
