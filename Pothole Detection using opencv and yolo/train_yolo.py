from ultralytics import YOLO

model = YOLO("yolov8n.pt") 

# Train the model
model.train(
    data="data1.yaml",  
    epochs=1,        
    imgsz=640,         
    batch=8,           
    device="cuda"      
)

# Save best model
print("✅ Training complete! Model saved at: runs/detect/train/weights/best.pt")
