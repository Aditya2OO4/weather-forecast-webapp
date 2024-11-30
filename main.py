import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ",help="Enter city name")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for next {days} days in {place}")

#Graph
def get_days(days):
    dates = ["2024-1-11", "2024-2-11", "2024-3-1"]
    temperature = [10, 11, 15]
    temperature = [days * i for i in temperature]
    return dates, temperature

d, t = get_days(days)
figure = px.line(x=d, y=t, labels={"x":"Date", "y":"Temperature (C)"})
st.plotly_chart(figure)

