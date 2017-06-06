import numpy as np
import cv2
cap = cv2.VideoCapture(0)

#Codec tanımlama ve VideoWriter nesnesi(object) oluşturma
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,0)
        out.write(frame)
        
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) &amp; 0xFF == ord('q'):
           break
    else:
       break

#Herşey yolunda gitti ise dükkanı kapatabiliriz :)
cap.release()
out.release()
cv2.destroyAllWindows()
