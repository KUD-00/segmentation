from ultralytics import YOLO
import time

# Load the trained model
model = YOLO("runs/detect/train3/weights/best.pt")

results = model("split_frames/down_left.jpg", show=True, save=True)