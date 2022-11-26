
from multiprocessing import Event
import numpy as np
import cv2
from .utils import post_processing, plot_boxes_cv2
import json

IN_IMAGE_H = 416
IN_IMAGE_W = 416
CLASS_NAME = "platic_box"


labels = [0, 1, 2, 3, 4]

def detect(session) -> None:
    vid = cv2.VideoCapture(0)
    quantity = 0
    ret, frame = vid.read()
    resized = cv2.resize(frame, (IN_IMAGE_W, IN_IMAGE_H),
                            interpolation=cv2.INTER_LINEAR)
    img_in = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
    img_in = np.transpose(img_in, (2, 0, 1)).astype(np.float32)
    img_in = np.expand_dims(img_in, axis=0)
    img_in /= 255.0
    outputs = session.run(None, {"input": img_in})
    print(outputs[0].shape)
    print(outputs[1].shape)
    boxes = post_processing(img_in, 0.4, 0.6, outputs)
    for i in range(len(boxes[0])):
        box = boxes[0][i]
        if len(box) >= 7:
            cls_conf = box[5]
            cls_id = box[6]
            if cls_conf > 0.5 and cls_id in labels:
                quantity += 1
        
    vid.release()
    # ----------- save data -----------
    with open('result.json', 'r') as f:
        data = json.load(f)
    data['quantity'] = quantity
    with open('result.json', 'w') as f:
        json.dump(data, f)
    return quantity