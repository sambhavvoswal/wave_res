import streamlit as st
import pandas as pd
from datetime import datetime
import re
import time

# Load data from Excel file
def load_data(file):
    data = pd.read_excel(file)
    return data

# Function to display countdown timer
def countdown_timer(target_time):
    remaining_time = target_time - datetime.now()
    days, seconds = remaining_time.days, remaining_time.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{days}d {hours:02d}:{minutes:02d}:{seconds:02d}"

# Set up Streamlit page
st.set_page_config(page_title="🌊 WAVE 2.0 Result Card 🌊", layout="centered")
st.markdown(
    """
    <style>
    @keyframes fadeIn {
      0% { opacity: 0; }
      100% { opacity: 1; }
    }

    .animated-header {
        animation: fadeIn 3s ease-in-out;
        font-size: 3em;
        font-weight: bold;
        text-align: center;
        color: #007BFF;
    }

    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
    }

    .result-text {
        font-size: 1.5em;
        margin: 10px 0;
    }

    .centered-countdown {
        font-size: 2em;
        text-align: center;
        color: #FF5733;
        margin-top: 20px;
    }

    .countdown-header {
        animation: fadeIn 3s ease-in-out;
        font-size: 2em;
        text-align: center;
        font-weight: bold;
        color: #007BFF;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<div class="animated-header">🌊 WAVE 2.0 Result Card 🌊</div>', unsafe_allow_html=True)

# Load the Excel data
data_file = 'result.xlsx'
data = load_data(data_file)

# User input for passcode verification
user_input = st.text_input("Enter your 4-character passcode (letters and numbers):")

# Validate that the passcode is exactly 4 characters long and contains only letters and numbers
if user_input and re.match("^[A-Za-z0-9]{4}$", user_input):
    if user_input in data['code'].values:
        row = data[data['code'] == user_input]
        st.markdown('<div class="result-text">Here are your results:</div>', unsafe_allow_html=True)
        # Extract the values from the respective columns without displaying the column names
        try:
            one = row['p1'].values[0]
            two = row['p2'].values[0]
            three = row['p3'].values[0]

            # Calculate the total marks and percentage
            total_marks = one + two + three
            percentage = (total_marks / 150) * 100

            # Display the results with increased font size
            st.markdown(f'<div class="result-text">1st round: {one}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-text">2nd round: {two}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-text">3rd round: {three}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-text">Total Marks: {total_marks}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-text">Percentage: {percentage:.2f}%</div>', unsafe_allow_html=True)
        except KeyError as e:
            st.write(f"Error: {e}. Please check the column names in your Excel file.")
    else:
        st.write("Invalid passcode. Please try again.")
elif user_input:
    st.write("Passcode must be exactly 4 characters long and contain only letters and numbers. Please try again.")

# Countdown timer for 12:00 PM, 2nd July 2024
end_time = datetime(2024, 7, 2, 12, 0, 0)
st.markdown('<div class="countdown-header">⏳ Hackathon Countdown ⏳</div>', unsafe_allow_html=True)
timer_placeholder = st.empty()

while datetime.now() < end_time:
    timer_placeholder.markdown(f'<b><div class="centered-countdown">{countdown_timer(end_time)}</div></b>', unsafe_allow_html=True)
    time.sleep(1)

# Add footer
st.markdown(
    """
    <div class="footer">
        <p>Powered by the WAVE Hackathon Team</p>
    </div>
    """, unsafe_allow_html=True
)
