import os
import cv2
rootdir = '/home/manoj/anaconda3/spyder_code/assignment_2/data'
for subdir, dirs,files in sorted(os.walk(rootdir)):
    for file in files:
        path = os.path.join(subdir,file)
        #path2 =os.path(subdir)         
        print(subdir)
        print(path)
        cap = cv2.VideoCapture(path) 
        try:
            if not os.path.exists(subdir+'data'):
                os.makedirs(subdir+'data')
        except OSError:
            print ('Error: Creating directory of data') 