import streamlit as st
import pandas as pd 
from PIL import Image
import numpy as np
import plotly_express as px






mall = pd.read_csv("/Users/saldana/Documents/streamlit_env/finalproject/Mall_Customers.csv")



st.title('Spending Score')
st.header('Scatter Plot by Age and Spending Score')



a= px.scatter(mall, x="Age", y="Spending Score (1-100)")
st.plotly_chart(a)


st.caption('From this scatter plot, we can see that people who are older than 40 years old tend to have a lower spending score compared to those who are younger. This can be due to wanting to buy items online rather than visiting the mall.')




st.header('Box Plot by Gender and Spending Score')

g=px.box(mall, x="Gender", y="Spending Score (1-100)", points="all", color="Gender")

st.plotly_chart(g)

st.caption('The spending score between male and female are the same. However males have a bigger range for spending score compared to females.')
