import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Calorie Calculator",
    page_icon="🍎"
)

# Title
st.title("🍎 Daily Calorie Calculator")

st.write("Enter your details to calculate your estimated daily calorie requirement.")

# User inputs
name = st.text_input("Enter your name:")

age = st.number_input(
    "Enter your age:",
    min_value=1,
    max_value=120,
    value=20
)

gender = st.selectbox(
    "Select your gender:",
    ["Male", "Female"]
)

weight = st.number_input(
    "Enter your weight (kg):",
    min_value=1.0,
    max_value=300.0,
    value=60.0
)

height = st.number_input(
    "Enter your height (cm):",
    min_value=50.0,
    max_value=250.0,
    value=170.0
)

activity = st.selectbox(
    "Select your activity level:",
    [
        "Sedentary - little or no exercise",
        "Lightly Active - exercise 1-3 days/week",
        "Moderately Active - exercise 3-5 days/week",
        "Very Active - exercise 6-7 days/week",
        "Extra Active - intense exercise or physical job"
    ]
)

# Calculate button
if st.button("Calculate Calories"):

    # Calculate BMR using Mifflin-St Jeor equation
    if gender == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    # Activity multipliers
    activity_factors = {
        "Sedentary - little or no exercise": 1.2,
        "Lightly Active - exercise 1-3 days/week": 1.375,
        "Moderately Active - exercise 3-5 days/week": 1.55,
        "Very Active - exercise 6-7 days/week": 1.725,
        "Extra Active - intense exercise or physical job": 1.9
    }

    # Calculate daily calories
    tdee = bmr * activity_factors[activity]

    # Display results
    st.success(f"Hello {name}! Your results are:")

    st.subheader("Your Results")

    st.write(f"**BMR:** {bmr:.0f} calories/day")
    st.write(f"**Estimated Daily Calories:** {tdee:.0f} calories/day")

    st.info(
        "This is an estimate of your daily energy needs and is not medical advice."
    )