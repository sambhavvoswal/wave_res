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
st.set_page_config(page_title="WAVE 2.0 Result Card", layout="centered")
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
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<div class="animated-header">WAVE 2.0 Result Card</div>', unsafe_allow_html=True)

# Load the Excel data
data_file = 'result.xlsx'
data = load_data(data_file)

# User input for passcode verification
user_input = st.text_input("Enter your 4-character passcode (only letters):")

# Validate that the passcode is exactly 4 characters long and contains only letters
if user_input and re.match("^[A-Za-z0-9]{4}$", user_input):
    if user_input in data['code'].values:
        row = data[data['code'] == user_input]
        st.write("Here are your results:")
        st.write(row[['1p1', '1p2', '1p3', '1p4', '1p5']])
    else:
        st.write("Invalid passcode. Please try again.")
elif user_input:
    st.write("Passcode must be exactly 4 characters long and appropiatee. Please try again.")

# Countdown timer for 12:00 PM, 2nd July 2024
end_time = datetime(2024, 7, 2, 12, 0, 0)
st.subheader("⏳ Hackathon Countdown")
timer_placeholder = st.empty()

while datetime.now() < end_time:
    timer_placeholder.markdown(f"<h2>{countdown_timer(end_time)}</h2>", unsafe_allow_html=True)
    time.sleep(1)

# Add footer
st.markdown(
    """
    <div class="footer">
        <p>Powered by the WAVE Hackathon Team</p>
    </div>
    """, unsafe_allow_html=True
)
