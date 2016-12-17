installations:
sudo apt-get install rabbitmq-server
sudo pip install celery

running celery:
# need to edit the concurrency according to the required workers.
bootstrap.sh

unless you use the video: SampleVideo_1280x720_1mb.mp4  - 
download from http://www.sample-videos.com/video/mp4/720/big_buck_bunny_720p_1mb.mp4 and locate under tmp/ folder
usage: python send test_program.py num_of_instances time_sleep video_file
# python send test_program.py 3 30 SampleVideo_1280x720_1mb.mp4