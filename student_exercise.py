import pandas as pd
import streamlit as st
import plotly.express as px

st.title("In Search for Happiness")
df = pd.read_csv("happy.csv")



choose = st.selectbox("Select for X-axis", ("Happiness", "GDP", "SOCIAL_SUPPORT"))

choose1 = st.selectbox("Select for Y-axis", ("Happiness", "GDP", "CORRUPTION"))

a  = choose.lower()
b = choose1.lower()

figure = px.scatter(x=df[a], y=df[b], labels={"x":f"{choose}", "y":f"{choose1}"})
st.plotly_chart(figure)