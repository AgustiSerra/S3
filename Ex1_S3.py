import os

os.system('ls')
os.system('cd Desktop')

#using the previous seminar functions for cuting the video and transforming it to the 4 different qualities
os.system('ffmpeg -ss 00:04:18 -i bbb.mp4 -to 00:00:10 -c copy bbb10sec.mp4')

os.system('ffmpeg -i bbb10sec.mp4 -filter:v scale=720:-2 -c:a copy bbb10sec720.mp4')
os.system('ffmpeg -i bbb10sec.mp4 -filter:v scale=480:-2 -c:a copy bbb10sec480.mp4')
os.system('ffmpeg -i bbb10sec.mp4 -filter:v scale=360:240 -c:a copy bbb10sec360x240.mp4')
os.system('ffmpeg -i bbb10sec.mp4 -filter:v scale=160:120 -c:a copy bbb10sec160x120.mp4')

#os.system('ffmpeg -i bbb10sec720.mp4 -vcodec libvpx -qmin 0 -qmax 50 -crf 10 -b:v 1M -acodec libvorbis 720vp8.mp4')
#os.system('ffmpeg -i bbb10sec720.mp4 -c:v libvpx -b:v 1M -c:a libvorbis 720vp8.mp4')
os.system('ffmpeg -i bbb10sec720.mp4 -c:v libvpx -qmin 0 -qmax 50 -crf 5 -b:v 1M -c:a libvorbis 720vp8.webm')
os.system('ffmpeg -i bbb10sec480.mp4 -c:a copy -c:v vp9 -r 30 480vp9.mp4')
#os.system('ffmpeg -i bbb10sec360x240.mp4 -an -vcodec libx264 -crf 23 360x240h264.mkv')
os.system('ffmpeg -i bbb10sec360x240.mp4 -c:v libx264 -preset slow -crf 22 -c:a copy 360x240h264.mp4')
#os.system('ffmpeg -i bbb10sec160x120.mp4 -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental 160x120av1.mp4')
