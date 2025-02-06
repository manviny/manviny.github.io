import cv2
from ultralytics import YOLO
import math
cap = cv2.VideoCapture('../videos/video1.mp4')
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]
model = YOLO("yolov8n.pt")
if (cap.isOpened()=='False'):
    print("Error Reading the Video")
center_points = []
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

output = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
count = 0
center_point_previous_frame=[]
tracking_objects = {}
track_id=0
while (cap.isOpened()):
    center_points_current_frame = []
    count += 1
    ret, frame = cap.read()
    if ret:
        #Object Detetcions using YOLOv8, frame by frame
        #stream = True, it will be using generator and it is more efficient than the normal
        results = model(frame, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1,y1, x2,y2 = box.xyxy[0]
                print(x1, y1, x2, y2)
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                print("Frame N", count, "", x1, y1, x2, y2)
                cx = int((x2+x1)/2)
                cy = int((y2+y1)/2)
                center_points_current_frame.append((cx,cy))
                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255, 0), 3)
                conf = math.ceil((box.conf[0]*100))/100
                cls = int(box.cls[0])
                class_name = classNames[cls]
                label = f'{class_name}{conf}'
                text_size=cv2.getTextSize(label,0, fontScale=1, thickness=2)[0]
                c2 = x1+text_size[0],  y1 - text_size[1] -3
                cv2.rectangle(frame, (x1, y1), c2, [255,0,0], -1, cv2.LINE_AA)
                cv2.putText(frame, label, (x1, y1-2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)
        if count <=2:
            for pt in center_points_current_frame:
                for pt2 in center_point_previous_frame:
                    distance = math.hypot(pt2[0]-pt[0], pt2[1]-pt[1])
                    if distance < 20:
                        tracking_objects[track_id] = pt
                        track_id+=1
        else:
            tracking_objects_copy = tracking_objects.copy()
            center_points_current_frame_copy = center_points_current_frame.copy()
            for object_id, pt2 in tracking_objects_copy.items():
                object_exists=False
                for pt in center_points_current_frame_copy:
                    distance = math.hypot(pt2[0]-pt[0], pt2[1]-pt[1])
                    if distance < 20:
                        tracking_objects[object_id] = pt
                        object_exists=True
                        if pt in center_points_current_frame:
                            center_points_current_frame.remove(pt)
                        continue
                if not object_exists:
                    tracking_objects.pop(object_id)
            # Add new ID found
            for pt in center_points_current_frame:
                tracking_objects[track_id] = pt
                track_id+=1
        for object_id, pt in tracking_objects.items():
            cv2.circle(frame, pt, 5, (0,0,255), -1)
            cv2.putText(frame, str(object_id), (pt[0], pt[1]-7), 0, 1, (255,0,0), 3)
        resize_frame = cv2.resize(frame, (0, 0), fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA)
        output.write(frame)
        print("Center Points of the Current Frame")
        print(center_points_current_frame)
        print("Center Points of the Previous Frame")
        print(center_point_previous_frame)

        center_point_previous_frame = center_points_current_frame.copy()
        cv2.imshow("Frame", resize_frame)

        if cv2.waitKey(1)&0xFF==ord('1'):
            break
    else:
        break
output.release()
cap.release()
cv2.destroyAllWindows()