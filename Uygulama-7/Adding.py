img1 = cv2.imread('ml.png')
img2 = cv2.imread('opencv-logo.png')

# Görüntünün Karıştırma(Blending) İşlemi:
dst = cv2.addWeighted(img1,0.8,img2,0.2,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
