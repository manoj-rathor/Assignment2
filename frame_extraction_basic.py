import cv2
import numpy as np
import os
from natsort import natsorted,humansorted,ns
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
'en_US.UTF-8'
cap = cv2.VideoCapture('/home/manoj/anaconda3/spyder_code/assignment_2/atul/1/1.mp4') 
try:
    if not os.path.exists('/home/manoj/anaconda3/spyder_code/assignment_2/atul/1/data1'):
        os.makedirs('/home/manoj/anaconda3/spyder_code/assignment_2/atul/1/data1')
except OSError:
    print ('Error: Creating directory of data')

currentFrame =6000

ret, frame = cap.read()
ret=True

x=0
while ret:
    # Capture frame-by-frame
    ret, frame = cap.read()
    x=x+1
    
    if x%5==0:  #extraxt every 5th frame
           # Saves image of the current frame in jpg file
           name = '/home/manoj/anaconda3/spyder_code/assignment_2/atul/1/data1/' + str(currentFrame) + 'x.jpg'
           print ('Creating...' + name)
           cv2.imwrite(name, frame)
       
           # To stop duplicate images
           currentFrame += 1

# When everything done, release the capture
cap.release()
list = os.listdir('/home/manoj/anaconda3/spyder_code/assignment_2/atul/1/data1')
x=len(list)