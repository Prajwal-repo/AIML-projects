
# 🏠 House Price Prediction

This project presents a machine learning approach to predict house prices based on various features. Utilizing the Boston Housing dataset, the model aims to provide accurate estimations, aiding stakeholders in making informed real estate decisions.

---

## 📁 Project Structure

```
House Price Prediction/
├── Housing.csv               # Dataset containing housing features and prices
├── Price_Predict.ipynb       # Jupyter Notebook with data analysis and model training
└── Readme.md                 # Project documentation
```

---

## 🎯 Objective

To develop a predictive model that estimates house prices using features such as:

- Crime rate
- Number of rooms
- Distance to employment centers
- Property tax rate
- Pupil-teacher ratio

---

## 🛠️ Technologies Used

- Python 3.x
- Pandas
- NumPy
- Matplotlib & Seaborn
- Scikit-learn

---

## 📊 Data Preprocessing

- **Handling Missing Values**: Ensured the dataset has no null values.
- **Feature Selection**: Identified and selected relevant features impacting house prices.
- **Normalization**: Scaled features to ensure uniformity.

---

## 🤖 Model Development

- **Algorithm**: Linear Regression
- **Training**: Split the dataset into training and testing sets.
- **Evaluation**: Assessed model performance using Mean Squared Error (MSE) and R² score.

---

## 📈 Results

The Linear Regression model achieved:

- **Mean Squared Error**: ~959766
- **R² Score**: ~0.58

These metrics indicate the model's effectiveness in predicting house prices based on the selected features.

---

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Prajwal-repo/AIML-projects.git
   ```

2. Navigate to the project directory:

   ```bash
   cd AIML-projects/House\ Price\ Prediction
   ```

3. Open the Jupyter Notebook:

   ```bash
   jupyter notebook Price_Predict.ipynb
   ```

4. Run the cells sequentially to execute data preprocessing, model training, and evaluation.

---

## 📌 Future Enhancements

- Incorporate advanced regression algorithms like Random Forest and Gradient Boosting.
- Implement cross-validation for more robust model evaluation.
- Deploy the model using Flask or Streamlit for real-time predictions.

---

## 🙌 Acknowledgments

- Dataset: [Boston Housing Dataset]
- Inspired by the open-source community and educational resources.

---

## 📬 Contact

For any queries or suggestions, feel free to reach out via [GitHub Issues](https://github.com/Prajwal-repo/AIML-projects/issues).
