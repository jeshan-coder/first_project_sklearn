#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:41:22 2025

@author: jeshan
"""
import streamlit as st

# Page title
st.title("Mobile Phone Data Documentation")

# Section: Metadata
st.header("Metadata Description")
st.divider()
# Dictionary containing column names as keys and their descriptions as values
columns_info = {
    "battery_power": "Total energy a battery can store in one time, measured in mAh.",
    "blue": "Indicates whether the phone has Bluetooth capability.",
    "clock_speed": "Speed at which the microprocessor executes instructions.",
    "dual_sim": "Indicates if the phone supports dual SIM.",
    "fc": "Front camera resolution in megapixels.",
    "four_g": "Indicates if the phone supports 4G.",
    "int_memory": "Internal memory in Gigabytes.",
    "m_dep": "Mobile depth in centimeters.",
    "mobile_wt": "Weight of the mobile phone.",
    "n_cores": "Number of cores in the processor.",
    "pc": "Primary camera resolution in megapixels.",
    "px_height": "Pixel resolution height.",
    "px_width": "Pixel resolution width.",
    "ram": "Random Access Memory in Mega Bytes.",
    "sc_h": "Screen height of the mobile in centimeters.",
    "sc_w": "Screen width of the mobile in centimeters.",
    "talk_time": "Longest time that a single battery charge will last when talking.",
    "three_g": "Indicates if the phone supports 3G.",
    "touch_screen": "Indicates if the phone has a touch screen.",
    "wifi": "Indicates if the phone has WiFi connectivity.",
    "price_range": "Target variable that categorizes the phone's price range."
}

# Loop through the dictionary and display each column as a subheading with its description
for column, description in columns_info.items():
    st.subheader(column)
    st.write(description)
    st.divider()

