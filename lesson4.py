import cv2
import numpy as np

img = cv2.imread("eyes.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)

detected_circles = cv2.HoughCircles(
    gray_blurred,
    cv2.HOUGH_GRADIENT,
    dp = 1.2,
    minDist = 100,
    param1 = 100,
    param2= 40,
    minRadius = 30,
    maxRadius = 80
)

if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        cv2.circle(img, (a, b), r, (0, 255, 0), 2)
        cv2.circle(img, (a, b), 2, (0, 0, 255), 3)

cv2.imshow("Detected Circles", img)
cv2.waitKey(0)
cv2.destroyAllWindows()