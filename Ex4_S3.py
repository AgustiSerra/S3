import os

os.system('ffmpeg -i bbb.mp4 -v 0 -vcodec mpeg4 -f mpegts udp://192.168.1.64:8080')
#os.system('ffmpeg -i bbb.mp4 -v 0 -vcodec mpeg4 -f mpegts udp://192.168.1.64:23000')
