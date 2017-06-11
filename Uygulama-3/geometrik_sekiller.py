import numpy as np
import cv2

# Siyah bir zemin oluşturuyoruz. İlk uygulama da öğrendiğimiz cv2.imread() komutu ile görüntü üzerine de yapabiliriz aynı işlemi..

img = np.zeros((600,730,3), np.uint8)

#İlk uygulama da öğrendiğimiz cv2.imread() komutu ile görüntü üzerinde de yapabiliriz aynı işlemleri. Bir aşağıdaki komut satırından img önündeki "#" silerek aynı işlemi görüntü üzerinde yapabilirsiniz.

#img = cv2.imread('esogu.jpg', cv2.IMREAD_COLOR)

# 5 piksel kalınlığında diagonal mavi bir çizgi çizdiriyoruz. Çizginin özellikleri size kalmış, 8 bitlik değerleri istediğiniz gibi değiştirebilirsiniz.

# Çizgi Çalışması !!!
cv2.line(img,(0,0),(511,511),(255,0,0),5)

# Dikdörtgen Çizimi:
cv2.rectangle (img,(384,0), (510,511), (0,255,0), 3)

# Daire Çizimi:
cv2.circle (img,(447,63),63,(0,0,255),-1)

# Elips Çizimi:
cv2.ellipse(img,(256,256), (100,50),0,0,180,255,-1)

# Poligon Çizimi:

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

#Beyaz renkte Esogu-EEE yazdıracağız.
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Esogu-EEE', (10,500), font, 4, (255,255,255),2,cv2.LINE_AA)

# Görüntünün Oluşturulduğu Pencereyi Kapatmak için Herhangi bir Tuşu bekle

cv2.imshow('Geometrik-Sekiller',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
