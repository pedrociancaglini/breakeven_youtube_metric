import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Function to calculate daily growth rate
def calculate_growth_rate(historical_data):
    daily_growth_rate = (historical_data[-1] - historical_data[0]) / len(historical_data) / historical_data[0] * 100
    return daily_growth_rate

# Function to calculate breakeven point
def calculate_breakeven(current_subs, daily_subs, sub_growth_rate, current_hours, daily_hours, hour_growth_rate):
    days = 0
    subs_list = [current_subs]
    hours_list = [current_hours]
    while current_subs < 1000 or current_hours < 4000:
        current_subs += daily_subs
        current_hours += daily_hours
        
        # Apply growth rates
        daily_subs *= (1 + sub_growth_rate / 100)
        daily_hours *= (1 + hour_growth_rate / 100)
        
        days += 1
        subs_list.append(current_subs)
        hours_list.append(current_hours)
        
    breakeven_date = datetime.now() + timedelta(days=days)
    return days, breakeven_date, subs_list, hours_list

# Streamlit App
st.title("YouTube Breakeven Point Calculator")

# Sidebar inputs
st.sidebar.header("Current Stats")
current_subs = st.sidebar.number_input("Current Subscribers", min_value=0, value=100)
current_hours = st.sidebar.number_input("Current Watch Hours", min_value=0.0, value=50.0)

st.sidebar.header("Daily Growth")
daily_subs = st.sidebar.number_input("Daily New Subscribers", min_value=0.0, value=10.0)
daily_hours = st.sidebar.number_input("Daily New Watch Hours", min_value=0.0, value=2.0)

st.sidebar.header("Historical Data")
historical_subs = st.sidebar.text_area("Historical Subscribers (comma-separated)", "100,110,120,130,140")
historical_hours = st.sidebar.text_area("Historical Watch Hours (comma-separated)", "50,52,54,56,58")

# Convert historical data from text input to list of floats
historical_subs = list(map(int, historical_subs.split(',')))
historical_hours = list(map(float, historical_hours.split(',')))

# Calculate growth rates based on historical data
sub_growth_rate = calculate_growth_rate(historical_subs)
hour_growth_rate = calculate_growth_rate(historical_hours)

# Calculate breakeven point
days, breakeven_date, subs_list, hours_list = calculate_breakeven(current_subs, daily_subs, sub_growth_rate, current_hours, daily_hours, hour_growth_rate)

# Display results
st.header("Results")
st.write(f"It will take approximately {days} days to reach 1000 subscribers and 4000 watch hours.")
st.write(f"Estimated Breakeven Date: {breakeven_date.strftime('%Y-%m-%d')}")

# Plot the forecast
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# Plot subscribers forecast
ax[0].plot(subs_list, label="Subscribers")
ax[0].axhline(1000, color='r', linestyle='--', label="Target 1000 Subscribers")
ax[0].set_title("Subscribers Growth Forecast")
ax[0].set_xlabel("Days")
ax[0].set_ylabel("Subscribers")
ax[0].legend()

# Plot watch hours forecast
ax[1].plot(hours_list, label="Watch Hours")
ax[1].axhline(4000, color='r', linestyle='--', label="Target 4000 Watch Hours")
ax[1].set_title("Watch Hours Growth Forecast")
ax[1].set_xlabel("Days")
ax[1].set_ylabel("Watch Hours")
ax[1].legend()

# Display the plot in Streamlit
st.pyplot(fig)
