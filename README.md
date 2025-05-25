# 🌱 Crop Recommendation System using Machine Learning

This project predicts the best crop to cultivate based on environmental and soil conditions. It’s part of a larger vision to develop smart agriculture solutions in Malaysia.

## 📊 Dataset

Used the [Crop Recommendation Dataset](https://www.kaggle.com/datasets) with the following features:
- N: Nitrogen content
- P: Phosphorus content
- K: Potassium content
- Temperature
- Humidity
- pH
- Rainfall
- Label: Crop type

## ⚙️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Matplotlib, Seaborn
- Google Colab

## 🔍 Workflow

1. **Data Exploration & Visualization**
2. **Preprocessing**: Label encoding, scaling
3. **Model Training**: 
   - `RandomForestClassifier`
   - `XGBClassifier`
4. **Model Comparison**:
   - Accuracy
   - Classification Report
   - Confusion Matrix
5. **Hyperparameter Tuning**: GridSearchCV

## 🧠 Results

Both models achieved high accuracy (>99%).  
XGBoost showed slightly better recall and F1-score on multiple classes.

## 📌 Future Plan

- Integrate real-time GPS + soil data for Malaysian farms
- Deploy model for farmer usage
- Transition into a business model for smart farming

## 📬 Contact

Feel free to connect on [LinkedIn](your-linkedin-url) or reach out to collaborate on smart agriculture solutions!
