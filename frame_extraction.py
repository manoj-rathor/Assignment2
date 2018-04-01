import cv2
import os
#from natsort import natsorted,humansorted,ns
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
'en_US.UTF-8'
rootdir = '/home/manoj/anaconda3/spyder_code/assignment_2/data'
for subdir, dirs,files in os.walk(rootdir):
    for file in files:
        path = os.path.join(subdir,file)
        path1 = os.path.join(subdir,'data')
        print(path1)
        cap = cv2.VideoCapture(path) 
        try:
            if not os.path.exists(subdir+'/'+'data'):
                os.makedirs(subdir+'/'+'data')
        except OSError:
            print ('Error: Creating directory of data') 
        currentFrame =0
        ret, frame = cap.read()
        ret=True    
        x=0
        while ret:
            # Capture frame-by-frame
            ret, frame = cap.read()
            x=x+1
            if x%10==0:  #extraxt every 5th frame
                # Saves image of the current frame in jpg file
                name = path1+'/'+str(currentFrame) + '.jpg'
                print ('Creating...' + name)
                cv2.imwrite(name, frame)
                # To stop duplicate images
                currentFrame += 1
        #When everything done, release the capture
        cap.release()
        list = os.listdir(path1+'/')
        x=len(list)
        a=0
        for i in sorted(list, key=lambda y: int(y.split('.')[0])):
            a=a+1
            if a>=100 and a<x-100:
                os.remove('data1/'+i)
                #print(i)     


  
