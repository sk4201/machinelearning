import cv2

#starting the camera

cap=cv2.VideoCapture(0)
#                   first camera
# to check camera is started or not

if cap.isOpened() :
    print("camera is ready to take picture")
else :
    print("to check web cam drivers")


#  now we can take  read input from camera

statu,img=cap.read() # it will take first picture
#now showing
cv2.imshow('live image',img)

# saving image
+cv2.imwrite('new.jpg',img)
cv2.waitKey(0)

#to close camera
cap.release()
