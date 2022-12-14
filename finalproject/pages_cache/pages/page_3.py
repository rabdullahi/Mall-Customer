import streamlit as st
import pandas as pd 
from PIL import Image
import numpy as np
import plotly_express as px






mall = pd.read_csv("finalproject/Mall_Customers.csv")

st.title('Annual Income')
st.header('Bar Graph by Age and Annual Income')







m=px.bar(mall, x="Age", y="Annual Income (k$)", color="Annual Income (k$)")
st.plotly_chart(m)

st.caption('In general, people in their 30s on average have a higher annual income. Individuals who are 60+ have a lower annual income in comparison to other ages. ')



st.header('Box Plot by Gender and Annual Income')

z=px.box(mall, x="Gender", y="Annual Income (k$)", points="all", color="Gender")
st.plotly_chart(z)

st.caption('The average annual income for male is slightly higher compared to females. Based on the range, the annual income is more dispersed for males.')
