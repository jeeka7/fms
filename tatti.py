import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

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
	st.write(len(pwd1.index),"people were selected in this category",)
if option=='pwd2':
	st.write(pwd2)
	st.write(len(pwd2.index),"people were selected in this category",)
if option=='pwd3':
	st.write(pwd3)
	st.write(len(pwd3.index),"people were selected in this category",)
if option=='pwd4':
	st.write(pwd4)
	st.write(len(pwd4.index),"people were selected in this category",)
if option=='pwd5':
	st.write(pwd5)
	st.write(len(pwd5.index),"people were selected in this category",)
if option=='pwd6':
	st.write(pwd6)
	st.write(len(pwd6.index),"people were selected in this category",)
details = {
    'Category' : ['PWD1', 'PWD2', 'PWD3', 'PWD4','PWD5','PWD6'],
    'Total Students' : [len(pwd1.index), len(pwd2.index), len(pwd3.index), len(pwd4.index),len(pwd5.index),len(pwd6.index)],
}
students = pd.DataFrame(details)
st.write(students)
pie_chart = px.pie(students,
                title='Viklaang LOG',
                values='Total Students',
                names='Category')

st.plotly_chart(pie_chart)
