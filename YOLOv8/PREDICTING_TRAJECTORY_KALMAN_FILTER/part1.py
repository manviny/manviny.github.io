import cv2
from kalmanfilter import KalmanFilter

kf = KalmanFilter()
circle_positions = [(50, 100), (100, 100), (150, 100), (200, 100), (250, 100), (300, 100), (350, 100), (400, 100), (450, 100)]
img = cv2.imread("image/image.jpg")
for pt in circle_positions:
    cv2.circle(img, pt, 15, (255,0,0),-1)
    predicted = kf.predict(pt[0], pt[1])
    #print(predicted)
    cv2.circle(img, predicted, 15, (0,255,0), 5)
#predicted1 = kf.predict(predicted[0], predicted[1])
#cv2.circle(img, predicted1, 15, (0,255,0), 5)
for i in range(10):
    predicted = kf.predict(predicted[0], predicted[1])
    cv2.circle(img, predicted, 15, (0,255,0), 5)
cv2.imshow("Image", img)

cv2.waitKey(0)