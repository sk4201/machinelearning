import cv2

#starting the camera

cap=cv2.VideoCapture(0)
#                   first camera
while cap.isOpened() :
    status,frame=cap.read()


#now showing
    # converting image into gray scale
    grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    print(frame.shape)
    # now we can drawn al those patterns
    #line
    cv2.line(frame,(0,0),(200,300),(0,0,255),3)
    #rectangle
    cv2.rectangle(frame,(50,50),(150,300),(0,0,255),2)
     #circle
    cv2.circle(frame,(200,300),100,(13,14.123),2)
      #text writing
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'ADHOC',(10,50), font, 2,(0,2,55),2,cv2.LINE_AA)


    cv2.imshow('live',frame)

    cv2.imshow('livegray',grayimg)
    
 
    if cv2.waitKey(0) & 0xff == ord('q') :
        break

cv2.destroyWindow('live')
cv2.destroyAllWindows() # this will destroy all the window

#to close camera
cap.release()
