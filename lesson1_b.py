import cv2
image=cv2.imread("zebra.webp",cv2.IMREAD_COLOR)
if image is None:
    print("Image not found. Check the file path.")
else:
    hsv_image=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("deer",image)
    cv2.waitKey(0)
    cv2.imshow("deer HSV",hsv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()