import numpy as np
from ultralytics import YOLO
import cv2
import time
import os

#old models
#defining model for front and rear cameras
model_front = YOLO(model = r"C:\Users\tuana\Downloads\Front.pt", task = 'detect')
model_rear = YOLO(model = r"C:\Users\tuana\Downloads\train2\train2\epoch-1021.engine", task = 'detect')


# Get the bottom half of the frame
def inference(vid):
    ret, frame = vid.read()
    height = frame.shape[0]
    bottom_half_frame = frame[height // 2:, :]
    result_rear = model_rear.track(bottom_half_frame, device='cuda:0',tracker = 'bytetrack.yaml', persist = True)
    for i, r in enumerate(result_rear):
        for box in r.boxes.xywh:
            x = int(box[0].item())
            y = int(box[1].item())
            w = int(box[2].item())
            h = int(box[3].item())

            # get the half of the frame
            half_frame = frame.shape[1] // 2
            mask = np.zeros_like(frame)
            mask[y:y + h, x:x + w] = 255

            # define the left and right cameras
            left_mask = mask[:, :half_frame]
            right_mask = mask[:, half_frame:]

            #return if there is an object in the right or left of the camera
            if left_mask.any():
                return {'right': True}
            elif right_mask.any():
                return {'left': True}

            # after done with the masks, reset them
            left_mask = np.zeros_like(left_mask)
            right_mask = np.zeros_like(right_mask)

def inference_front(vid):
    ret, frame = vid.read()
    height = frame.shape[0]
    top_half_frame = frame[:height // 2, :]
    result_front = model_front.track(top_half_frame, device='cuda:0', tracker = 'bytetrack.yaml', persist = True, show = True)
    for i, r in enumerate(result_front):
        for box in r.boxes.xywh:
            x = int(box[0].item())
            y = int(box[1].item())
            w = int(box[2].item())
            h = int(box[3].item())

            mask = np.zeros_like(frame)
            mask[y:y + h, x:x + w] = 255
            #return if there is an object in the right or left of the camera
            if mask.any():
                return {'front': True}