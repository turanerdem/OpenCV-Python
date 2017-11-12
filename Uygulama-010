import cv2
import numpy as np,sys
A = cv2.imread('elma.jpg')
B = cv2.imread('portakal.jpg')
# A için Gauss Piramidi
G = A.copy()
gpA = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# B için Gauss Piramidi
G = B.copy()
gpB = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpB.append(G)
# A için Laplace Piramidi
lpA = [gpA[5]]
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)
# B için Laplace Piramidi
lpB = [gpB[5]]
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)
# SAĞ Ve SOL Yarım Kürelerini Ekliyoruz
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))
    LS.append(ls)
# Şimdi Yeniden Oluşturma
ls_ = LS[0]
for i in xrange(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# Her Yarım Küreye Bağlantı:

real = np.hstack((A[:,:cols/2],B[:,cols/2:]))
cv2.imwrite('Piramid_Karistirma.jpg',ls_)
cv2.imwrite('Direkt_Karistirma.jpg',real)
