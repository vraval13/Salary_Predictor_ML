import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2E8B57, #6B8E23);
        color: white;
    }
    .stButton button {
        background-color: #008CBA;
        border: none;
        color: white;
        padding: 12px 24px;
        text-align: center;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #005f6b;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        animation: fadeIn 2s ease-in-out;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# Title with animation
st.markdown("<div class='title'>Salary Prediction and Exploration</div>", unsafe_allow_html=True)

# Sidebar with navigation options
page = st.sidebar.selectbox("Choose an option:", ("Predict", "Explore"))

# Add a progress bar to simulate loading
st.sidebar.progress(70)

# Adding a nice image or logo (optional)
st.sidebar.image("https://images.pexels.com/photos/27916602/pexels-photo-27916602/free-photo-of-a-man-on-a-motorcycle-is-sitting-in-the-middle-of-a-street.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", use_column_width=True)

# Interactive content based on page selection
if page == "Predict":
    st.write("## Welcome to the Salary Predictor!")
    show_predict_page()
else:
    st.write("## Welcome to the Explore Section!")
    show_explore_page()

# Footer with smooth animations
st.markdown("""
    <footer style="text-align: center; margin-top: 50px;">
        <p style="font-size:14px; font-weight:bold; color:#808080;">
            Made with ❤️ using Streamlit by Vyom Raval
        </p>
    </footer>
""", unsafe_allow_html=True)
