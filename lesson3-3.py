import cv2
import numpy as np

image = np.zeros((600, 800, 3), dtype= "uint8")

#Moon
cv2.circle(image, (650, 100), 60, (255, 255, 255), -1)

#Mountain 1
mount1 = np.array([
    [50, 400],
    [250, 150],
    [450, 400]
])

cv2.fillPoly(image, [mount1], (100, 100, 100))
cv2.polylines(image, [mount1], True, (255, 255, 255), 3)

#Mountain 2
mount2 = np.array([
    [300, 400],
    [500, 180],
    [750, 400]
])

cv2.fillPoly(image, [mount2], (70, 70, 70))
cv2.polylines(image, [mount2], True, (255, 255, 255), 3)

#Ground

cv2.rectangle(image, (0, 400), (800, 600), (0, 100, 0), -1)

#River

river = np.array([
    [350, 400],
    [450, 400],
    [600, 600],
    [200, 600]
])

cv2.fillPoly(image, [river], (255, 100, 0))

#Tree trunk

cv2.rectangle(image, (100, 300), (140, 450), (42, 42, 165), -1)

#Tree leaves

cv2.circle(image, (120, 270), 70, (0, 150, 0), -1)

cv2.circle(image, (70, 310), 50, (0, 150, 0), -1)

cv2.circle(image, (70, 310), 50, (0, 150, 0), -1)

#Bird 1

cv2.line(image, (500, 100), (515, 90), (255, 255, 255), 3)
cv2.line(image, (515, 90), (530, 100), (255, 255, 255), 3)

#Bird 2

cv2.line(image, (400, 150), (415, 140), (255, 255, 255), 3)
cv2.line(image, (415, 140), (430, 150), (255, 255, 255), 3)
