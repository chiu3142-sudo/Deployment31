


import joblib
import streamlit as st

import numpy as np
model = joblib.load("housing_price_model.pkl")
st.title("Housing  Price Prediction ")
st.write("Enter the input and hit predict to get a estimate price for your house")


#2

area_sqft = st.number_input("Area (sqft)",min_value = 200.0,max_value=10000.0, value=1200.0, step=50.0)
bedrooms = st.number_input("bedrooms",min_value = 1,max_value=10, value=1, step=1)
bathrooms  = st.number_input("bathrooms",min_value = 1,max_value=10, value=1, step=1)
age_years = st.number_input("age_years(year)",min_value = 0.0,max_value=100.0, value=10.0, step=1.0)
distance_city_km = st.number_input("distance_city_km(KM)",min_value = 0.1,max_value=600.0, value=12.0, step=0.5)

# predict

if st.button("Predict Price"):
  x=np.array([["area_sqft","bedrooms","bathrooms","age_years","distance_city_km"]])
  pred=model.predict(x)[0]
  st.success(f"Estimated Price: {pred:.2f} lakhs")
