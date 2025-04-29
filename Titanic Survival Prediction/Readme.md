# 🚢 Titanic Survival Prediction

This project is a machine learning solution for predicting survival outcomes of passengers aboard the Titanic using a supervised classification approach. It leverages exploratory data analysis, data preprocessing, and predictive modeling using Scikit-learn.

---

## 📂 Project Structure

```
Titanic Survival Prediction/
│
├── Titanic-Dataset.csv              # Original Titanic dataset
├── Survival_predict.ipynb           # Jupyter Notebook with full pipeline
└── README.md                        # Project documentation
```

---

## 🎯 Objective

To predict whether a passenger survived the Titanic shipwreck using features like age, sex, passenger class, and fare.

---

## 🛠️ Technologies Used

- Python 3.x
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## 📊 Data Preprocessing Steps

- Handling missing values (e.g., imputing age with mean)
- Converting categorical variables (e.g., Gender, Embarked) using encoding
- Feature selection and engineering
- Scaling/normalizing data if needed

---

## 🔍 Exploratory Data Analysis

- Gender vs Survival rate
- Age distribution
- Class-wise survival analysis
- Heatmaps for correlation
- Hyperparameter Tuning

---

## 🤖 Machine Learning Model

- **Algorithm Used**: Logistic Regression
- **Target Variable**: `Survived`
- **Evaluation Metric**: Accuracy

---

## 📈 Results

- **Training Accuracy**: ~81% (subject to change based on dataset split and preprocessing)
- Confusion matrix and classification report are included for evaluation.

---

## 🧪 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Prajwal-repo/AIML-projects.git
   cd 'Titanic Survival Prediction'
   ```

2. Open the notebook:
   ```bash
   jupyter notebook Survival_predict.ipynb
   ```

3. Run the cells sequentially to preprocess, train and evaluate the model.

---

## 📌 Future Improvements

- Experiment with more models (e.g., Random Forest, XGBoost)
- Cross-validation
- Model interpretability with SHAP or LIME

---

## 🙌 Acknowledgments

- Dataset: [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic)
- Thanks to the open-source Python community.

---

## 📬 Contact

For any queries, reach out via GitHub issues or contact the author directly.