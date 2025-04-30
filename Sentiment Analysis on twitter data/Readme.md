
# 🧠 Sentiment Analysis on Twitter Data

This project implements a sentiment analysis model using machine learning and natural language processing (NLP) to classify tweets as either positive or negative. It demonstrates a complete pipeline from data preprocessing to model training and evaluation using a neural network.

---

## 📁 Project Structure

```
Sentiment Analysis on twitter data/
├── Sentiment_analysis.ipynb      # Jupyter Notebook with preprocessing, training, and evaluation
├── twitter_sentiment_model.h5    # Saved trained model
└── Readme.md                     # Project documentation
```

---

## 🎯 Objective

To build a machine learning model capable of analyzing the sentiment of tweets (positive/negative) using text data and NLP techniques.

---

## 🛠️ Technologies Used

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- TensorFlow / Keras
- NLTK
- Jupyter Notebook

---

## 📊 Data Preprocessing Steps

- **Text Cleaning**: Removing special characters, converting to lowercase
- **Tokenization**: Breaking sentences into individual words
- **Stopword Removal**: Eliminating common words with low information value
- **Vectorization**: Converting words into numerical form using CountVectorizer or TF-IDF

---

## 🤖 Model Details

- **Type**: Feedforward Neural Network using Keras
- **Layers**: Dense + Dropout layers
- **Loss Function**: Binary Crossentropy
- **Optimizer**: Adam
- **Metrics**: Accuracy

---

## 📈 Results

- Achieved high accuracy on the test dataset
- Confusion matrix, accuracy, precision, and recall used for evaluation

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Prajwal-repo/AIML-projects.git
   cd AIML-projects/Sentiment\ Analysis\ on\ twitter\ data
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Jupyter Notebook:
   ```bash
   jupyter notebook Sentiment_analysis.ipynb
   ```

---

## 💡 Future Enhancements

- Integrate real-time tweet fetching via Twitter API
- Use LSTM or transformer-based models like BERT
- Deploy via Flask/Streamlit for interactive web app

---

## 🙌 Acknowledgments

- Dataset: [Kaggle - Sentiment140](https://www.kaggle.com/datasets/kazanova/sentiment140)
- Project inspired by various NLP and sentiment classification tutorials

---

## 📬 Contact

For feedback or questions, please open an issue on the GitHub repo.
