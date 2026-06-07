import cv2
img=cv2.imread('deer.webp',cv2.IMREAD_COLOR)
cv2.imshow('deer image',img)
gray=cv2.imread('deer.webp',0)
cv2.imshow('black and white image',gray)
cv2.imwrite('bwdeer.png',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()