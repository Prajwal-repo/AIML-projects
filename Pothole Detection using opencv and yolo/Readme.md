# 🕳️ Pothole Detection using OpenCV and YOLO

This project implements a pothole detection system using the YOLOv8 object detection model and OpenCV. It allows detection on images, videos, or via a live web interface using Streamlit.

---

## 📁 Project Structure

Pothole Detection using opencv and yolo/ 
├── train/              # Training images and labels 
├── best.pt             # Trained YOLOv8 model weights 
├── yolov8n.pt          # Pre-trained YOLOv8n weights 
├── data1.yaml          # Dataset config 
├── front.py            # Streamlit web interface 
├── opencv_detect.py    # Detection using traditional OpenCV 
├── yolo_detect.py      # Detection using YOLOv8 
├── train_yolo.py       # Script to train YOLOv8 
└── Readme.md           # Project documentation

---

## 🎯 Objective

To detect potholes on roads in real-time using a pre-trained YOLOv8 model or OpenCV image processing techniques.

---

## 🛠️ Technologies Used

- Python 3.x  
- OpenCV  
- Ultralytics YOLOv8  
- Streamlit  
- PyTorch  

---

## 🧪 Detection Methods

### 1. YOLOv8 Detection
- Uses the trained `best.pt` model.
- Script: `yolo_detect.py`

### 2. OpenCV Detection
- Applies thresholding, contour detection.
- Script: `opencv_detect.py`

---

## 🖥️ Web Interface

Launch the Streamlit app (`front.py`) for an interactive UI:
```bash
streamlit run front.py
```

---

## 🚀 How to Run

1. Clone the repo:

```bash
git clone https://github.com/Prajwal-repo/AIML-projects.git
cd AIML-projects/Pothole\ Detection\ using\ opencv\ and\ yolo
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3.(Optional) Train YOLO model:

```bash
python train_yolo.py
```

4. Run detection:

- YOLO: python yolo_detect.py
- OpenCV: python opencv_detect.py

5. Use Streamlit interface:

```bash
streamlit run front.py
```
---

## 💡 Future Improvements

- GPS integration for pothole localization
- Add audio alerts for real-time use
- Deploy on mobile or edge devices

---

## 🙌 Acknowledgments

- Ultralytics YOLOv8
- OpenCV community

