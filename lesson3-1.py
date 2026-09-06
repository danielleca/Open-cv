import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype= "uint8")

cv2.line(img, (50, 50), (450, 50), (255, 0, 0), 3)
cv2.rectangle(img, (50, 100), (200, 250), (0, 255, 0), -1)
cv2.circle(img, (350, 200), 80, (0, 0, 255), -1)
cv2.putText(img, "Open CV Drawing", (20, 450),
            cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 255, 255), 2,
            cv2.LINE_AA)
cv2.imshow("Drawing Example", img)
cv2.waitKey(0)
cv2.destroyAllWindows()