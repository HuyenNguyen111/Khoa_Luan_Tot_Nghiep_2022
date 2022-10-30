
from multiprocessing import Event
import numpy as np
import cv2
from .utils import post_processing, plot_boxes_cv2, do_inference
import json

IN_IMAGE_H = 416
IN_IMAGE_W = 416
CLASS_NAME = "platic_box"


def detect(even: Event, buffers, context) -> None:
    vid = cv2.VideoCapture(0)
    quantity = 0
    while (True):
        ret, frame = vid.read()
        resized = cv2.resize(frame, (IN_IMAGE_W, IN_IMAGE_H),
                             interpolation=cv2.INTER_LINEAR)
        img_in = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        img_in = np.transpose(img_in, (2, 0, 1)).astype(np.float32)
        img_in = np.expand_dims(img_in, axis=0)
        img_in /= 255.0
        img_in = np.ascontiguousarray(img_in)

        inputs, outputs, bindings, stream = buffers

        inputs[0].host = img_in
        outputs = do_inference(context, bindings=bindings,
                               inputs=inputs, outputs=outputs, stream=stream)
        outputs[0] = outputs[0].reshape(1, -1, 1, 4)
        outputs[1] = outputs[1].reshape(1, -1, 1)
        boxes = post_processing(img_in, 0.4, 0.6, outputs)
        quantity += len(boxes)
        img = plot_boxes_cv2(frame, boxes[0], class_names=CLASS_NAME)
        cv2.imshow('frame', img)
        if even.is_set():
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

    # ----------- save data -----------
    with open('result.json', 'r') as f:
        data = json.load(f)
    data['quantity'] = quantity
    with open('result.json', 'w') as f:
        json.dump(data, f)
