import streamlit as st
import pandas as pd 
from PIL import Image
import numpy as np
import plotly_express as px







st.markdown("# Mall Customer Dataset")



image = Image.open('finalproject/pages_cache/mall.jpeg')
st.image(image, caption='This project is about Mall Customer Segmentation Data. The dataset contains the basic information (ID, Gender, Age, Annual Income, Spending Score) about the customer.')








mall = pd.read_csv("finalproject/Mall_Customers.csv")
st.write(mall)






st.header('In general, how does the amount of annual income an individual makes compare to how much they spend at the mall?')
p=px.line(mall, y="Spending Score (1-100)", x="Annual Income (k$)")
st.plotly_chart(p)

st.caption('Based on this line chart, we can see that people making around 20 thousand have a higher spending score compared to people making 100k+. You would think it would be the other way around but based on this dataset, this is not the case. What is also interesting is the people making around 40-70 thousand. This area of the chart mostly stays at the average spending score amount, there are not as much spikes compared to other areas of the chart.')





def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 ❄️")
    st.sidebar.markdown("# Page 3 ❄️")
