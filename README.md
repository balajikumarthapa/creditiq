# 💳 CreditIQ — Credit Risk Intelligence Platform

An AI-powered credit risk prediction system built with Streamlit and Random Forest Machine Learning.

---

## 📁 Project Structure

```
final_year_project_edit/
│
├── app.py                          ← main entry point
├── requirements.txt                ← install dependencies
├── users.db                        ← user login database
├── project2.ipynb                  ← data exploration notebook
├── Base Paper.pdf                  ← research reference paper
│
├── assets/
│   └── css/
│       └── main.css                ← all custom CSS styling
│
├── components/
│   ├── auth.py                     ← login & register UI
│   ├── header.py                   ← top header bar
│   └── sidebar.py                  ← navigation menu
│
├── custom_pages/
│   ├── about.py                    ← project info & team details
│   ├── analytics.py                ← model performance analytics
│   ├── dashboard.py                ← main dashboard with charts
│   ├── dataset.py                  ← dataset explorer
│   ├── history.py                  ← prediction history & export
│   └── prediction.py               ← real-time credit risk prediction
│
├── config/
│   └── settings.py                 ← app configuration & constants
│
├── data/
│   └── raw/
│       └── creditdata.csv          ← raw loan dataset
│
├── ml/
│   ├── predict.py                  ← model loading & prediction logic
│   └── preprocessing.py            ← data preprocessing pipeline
│
├── models/
│   └── loan_model.pkl              ← trained Random Forest model
│
└── utils/
    ├── data_loader.py              ← loads and preprocesses data
    ├── helpers.py                  ← utility functions (CSS loader etc.)
    └── session_manager.py          ← manages user session state
```

---

## 🚀 How to Run

```bash
# Step 1 — Install dependencies
pip install -r requirements.txt

# Step 2 — Run the app
streamlit run app.py
```

---

## 🔐 Default Login

| Email               | Password  |
|---------------------|-----------|
| admin@creditiq.com  | Admin@123 |

> You can also register a new account from the Register tab on the login page.

---

## 🧠 Machine Learning Model

- **Algorithm:** Random Forest Classifier
- **Task:** Binary Classification (Low Risk / High Risk)
- **Dataset:** creditdata.csv
- **Model File:** models/loan_model.pkl

---

## 📊 App Pages

| Page            | Description                                 |
|-----------------|---------------------------------------------|
| Dashboard       | Overview metrics and charts                 |
| Prediction      | Real-time credit risk prediction with gauge |
| History         | View and download past predictions          |
| Dataset         | Explore the raw loan dataset                |
| Model Analytics | Accuracy, Precision, Recall, F1 Score       |
| About           | Project info, team members, and tech stack  |

---

## 👨‍💻 Developed By

- Aman H
- Anbudaiya Balan R
- Balaji Kumar Thapa L
- Balasubramani L

---

## 🛠 Tech Stack

- Python
- Streamlit
- Scikit-Learn
- Plotly
- Pandas & NumPy
- Random Forest Classifier