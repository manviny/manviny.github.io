import cv2

image = cv2.imread('../images/image3.png')

resize_image = cv2.resize(image, (0,0), fx=0.6, fy=0.6, interpolation = cv2.INTER_AREA)
cv2.imshow("Image1", resize_image)

cv2.waitKey(0)