#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:33:44 2025

@author: jeshan
"""
import streamlit as st
import pandas as pd
import numpy as np

st.title("Mobile price prediction")


col1,col2,col3,col4=st.columns(4)

# numerical columns
with col1:
    battery_power=st.number_input("Battery Power")#1

with col2:
    clock_speed=st.number_input("Clock speed")

with col3:
    fc=st.number_input("Front camera (FC)")
    
with col4:
    int_memory=st.number_input("Internal Memory")
    



st.divider()

col5,col6,col7,col8=st.columns(4)



with col5:
    m_dep=st.number_input("Mobile Depth (m_dep)")
    
with col6:
    mobile_wt=st.number_input("Mobile Weight")

with col7:
    n_cores=st.number_input("No. of cores(n_cores)")

with col8:
    pc=st.number_input("Primary Camera(pc)")
    
st.divider()

col9,col10,col11,col12=st.columns(4)

with col9:
    px_height=st.number_input("Pixel Height(px_height)")

with col10:
    px_width=st.number_input("Pixel Width(px_width)")

with col11:
    ram=st.number_input("Ram")

with col12:
    sc_h=st.number_input("Screen Height(sc_h)")
    
#categorical columns
st.divider()
col13,col14=st.columns(2)

with col13:
    sc_w=st.number_input("screen Width(sc_w)")

with col14:
    talk_time=st.number_input("Talk Time(talk_time)")

st.divider()
col15,col16=st.columns(2)

with col15:
    blue=st.toggle("Bluetooth(Blue)")
    if blue:
        st.write("Bluetooth exists !")
    dual_sim=st.toggle("Dual SIM")
    if dual_sim:
        st.write("Dual sim exists !")
    four_g=st.toggle("Four G")
    if four_g:
        st.write("Four G exists !")

st.divider()

with col16:
    three_g=st.toggle("Three G")
    if three_g:
        st.write("Three G exists !")
    touch_screen=st.toggle("Touch Screen")
    if touch_screen:
        st.write("Touch screen exists !")
    wifi=st.toggle("WIFI")
    if wifi:
        st.write(f"WIFi exists ! {wifi}")
        
#categories_columns
#['blue', 'dual_sim', 'four_g', 'three_g', 'touch_screen', 'wifi']
 
#numerical columns
#['battery_power', 'clock_speed', 'fc', 'int_memory', 'm_dep',
#      'mobile_wt', 'n_cores', 'pc', 'px_height', 'px_width', 'ram', 'sc_h',
#      'sc_w', 'talk_time']

#order of columns
#['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g',
 #      'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height',
#       'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g',
 #      'touch_screen', 'wifi', 'price_range']

#haldling categories
'blue', 'dual_sim', 'four_g', 'three_g', 'touch_screen', 'wifi'
if blue:
    blue='yes'
blue='no'

if dual_sim:
    dual_sim='yes'
dual_sim='no'

if four_g:
    four_g='yes'
four_g='no'

if three_g:
    three_g='yes'
three_g='no'

if touch_screen:
    touch_screen='yes'
touch_screen='no'

if wifi:
    wifi='yes'
wifi='no'

import pandas as pd


col16,col17,col18=st.columns([1,2,1])


predict=st.button("predeict")


from inference import inference
if predict:
    input_values={''
        'battery_power':[battery_power], 
                  'blue':[blue], 
                  'clock_speed':[clock_speed], 
                  'dual_sim':[dual_sim], 
                  'fc':[fc],'four_g':[four_g],
              'int_memory':[int_memory],
              'm_dep':[m_dep], 
              'mobile_wt':[mobile_wt], 
              'n_cores':[n_cores], 
              'pc':[pc], 
              'px_height':[px_height],
              'px_width':[px_width], 
              'ram':[ram], 
              'sc_h':[sc_h], 
              'sc_w':[sc_w], 
              'talk_time':[talk_time], 
              'three_g':[three_g],
              'touch_screen':[touch_screen],
              'wifi':[wifi]
              }
    input_df=pd.DataFrame(input_values)
    
    result=inference(input_df)
    st.write(result)
    






    
    
    
    



    
    

