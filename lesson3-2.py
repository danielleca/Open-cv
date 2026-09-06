import cv2
import numpy as np

image = np.full((500, 800, 3), (230, 216, 173), dtype = np.uint8)

#Triangle

points = np.array(
    [
        [250, 100],
        [100, 400],
        [400, 400]
    ]
)

points = points.reshape((-1, 1, 2))

cv2.fillPoly(image, [points], (0, 255, 0))
cv2.imshow("Filled Triangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Pentagon

points = np.array([
    [250, 80],
    [100, 200],
    [150, 400],
    [350, 400],
    [400, 200]
])

cv2.fillPoly(image, [points], (0, 255, 255))

cv2.imshow("Pentagon", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Diamond

points =np.array([
    [250, 100],
    [100, 250],
    [250, 400],
    [400, 250]
])

cv2.fillPoly(image, [points], (255, 255, 0))

#Arrow

cv2.arrowedLine(image, (50, 250), (450, 250), (255, 0, 255), 5)

cv2.imshow("Diamond", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

