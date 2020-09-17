import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter('Video.avi',fourcc,20.0,(640,480))

while cap.isOpened():
    _,img=cap.read()
    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)
    out.write(img)
    cv2.imshow('img',img)
    if cv2.waitKey(1)==ord('q'):    
        break

cap.release()
out.release()
cv2.destroyAllWindows()