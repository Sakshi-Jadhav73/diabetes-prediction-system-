# 🩺 Diabetes Prediction System

A Machine Learning-based web application that predicts whether a person is diabetic or not based on medical input parameters.

---

## 📌 Project Overview

This project uses a trained Machine Learning model to analyze health-related features such as glucose level, BMI, age, etc., and predicts the likelihood of diabetes. The application is deployed using **Streamlit** for an interactive user interface.

---

## ⚙️ Features

* User-friendly web interface
* Real-time diabetes prediction
* Pre-trained Machine Learning model
* Input-based prediction system
* Simple and clean UI

---

## 📊 Input Features

The model uses the following parameters:

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## 📂 Project Structure

```
Diabetes-Prediction-System/
│── app.py
│── model.pkl
│── scaler.pkl
│── requirements.txt
│── README.md
│── data.csv
│── diabetes_prediction.ipynb
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/Sakshi-Jadhav73/diabetes-prediction-system-.git
```

### 2️⃣ Open Project Folder

```
cd diabetes-prediction-system-
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```
streamlit run app.py
```

---

## 💡 How It Works

* User enters medical details in the web app
* Data is preprocessed using a scaler
* Model predicts whether the person is diabetic or not
* Result is displayed instantly

---

## 📌 Future Improvements

* Improve model performance
* Deploy on cloud (Render/Streamlit Cloud)
* Add user authentication
* Enhance UI/UX
---

## 👩‍💻 Author

Sakshi Jadhav

---
