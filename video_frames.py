import sys, logging, os, time
from time import gmtime, strftime

sys.path.append('/usr/local/lib/python2.7/site-packages')
sys.path.remove('/usr/lib/pymodules/python2.7')
import cv2
from datetime import datetime

BASE = '/var/co/project_opencv/tmp/'
LOGGER = "/var/co/project_opencv/logs/task.log"
logging.basicConfig(format='%(asctime)s %(levelname)s   %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', filename=LOGGER, level=logging.INFO)
DEFAULT_RESIZE = (512, 512)

def save_video_frames(video_instance, video_path='tmp/SampleVideo_1280x720_1mb.mp4', resize=DEFAULT_RESIZE):
    start_time = datetime.now()
    print('my video instance = %s' % video_instance)

    folder = BASE + 'vid-instance%d' % video_instance
    if not os.path.exists(folder):
        os.makedirs(folder, 0777)
    cap = cv2.VideoCapture(video_path)
    while not cap.isOpened():
        cap = cv2.VideoCapture(video_path)
        cv2.waitKey(1000)
        print "Wait for the header"
    print('my video path = %s' % video_path)
    pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
    frame_rate = 0
    while True:
        flag, frame = cap.read()
        if flag:
            try:
                cv2.imwrite(folder + "/frame%d.jpg" % frame_rate, cv2.resize(frame, resize))
                frame_rate += 1
                cv2.waitKey()
            except Exception as e:
                logging.ERROR(str(e))

            pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
            print str(pos_frame) + " frames"
        else:
            cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame - 1)
            print "frame is not ready"
            cv2.waitKey(1000)

        if cv2.waitKey(10) == 27:
            break
        if cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
            break
    total_time = datetime.now() - start_time
    logging.info('video - %s completely converted, frame rate is %s, time for conversion = %d seconds' % (video_path, frame_rate, total_time.seconds))


if __name__ == "__main__":
    save_video_frames(1)
