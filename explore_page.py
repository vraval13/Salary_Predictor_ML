import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to filter countries with a threshold
def filterShortCountries(categories, threshold):
    catMap = {}
    for i in range(len(categories)):
        if categories.values[i] >= threshold:
            catMap[categories.index[i]] = categories.index[i]
        else:
            catMap[categories.index[i]] = 'Other'
    return catMap

# Function to clean Years of CodePro
def cleanYear(x):
    if x == 'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

# Function to clean the education levels
def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    if ('Some college/university' in x or 
        'Secondary school' in x or 
        'Associate degree' in x or 
        'Primary/elementary school' in x or 
        'Something else' in x):
        return 'Less than a Bachelors'
    return 'Less than a Bachelors'

# Cache the data loading function for improved performance
@st.cache
def load_data():
    df = pd.read_csv('survey_results_public.csv')
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()

    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop(columns=["Employment"])

    shortCountryMap = filterShortCountries(df.Country.value_counts(), 400)
    df["Country"] = df["Country"].map(shortCountryMap)
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df["Salary"] != 'Other']

    df["YearsCodePro"] = df["YearsCodePro"].apply(cleanYear)
    df['EdLevel'] = df['EdLevel'].apply(clean_education)
    return df

df = load_data()

# Page for exploring the data
def show_explore_page():
    # Adding custom CSS
    st.markdown("""
        <style>
            body {
                background-color: white;
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }
            .title {
                font-size: 36px;
                color: #3498DB;
                text-align: center;
                animation: fadeIn 2s ease-in;
            }
            .subtitle {
                font-size: 24px;
                color: #2C3E50;
                text-align: center;
                margin-top: 20px;
            }
            @keyframes fadeIn {
                0% { opacity: 0; }
                100% { opacity: 1; }
            }
            .stButton button {
                background-color: #1ABC9C;
                color: white;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 8px;
                transition: 0.3s ease;
            }
            .stButton button:hover {
                background-color: #16A085;
            }
            .footer {
                margin-top: 40px;
                text-align: center;
                color: #7F8C8D;
                font-size: 12px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Adding titles with custom animation
    st.markdown("<div class='title'>Explore Software Engineer Salaries</div>", unsafe_allow_html=True)
    st.write("""### Stack Overflow Developer Survey 2024""")
  
    # Pie chart for country distribution
    st.write("""#### Number of Data from Different Countries""")
    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)

    # Bar chart for mean salary by country
    st.write("""#### Mean Salary Based On Country""")
    country_salary_data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(country_salary_data)

    # Line chart for mean salary by years of experience
    st.write("""#### Mean Salary Based On Experience""")
    experience_salary_data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(experience_salary_data)

    # Footer with smooth animation
    st.markdown("""
        <div class='footer'>
            Powered by Streamlit · Data from Stack Overflow Developer Survey
        </div>
    """, unsafe_allow_html=True)

