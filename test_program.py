
import time, sys

from tasks import run_resize_task

QUEUE = 'resize_api'


def run_resize(instance, m, path):
    run_resize_task.apply_async((0, path,), queue=QUEUE)
    for i in range(1, instance+1):
        time.sleep(m)
        run_resize_task.apply_async((i, path,), queue=QUEUE)

path='SampleVideo_1280x720_1mb.mp4'
if len(sys.argv) > 1:
    instance = sys.argv[1]
    time_sleep = sys.argv[2]
    video_path = sys.argv[3] if len(sys.argv) >3 else path
else:
    instance=5
    time_sleep = 5
    video_path = 'SampleVideo_1280x720_1mb.mp4'
run_resize(instance,time_sleep, video_path)