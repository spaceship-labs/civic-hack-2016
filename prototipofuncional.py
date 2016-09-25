#!/usr/bin/python
import time
import numpy as np
import Image
import cv2
from PIL import Image
import pytesseract
import urllib2
import sys
import os

fecha= (time.strftime("%d:%m:%y-%H:%M:%S"))
host = "192.168.1.134:8080"
if len(sys.argv)>1:
    host = sys.argv[1]

hoststr = 'http://' + host + '/video'
print 'Streaming '
stream=urllib2.urlopen(hoststr)

bytes=''
while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        cv2.imshow(hoststr,i)
        #if cv2.waitKey(1) ==27:
        #    exit(0)
        if cv2.waitKey(1) & 0xFF == ord('s'):
           cv2.imwrite( "foto.jpg", i )
           os.system("alpr -c qr -p qr foto.jpg | head -n 2 | tail -n 1 | cut -b 7-14 ")
           os.system("mkdir Matricula")
           #os.system("alpr -c qr -p qr foto.jpg ")
           os.system("streamer -t 0:0:10 rj -c /dev/video0 -f rgb24 -r 24  -o  Matricula/%s.avi" %fecha)
           break
