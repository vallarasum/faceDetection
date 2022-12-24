

import cv2
trainedDataset=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video=cv2.videoCapture(0)
while (True):
 success,frame=video.read()

 if success==True:
   gray_image =cv2.cvtcolor(frame,cv2.COLOR_BGR2GRAY)
   faces=trainedDataset.detectMultiScale(gray_image)

for x,y,w,h in faces:
 cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
 cv2.imshow('vide',frame)
 cv2.waitkey(1)
else:
 print(videodetected)


