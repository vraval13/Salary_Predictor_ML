import streamlit as st
import pickle
import numpy as np

# Load the model
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_edu"]

# Show prediction page
def show_predict_page():
    # Apply some custom CSS for styling and animations
    st.markdown("""
        <style>
            .stButton button {
                background-color: #008CBA;
                border: none;
                color: white;
                padding: 12px 24px;
                font-size: 16px;
                border-radius: 12px;
                transition: background-color 0.3s ease;
            }
            .stButton button:hover {
                background-color: #005f6b;
            }
            .title {
                font-size: 36px;
                color: #4CAF50;
                text-align: center;
                animation: slideDown 1s ease-in-out;
            }
            @keyframes slideDown {
                0% { transform: translateY(-100%); opacity: 0; }
                100% { transform: translateY(0); opacity: 1; }
            }
            .description {
                text-align: center;
                font-size: 18px;
                color: #555;
                margin-bottom: 20px;
            }
            .footer {
                margin-top: 50px;
                text-align: center;
                font-size: 12px;
                color: #aaa;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Title with custom CSS animation
    st.markdown("<div class='title'>Software Developer Salary Prediction</div>", unsafe_allow_html=True)

    # st.markdown("<div class='description'>We need some information to predict the salary</div>", unsafe_allow_html=True)

    countries = (
        "United States of America",
        "India",
        "United Kingdom of Great Britain and Northern Ireland",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Italy",
        "Other"
    )

    education_levels = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad"
    )

    # Create user input fields with select boxes and sliders
    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education_levels)
    experience = st.slider("Years of Experience", 0, 50, 3)

    # Button to trigger prediction
    ok = st.button("Calculate Salary")
    
    # Perform prediction and show result when button is clicked
    if ok:
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:, 0])
        X[:, 1] = le_education.transform(X[:, 1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:,.2f}")

    # Footer with smooth animation
    st.markdown("""
        <div class='footer'>
            Powered by Streamlit · Data from Stack Overflow Developer Survey
        </div>
    """, unsafe_allow_html=True)

