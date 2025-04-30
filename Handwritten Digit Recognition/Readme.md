
# ✍️ Handwritten Digit Recognition

This project implements a Convolutional Neural Network (CNN) to recognize handwritten digits using image data. It demonstrates a typical deep learning pipeline for image classification using TensorFlow/Keras.

---

## 📁 Project Structure

```
Handwritten Digit Recognition/
├── digit_pixels.csv             # Dataset with pixel values of digit images
├── test.csv                     # Dataset for evaluation
├── Digit_recognition.ipynb      # Notebook with model training and evaluation
├── cnn_adam.h5                  # Saved trained model weights
└── Readme.md                    # Project documentation
```

---

## 🎯 Objective

To develop a deep learning model that accurately classifies handwritten digits (0 to 9) based on pixel input.

---

## 🛠️ Technologies Used

- Python 3.x
- NumPy
- Pandas
- TensorFlow / Keras
- Matplotlib
- Jupyter Notebook

---

## 📊 Data Preprocessing

- **Loading CSV Files**: Importing training and testing data
- **Normalization**: Scaling pixel values to [0, 1] range
- **Reshaping**: Changing input shape to (28, 28, 1)
- **One-hot Encoding**: Encoding digit labels into binary matrix

---

## 🤖 CNN Model Architecture

The model includes:

- Convolutional Layers for feature extraction
- MaxPooling Layers to reduce spatial size
- Dense Layers for classification
- ReLU and Softmax activation functions

Example Model Summary:
```python
model = Sequential([
    Conv2D(32, kernel_size=3, activation='relu', input_shape=(28,28,1)),
    MaxPooling2D(2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])
```

---

## 📈 Results

The model performs well with high accuracy on the test dataset:

- **Test Accuracy**: Over 98% (depending on training)
- **Low Loss**: Indicates effective learning from features

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Prajwal-repo/AIML-projects.git
   cd AIML-projects/Handwritten\ Digit\ Recognition
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch the notebook:
   ```bash
   jupyter notebook Digit_recognition.ipynb
   ```

4. Execute all cells for training and testing.

---

## 💡 Future Work

- Add data augmentation
- Try other CNN architectures (e.g., LeNet, VGG)
- Convert to real-time recognition using a webcam interface
- Deploy with Streamlit/Flask

---

## 🙌 Acknowledgments

- Dataset: [Kaggle Digit Recognizer](https://www.kaggle.com/datasets/hojjatk/mnist-dataset)
- Inspired by foundational CNN applications in computer vision.

---

## 📬 Contact

For questions or feedback, open an issue on the GitHub repository.
