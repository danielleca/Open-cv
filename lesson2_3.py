import cv2

img = cv2.imread("img2.png")

bordered_image = cv2.copyMakeBorder(
    img, 10, 10, 10, 10,
    cv2.BORDER_CONSTANT,
    value = (0,0,255)
)

cv2.imshow("Constant border", bordered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

bordered_image = cv2.copyMakeBorder(
    img, 10, 10, 10, 10,
    cv2.BORDER_WRAP,
)

cv2.imshow("Wrap border", bordered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

bordered_image = cv2.copyMakeBorder(
    img, 10, 10, 10, 10,
    cv2.BORDER_REFLECT,
)

cv2.imshow("Reflect border", bordered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

bordered_image = cv2.copyMakeBorder(
    img, 10, 10, 10, 10,
    cv2.BORDER_REFLECT_101,
)

cv2.imshow("Reflect_101 border", bordered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()