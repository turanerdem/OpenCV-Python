# İki Görüntü Yükle:
img1 = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')
# Sol Üst Köşeye Görüntüyü Yerleştirmek İstiyoruz:
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
# Şimdi Bir Maske Oluşturuyoruz, Ve O Maskenin Tersini Oluşturuyoruz:
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
# ROI Üzerindeki Siyah Bölge İçin:
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
# Görüntü Bölgesinin Alımı:
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
# Ana Resmi İşliyoruz:
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
