import numpy as np
import cv2
cap = cv2.VideoCapture(0) # harici bir kamerada i=0 yerine i=1,2,3..vs kullanabilirsiniz
while(True):

#Çerçeveler halinde görüntü yakalar
    ret, frame = cap.read()

#Üzerinde işlem yapacağımız çerçeve buraya gelsin
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#Sonuç Çerçeveyi Görüntüleme:
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Herşey yolunda gitti ise dükkanı kapatabiliriz :)
cap.release()
cv2.destroyAllWindows()
