import cv2
import numpy as np

image = cv2.imread("circles.jpg",cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found")
    exit()

_, thresh = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY_INV)

thresh = cv2.GaussianBlur(thresh, (5, 5), 0)

params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 10
params.maxThreshold = 200

params.filterByColor = True
params.blobColor = 255

params.filterByArea = True
params.minArea = 1000
params.maxArea = 50000

params.filterByConvexity = False
params.filterByInertia = False

params.filterByCircularity = True
params.minCircularity = 0.7

detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(thresh)

output = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

output = cv2.drawKeypoints(
    output,
    keypoints,
    None,
    (0, 0, 255),
    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

number_of_blobs = len(keypoints)
print("Number of blobs detected: ", number_of_blobs)

cv2.putText(
    output,
    "Blobs Detected: "+str(number_of_blobs),
    (20, 40),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (0, 255, 0),
    2
)

display = cv2.resize(output, (900, 600))
cv2.imshow("Blob Detection", display)
cv2.waitKey(0)
cv2.destroyAllWindows()