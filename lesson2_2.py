import cv2
import numpy as np

image = cv2.imread("deer.webp")

# EROSION

kernel = np.ones((15,15), np.uint8)
eroded_image = cv2.erode(image, kernel)
cv2.imshow("Eroded Image", eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#BLURRING OF AN IMAGE

#GAUSSIAN BLUR

image2 = cv2.imread("img2.png")
gaussian = cv2.GaussianBlur(image2, (7,7), 0)
cv2.imshow("Gaussian Blur", gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Median Blur

image3 = cv2.imread("img2.png")
median = cv2.medianBlur(image3, 5)
cv2.imshow("Median Blur", median)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Bilateral Filter

image4 = cv2.imread("img2.png")
bilateral = cv2.bilateralFilter(image4, 9, 75, 75)
cv2.imshow("Bilaterial Filter", bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()