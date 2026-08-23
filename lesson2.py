# Arithematic Operations on Image

# Addition

import cv2

image1 = cv2.imread("img1.png")
image2 = cv2.imread("img2.png")

weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)

cv2.imshow("Weighted Image", weightedSum)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Subtraction

sub = cv2.subtract(image1, image2)
cv2.imshow("Subtracted Image", sub)
cv2.waitKey(0)
cv2.destroyAllWindows


# Resizing Image

resized = cv2.resize(image2, (500, 500))
cv2.imshow("Reduced Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()