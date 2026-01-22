#  Fake News Detection (Machine Learning + Streamlit)

This project is a **Fake News Detection system** that classifies news as **Fake ** or **Real ** using **Machine Learning** and a simple **Streamlit web app**.

---

##  Demo Features
 Enter news text/title  
 Predict whether the news is Fake or Real  
 Simple UI using Streamlit  
 Trained using TF-IDF + ML model  

---

##  Dataset
Dataset used:
- `Fake.csv` (Fake news articles)
- `True.csv` (Real news articles)

Source: Kaggle Fake News Dataset

---

##  Machine Learning Approach
###  Data Preprocessing
- Combined `Fake.csv` and `True.csv`
- Assigned labels:
  - Fake → `0`
  - True → `1`
- Removed duplicates (optional)
- Shuffled dataset

###  Feature Extraction
Used:
- **TF-IDF Vectorizer**

###  Model Used
- **KNN Classifier** *(as used in the Streamlit app)*  
*(You can also try Logistic Regression / Naive Bayes for comparison)*

---

##  Model Evaluation
Model performance was evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

