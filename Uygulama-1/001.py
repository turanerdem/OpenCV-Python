import numpy as np
import cv2
img = cv2.imread('esogu-eee.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # ESC tuşu ile çıkış yapar
    cv2.destroyAllWindows()
elif k == ord('s'): # 's' tuşu ile resmi kaydeder
    cv2.imwrite('esogu-eee.png',img)
    cv2.destroyAllWindows()
