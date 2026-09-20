#Blob detection

import cv2
import numpy as np

img = cv2.imread("blobs.jpg")

if img is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY_INV)

params = cv2.SimpleBlobDetector_Params()

params.filterByArea = True
params.minArea = 2000
params.maxArea = 200000

params.filterByColor = True
params.blobColor = 255

params.filterByCircularity = False
params.filterByConvexity = False
params.filterByInertia = False

detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(thresh)

print("Detected blobs:", len(keypoints))

output = cv2.drawKeypoints(
    img,
    keypoints,
    None,
    (0, 0, 255),
    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

cv2.namedWindow("Blob detection", cv2.WINDOW_NORMAL)
cv2.imshow("Blob Detection", output)
cv2.waitKey(0)
cv2.destroyAllWindows()