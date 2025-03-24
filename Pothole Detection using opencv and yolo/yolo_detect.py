from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image

model = YOLO("best.pt")  

def detect_potholes(image):
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    results = model(image)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  
            conf = box.conf[0].item()  

            if conf > 0.5:  
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(image, f"Pothole {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return image
