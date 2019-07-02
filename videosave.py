#!/usr/bin/python3

import  cv2
#  staring  camera
cap=cv2.VideoCapture('http://192.168.43.1:8080/video?=')
#  adding  plugin  
plugin=cv2.VideoWriter_fourcc(*'XVID') 
#   saving  video                            width , height  
output=cv2.VideoWriter('class2.avi',plugin,1000,(640,480))

while  cap.isOpened() :
    status,frame=cap.read()
    cv2.imshow('live',frame)
    #   draw  pattern 
    output.write(frame)   #  sending  data  to VideoWrite 
    if  cv2.waitKey(10)   &   0xff  ==  ord('q')  :
        break
cv2.destroyAllWindows()  #   this will destroy all windows 
cap.release()

