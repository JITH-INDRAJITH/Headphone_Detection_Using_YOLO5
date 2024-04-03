# Headphone_Detection_Using_YOLO5

## Objective
The objective of this project is to detect whether a person is wearing headphones in a live webcam feed using YOLO (You Only Look Once) object detection.

## Dataset Collection
Images were collected by capturing snapshots using a webcam.
Two categories were created: "Person_not_wearing_headphones" and "Person_with_headphones".
# The images were annotated and labeled using LabelImg.
## Training
The dataset was split into training and validation sets.
Due to hardware limitations, training was conducted on Google Colab using GPU acceleration.
## The YOLOv5 model was trained using the following command:
### python train.py --img 640 --epochs 100 /yolov5train/dataset.yaml --weights yolov5s.pt

## Webcam Testing
Python code was developed to access the webcam feed.
The trained model was integrated into the code to detect whether a person is wearing headphones in real-time.
The results are displayed in a window.
# Results
Person_not_wearing_headphone:
Person_with_headphone:

## Files
To_Take_Images.py : To snap the Images for custom dataset, Using this we can Train our model.
train.py: Python script for training the YOLOv5 model.
dataset.yaml: YAML file containing dataset configuration.
detection.py: Python script for accessing webcam and performing real-time headphone detection.
## Future Improvements
Fine-tuning the model for better accuracy.
Scaling the system for real-world applications.
Integrating additional features such as notifications/alerts for headphone detection.
## Conclusion
The project successfully demonstrates the implementation of YOLO object detection for live webcam headphone detection. Further improvements and optimizations can enhance its applicability in various domains.

