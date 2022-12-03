import numpy as np
import cv2
from .utils import post_processing, plot_boxes_cv2
import threading
import os
import time

IN_IMAGE_H = 416
IN_IMAGE_W = 416
CLASS_NAME = ["Plastic_bottle", "Plactic_bottle_detergent", "Plastic_box", "Plastic_bottle_yogurt", "Can", "Foam_box", "Face_mask"]

labels = [0, 1, 2, 3, 4]

fps = None

class CameraThread(threading.Thread):
    def __init__(self, session) -> None:
        threading.Thread.__init__(self)
        self.session = session
        self.name = "camera"

    def run(self) -> None:
        global fps
        vid = cv2.VideoCapture(0)
        prev_frame_time = 0
        new_frame_time = 0
        while vid.isOpened():
            quantity = 0
            _, frame = vid.read()
            resized = cv2.resize(frame, (IN_IMAGE_W, IN_IMAGE_H),
                            interpolation=cv2.INTER_LINEAR)
            img_in = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
            img_in = np.transpose(img_in, (2, 0, 1)).astype(np.float32)
            img_in = np.expand_dims(img_in, axis=0)
            img_in /= 255.0
            outputs = self.session.run(None, {"input": img_in})
            boxes = post_processing(img_in, 0.4, 0.6, outputs)
            img = plot_boxes_cv2(frame, boxes[0], class_names=CLASS_NAME)
            for i in range(len(boxes[0])):
                box = boxes[0][i]
                if len(box) >= 7:
                    cls_conf = box[5]
                    cls_id = box[6]
                    if cls_conf > 0.5 and cls_id in labels:
                        quantity += 1
            if os.path.exists('count/request.txt'):
                os.remove('count/request.txt')
                with open('count/response.txt', 'w') as f:
                    f.write(f'{quantity}')
            new_frame_time = time.time()
            fps = 1/(new_frame_time - prev_frame_time)
            fps = int(fps)
            fps = f'FPS: {fps} classes: {quantity}'

            img = cv2.putText(img, fps, (7, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100, 255, 0), 1, cv2.LINE_AA)
            cv2.imshow('frame', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            prev_frame_time = time.time()
        vid.release()
        cv2.destroyAllWindows()
