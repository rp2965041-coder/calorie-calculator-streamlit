# 🍎 Calorie Calculator - Streamlit App

A simple and beginner-friendly **Calorie Calculator web application** built using **Python and Streamlit**.

The application calculates a user's estimated **Basal Metabolic Rate (BMR)** and **daily calorie requirement (TDEE)** based on their personal details and activity level.

## 🚀 Features

* Enter user's name
* Enter age
* Select gender
* Enter weight in kilograms
* Enter height in centimeters
* Select activity level
* Calculate estimated BMR
* Calculate estimated daily calorie requirement
* Simple and user-friendly Streamlit interface

## 🛠️ Technologies Used

* **Python 3.10**
* **Streamlit**
* **Conda Environment**

## 📁 Project Structure

```text
calorie-calculator-streamlit/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Create a Conda environment

Open Anaconda Prompt and run:

```bash
conda create -n myenv python=3.10
```

Activate the environment:

```bash
conda activate myenv
```

### 2. Install Streamlit

```bash
pip install streamlit
```

Or install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Open Anaconda Prompt and navigate to the project folder:

```bash
cd Desktop\streamlit_app
```

Then run:

```bash
streamlit run app.py
```

The application will open in your web browser.

## 🧮 Calculation

The application uses the **Mifflin-St Jeor equation** to estimate BMR.

The estimated daily calorie requirement is calculated by multiplying BMR by an activity factor.

### Activity Levels

| Activity Level    | Factor |
| ----------------- | -----: |
| Sedentary         |    1.2 |
| Lightly Active    |  1.375 |
| Moderately Active |   1.55 |
| Very Active       |  1.725 |
| Extra Active      |    1.9 |

## 🎯 Purpose

This project was created as a simple **Python and Streamlit learning project** to demonstrate how user inputs can be processed and displayed through an interactive web application.

## ⚠️ Disclaimer

The calorie values provided by this application are estimates for educational purposes only. They should not be considered medical or professional nutritional advice.

## 👨‍💻 Author

**Raj Bhosale**

## 📄 License

This project is available for educational and learning purposes.
