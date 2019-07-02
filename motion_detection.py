#!/usr/bin/python3
#motion Dectector
import cv2
#start camera

cap=cv2.VideoCapture(0)

tp1=cap.read()[1] 
tp1=cap.read()[1] 
tp1=cap.read()[1] 

#to make more perfect we convert image in greyscale

grey1=cv2.cvtColor(tp1.cv2.COLOR_BGR2GRAY)
grey2=cv2.cvtColor(tp2.cv2.COLOR_BGR2GRAY)
grey3=cv2.cvtColor(tp3.cv2.COLOR_BGR2GRAY)

#now creating image difference

def image_diff(x,y,z):
	#difference between x,y --grey1 and grey2  --d1
	d1=cv2.absdiff(x,y)
	#difference between y,z --grey2 and grey3  --d1
	d1=cv2.absdiff(y,z)

	#absolute difference between d1 and d2
	finalimg=cv2.bitwise_and(d1,d2)
	return finalimg

#now apply function

while cap.isOpened():
	status, frame=cap.read()
	motionimg=image_diff(grey1,grey2,grey3)
	#replacing image frame

	grey1=grey2
	grey2=grey3
	grey3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#cv2.imshow ('live',frame)
	cv2.imshow('motion',motionimg)
	if cv2.waitKey(10) & 0xff== ord('q'):
		break


cv2.destroyAllWindows()
cap.release()
