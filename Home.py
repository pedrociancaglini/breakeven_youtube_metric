import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Function to calculate breakeven point
def calculate_breakeven(current_subs, daily_subs, sub_growth_rate, current_hours, daily_hours, hour_growth_rate):
    days = 0
    while current_subs < 1000 or current_hours < 4000:
        current_subs += daily_subs
        current_hours += daily_hours
        
        # Apply growth rates
        daily_subs *= (1 + sub_growth_rate / 100)
        daily_hours *= (1 + hour_growth_rate / 100)
        
        days += 1
        
    breakeven_date = datetime.now() + timedelta(days=days)
    return days, breakeven_date

# Streamlit App
st.title("YouTube Breakeven Point Calculator")

# Sidebar inputs
st.sidebar.header("Current Stats")
current_subs = st.sidebar.number_input("Current Subscribers", min_value=0, value=100)
current_hours = st.sidebar.number_input("Current Watch Hours", min_value=0.0, value=50.0)

st.sidebar.header("Daily Growth")
daily_subs = st.sidebar.number_input("Daily New Subscribers", min_value=0.0, value=10.0)
sub_growth_rate = st.sidebar.number_input("Subscriber Growth Rate (%)", min_value=0.0, value=2.0)
daily_hours = st.sidebar.number_input("Daily New Watch Hours", min_value=0.0, value=2.0)
hour_growth_rate = st.sidebar.number_input("Watch Hour Growth Rate (%)", min_value=0.0, value=2.0)

# Calculate breakeven point
days, breakeven_date = calculate_breakeven(current_subs, daily_subs, sub_growth_rate, current_hours, daily_hours, hour_growth_rate)

# Display results
st.header("Results")
st.write(f"It will take approximately {days} days to reach 1000 subscribers and 4000 watch hours.")
st.write(f"Estimated Breakeven Date: {breakeven_date.strftime('%Y-%m-%d')}")

