import python.darknet
import os, sys
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
net = python.darknet.load_net(b"/home/manoj/Downloads/darknet-master/cfg/yolov3.cfg",b"/home/manoj/Downloads/darknet-master/yolov3.weights",0)
meta = python.darknet.load_meta(b"/home/manoj/Downloads/darknet-master/cfg/coco.data")
folder = "/home/manoj/Desktop/test_data/"
files = os.listdir(folder)
for f in files:
    flag =2
    if f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png"):
    	path = bytes(os.path.join(folder, f), encoding="utf-8")
    r = python.darknet.detect(net, meta, path)
    #name = r[0][0]
    #predict = r[0][1]
    k =0 
    for i in r:
        k+=1
        if i[0] ==b'person' and i[1]>.95:
            flag = 0
            for j in range(k,len(r)):
                if r[j][0]==b'person':
                    flag==1
                    saving_path = "/home/manoj/anaconda3/spyder_code/assignment_2/data_/atul/1/data/new4/"+f
                    save_file = open(saving_path, 'w')
                    image = Image.open(path)
                    image.save(saving_path)
                    save_file.close()
                    break
            if(flag==0):
                x = i[2][0] 
                y = i[2][1]
                w = i[2][2]
                z = i[2][3]
                x_max = (2*x+w)/2
                x_min = (2*x-w)/2
                y_min = (2*y-z)/2
                y_max = (2*y+z)/2
                image = Image.open(path)
                cropped = image.crop((x_min, y_min, x_max, y_max))
                saving_path = "/home/manoj/anaconda3/spyder_code/assignment_2/data_/atul/1/data/new3/"+f
                save_file = open(saving_path, 'w')
                plt.imshow(cropped)
                cropped.save(saving_path)
                save_file.close()
    if flag ==2: 
        saving_path = "/home/manoj/anaconda3/spyder_code/assignment_2/data_/atul/1/data/new4/"+f
        save_file = open(saving_path, 'w')
        image = Image.open(path)
        image.save(saving_path)
        save_file.close()