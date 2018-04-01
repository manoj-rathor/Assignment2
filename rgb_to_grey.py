import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import os 
print(os.getcwd())
"""def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
img = mpimg.imread('113.jpg')     
gray = rgb2gray(img)    
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.show()
mpimg.imsave('113_grey',gray,cmap='Greys_r')"""
test1 = cv2.imread('113.jpg')
# convert the test image to gray iage as open cv face detector expects gray images
gray_img = cv2.cvtColor(test1,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img,cmap = 'gray') 
def convertToRGB(img): 
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#load cascade classifier training file for haarcascade 
haar_face_cascade = cv2.CascadeClassifier('/home/manoj/anaconda3/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')
#let's detect multiscale (some images may be closer to camera than others) images 
faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5);  
#print the number of faces found 
print('Faces found: ', len(faces))
faces[0,0] = faces[0,0]-50
faces[0,1] = faces[0,1]-20
faces[0,2] = faces[0,2]+153
faces[0,3] = faces[0,3]+153
for (x, y, w, h) in faces:
    cv2.rectangle(test1, (x, y), (x+w, y+h), (0, 255, 0), 2)
    subimage = test1[y:y+h,x:x+h]
#convert image to RGB and show image 
plt.imshow(convertToRGB(test1))
n = convertToRGB(subimage)
plt.imshow(n)
#mpimg.imsave('subimage.jpg')
cv2.imwrite("subimage.jpg",n)