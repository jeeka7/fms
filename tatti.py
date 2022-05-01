import streamlit as st
import pandas as pd
import numpy as np

st.write("List of waitlisted candidates of 2022 FMS batch")
waitlisted=pd.read_csv("https://raw.githubusercontent.com/jeeka7/fms/main/MBAFT_WAITLIST_PWD_2022.csv")
pwd1=waitlisted.loc[waitlisted["Category"]=="PWD1"]
pwd2=waitlisted.loc[waitlisted["Category"]=="PWD2"]
pwd3=waitlisted.loc[waitlisted["Category"]=="PWD3"]
pwd4=waitlisted.loc[waitlisted["Category"]=="PWD4"]
pwd5=waitlisted.loc[waitlisted["Category"]=="PWD5"]
pwd6=waitlisted.loc[waitlisted["Category"]=="PWD6"]
#df.loc[df['column_name'] == some_value]
st.write(waitlisted)
option = st.selectbox('what category you wnt to see?',('pwd1', 'pwd2', 'pwd3','pwd4','pwd5','pwd6'))
st.write('You selected:', option)
if option=='pwd1':
	st.write(pwd1)
if option=='pwd2':
	st.write(pwd2)
if option=='pwd3':
	st.write(pwd3)
if option=='pwd4':
	st.write(pwd4)
if option=='pwd5':
	st.write(pwd5)
if option=='pwd6':
	st.write(pwd6)
