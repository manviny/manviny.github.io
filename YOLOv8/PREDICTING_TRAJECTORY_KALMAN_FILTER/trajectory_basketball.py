import cv2
from ultralytics import YOLO
from kalmanfilter import KalmanFilter
import math
classNames = ["BasketBall"]
cap = cv2.VideoCapture('videos/demo1.mp4')
kf = KalmanFilter()
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

output = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

model = YOLO("model_weights/best.pt")

if (cap.isOpened()==False):
    print("Unable to read the Video")

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret is False:
        break
    results = model(frame, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1,y1,x2,y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            print(x1, y1, x2, y2)
            cx = int((x1+x2)/2)
            cy = int((y1+y2)/2)
            cv2.circle(frame, (cx, cy), 5, (0,0,255), -1)
            cv2.rectangle(frame, (x1, y1), (x2,y2), (255,0,255), 3)
            conf = math.ceil((box.conf[0]*100))/100
            cls = int(box.cls[0])
            class_name = classNames[cls]
            label = f'{class_name}{conf}'
            predicted=kf.predict(cx, cy)
            cv2.circle(frame, (predicted[0], predicted[1]), 20, (255,0,0), -1)


    resized_frame = cv2.resize(frame, (0,0), fx = 0.5, fy = 0.5, interpolation = cv2.INTER_AREA)
    output.write(frame)
    cv2.imshow("Frame", resized_frame)
    if cv2.waitKey(1) & 0xFF==ord('1'):
        break
output.release()
cap.release()
cv2.destroyAllWindows()