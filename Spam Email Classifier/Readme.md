
# 📧 Spam Email Classifier

This project implements a machine learning model to classify emails as spam or not spam (ham). It uses natural language processing (NLP) techniques and a Naive Bayes classifier to detect spam messages in email content.

---

## 📁 Project Structure

```
Spam Email Classifier/
├── spam.csv                    # Dataset of labeled emails (spam/ham)
├── Email_classifier.ipynb      # Jupyter Notebook with preprocessing, training, and evaluation
└── Readme.md                   # Project documentation
```

---

## 🎯 Objective

To build a classifier that can automatically distinguish between spam and non-spam emails using supervised learning.

---

## 🛠️ Technologies Used

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Jupyter Notebook

---

## 📊 Data Preprocessing Steps

- **Text Cleaning**: Lowercasing, removing punctuation and special characters
- **Tokenization**: Breaking the email text into tokens (words)
- **Stopword Removal**: Removing common English stopwords
- **Vectorization**: Using CountVectorizer or TF-IDF to convert text into numerical features

---

## 🤖 Model Details

- **Algorithm**: Multinomial Naive Bayes
- **Training/Test Split**: 80/20
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1-score

---

## 📈 Results

The Naive Bayes classifier showed:

- **Accuracy**: ~98%
- **Precision and Recall**: High values, indicating good spam detection performance
- **Confusion Matrix**: Shows a low false positive and false negative rate

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Prajwal-repo/AIML-projects.git
   ```

2. Navigate to the project:
   ```bash
   cd AIML-projects/Spam\ Email\ Classifier
   ```

3. Open the notebook:
   ```bash
   jupyter notebook Email_classifier.ipynb
   ```

4. Run all cells to train the model and test its predictions.

---

## 💡 Future Improvements

- Add support for live email classification via user input
- Explore deep learning models like LSTM or BERT for better accuracy
- Implement deployment using Flask or Streamlit

---

## 🙌 Acknowledgments

- Dataset Source: [Kaggle Spam Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- Tools: Scikit-learn, NLTK, Python community contributions

---

## 📬 Contact

For queries or suggestions, open an issue on the GitHub repo or contact the author directly.
