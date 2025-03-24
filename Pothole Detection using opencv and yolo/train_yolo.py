from ultralytics import YOLO

if __name__ == "__main__":  
    model = YOLO("yolov8n.pt")  

    model.train(
        data="C:/Users/Prajwal/OneDrive/Desktop/AIML-Projects/Pothole Detection using opencv and yolo/data1.yaml",
        epochs=5,
        imgsz=640,
        batch=8,
        device="cpu"
    )

