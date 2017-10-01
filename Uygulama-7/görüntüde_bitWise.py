# İki Görüntü Yükle:
res1 = cv2.imread('player.jpg')
res2 = cv2.imread('logo.png')
# Sol Üst Köşeye Görüntüyü Yerleştirmek İstiyoruz:
rows,cols,channels = res2.shape
roi = res1[0:rows, 0:cols ]
# Şimdi Bir Maske Oluşturuyoruz, Ve O Maskenin Tersini Oluşturuyoruz:
res2gray = cv2.cvtColor(res2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(res2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
# ROI Üzerindeki Siyah Bölge İçin:
res1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
# Görüntü Bölgesinin Alımı:
res2_fg = cv2.bitwise_and(res2,res2,mask = mask)
# Ana Resmi İşliyoruz:
dst = cv2.add(res1_bg,res2_fg)
res1[0:rows, 0:cols ] = dst
cv2.imshow('res',res1)
cv2.waitKey(0)
cv2.destroyAllWindows()
