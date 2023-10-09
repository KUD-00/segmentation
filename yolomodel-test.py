from ultralytics import YOLO
import time

# Load the trained model
model = YOLO("runs/detect/train2/weights/best.pt")

results = model("split_frames/down_right.jpg", show=True, save=True)