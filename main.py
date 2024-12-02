import streamlit as st
import plotly.express as px

from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ",help="Enter city name")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for next {days} day(s) in {place}")

#Get temperature data


if place:
    try:
        filtered_data = get_data(place, days)
        #Create temperature plot
        if option == "Temperature":
            temperature = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperature, labels={"x":"Date", "y":"Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            num_columns = 6
            cols = st.columns(num_columns)

            for i, image_path in enumerate(image_paths):
                col_index = i % num_columns  # Determine the column to use
                with cols[col_index]:
                    st.image(image_path, width=115)
                    dates = [dict["dt_txt"] for dict in filtered_data]
                    st.write(dates[0])
    except KeyError:
        st.info("You Entered a NON-EXISTING Place!!! " "\n" "OR" "\n" "WE DONT HAVE DATA FOR THAT PLACE.")