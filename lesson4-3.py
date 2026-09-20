# Coin detection

import cv2
import numpy as np

img = cv2.imread("coins.jpg")

if img is None:
    print("Image not found!")
    exit()

output = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (9, 9), 2)

circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp = 1.2,
    minDist = 80,
    param1 = 100,
    param2 = 40,
    minRadius = 30,
    maxRadius = 120
)

coin_count = 0

if circles is not None:
    circles = np.uint16(np.around(circles))
    coin_count = len(circles[0])

    for (x, y, r) in circles[0]:
        cv2.circle(output, (x, y), r, (0, 255, 0), 3)
        cv2.circle(output, (x, y), 3, (0, 0, 255), -1)

cv2.putText(
    output,
    "Total Coins :"+str(coin_count),
    (20, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.2,
    (0, 255, 0),
    3
)

display = cv2.resize(output, (1000, 700))

cv2.imshow("coin counter", display)
cv2.waitKey(0)
cv2.destroyAllWindows()