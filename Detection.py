import cv2
import torch
import numpy as np
path = "C:/Users/HP/Desktop/headphone_detection/headphone/best-100-lat.pt"
model = torch.hub.load('ultralytics/yolov5', 'custom', path, force_reload = True)
cap = cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    frame = cv2.resize(frame,(1400,700))
    results = model(frame)
    frame = np.squeeze(results.render())
    cv2.imshow('FRAME', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()