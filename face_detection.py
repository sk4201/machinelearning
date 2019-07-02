#!/usr/bin/python3

import cv2
#calling classifier

casclf=cv2.CascadeClassifier('face.xml')
casclf1=cv2.CascadeClassifier('eye.xml')
#loading facedata
cap=cv2.VideoCapture('http://192.168.43.1:8080/video?=')

while cap.isOpened():
	status, frame= cap.read()
	#now we can apply classifier in live frame 
	face=casclf.detectMultiScale(frame,1.13,5)     #classifier tuning parameter 
	eye=casclf1.detectMultiScale(frame,1.13,5)     #classifier tuning parameter 
	#print(face)
	for x,y,h,w in face:
		cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2)
#		facedata=frame[x:x+h,y:y+h]
#		cv2.imshow('f', facedata)
		for x,y,h,w in eye:
			cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2)

		
		
	cv2.imshow('face',frame)
	cv2.imshow('eye',frame)
	if cv2.waitKey(10) & 0xff== ord('q'):
		break





cv2.destroyAllWindows()
cap.release()


