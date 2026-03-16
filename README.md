# ⚡ Power Plant Energy Output Prediction using Machine Learning

## 📌 Project Overview

This project predicts the **power output (PE)** of a Combined Cycle Power Plant based on environmental conditions.
Machine learning models are trained on historical operational data to understand how atmospheric factors influence electricity generation.

The goal is to build accurate predictive models that can assist **power plant operators and energy companies in forecasting power production and optimizing efficiency**.

---

## 📊 Dataset Information

The dataset contains operational data from a **Combined Cycle Power Plant** with the following features:

| Feature | Description                                           |
| ------- | ----------------------------------------------------- |
| **AT**  | Ambient Temperature                                   |
| **V**   | Exhaust Vacuum                                        |
| **AP**  | Ambient Pressure                                      |
| **RH**  | Relative Humidity                                     |
| **PE**  | Net Hourly Electrical Energy Output (Target Variable) |

Typical output range:

420 MW – 495 MW

---

## ⚙️ Machine Learning Models Implemented

Several regression models were trained and evaluated:

* Linear Regression
* Random Forest Regressor
* Gradient Boosting Regressor
* XGBoost Regressor
* Artificial Neural Network (ANN) using PyTorch

These models were compared using standard regression metrics.

---

## 📈 Model Performance Comparison

| Model                     | R² Score   | Notes                                    |
| ------------------------- | ---------- | ---------------------------------------- |
| Linear Regression         | ~0.93      | Baseline model                           |
| Random Forest             | ~0.95      | Strong performance with ensemble trees   |
| Gradient Boosting         | ~0.95      | Improved learning of complex patterns    |
| XGBoost                   | ~0.96–0.97 | Best performing model                    |
| Artificial Neural Network | ~0.93–0.94 | Good performance with nonlinear modeling |

The **XGBoost model achieved the best predictive accuracy**.

---

## 🔍 Key Insights

* **Ambient Temperature (AT)** is the most influential variable affecting power output.
* Lower temperatures typically lead to **higher plant efficiency and greater power generation**.
* Ensemble tree models significantly outperform simple linear regression for this dataset.

---

## 🧠 Feature Importance

Feature importance analysis (using Random Forest) shows:

1. Ambient Temperature (AT) – dominant factor
2. Exhaust Vacuum (V)
3. Ambient Pressure (AP)
4. Relative Humidity (RH)

This aligns with real-world thermodynamic behavior of power plants.

---

## 🌐 Live Deployment

The trained model has been deployed using **Streamlit**.

Live Demo:
[Add your Streamlit link here]

Users can input environmental conditions and receive an instant prediction of power output.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* PyTorch
* Streamlit
* Matplotlib / Seaborn

---

## 📂 Project Structure

```
power-plant-ml/
│
├── app.py                 # Streamlit application
├── power_model.pkl        # Trained ML model
├── requirements.txt       # Dependencies
├── power_prediction.ipynb # Model training notebook
└── README.md
```

---

## 🚀 How to Run the Project Locally

1. Clone the repository

```
git clone https://github.com/yourusername/power-plant-ml.git
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the Streamlit app

```
streamlit run app.py
```

4. Open in browser

```
http://localhost:8501
```

---

## 🎯 Applications

This model can be useful for:

* Power plant operational planning
* Energy production forecasting
* Smart grid management
* Energy efficiency analysis

---

## 👨‍💻 Author

**Raghav Chugh**
B.Tech Artificial Intelligence

Skills:
Python • Machine Learning • Data Analysis • Web Deployment

---

## ⭐ If you found this project useful

Feel free to **star the repository** and connect with me on LinkedIn.
