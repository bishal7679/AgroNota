# import streamlit as st
# import pandas as pd
# from functions import train_and_predict_N_category, train_and_predict_K_category, train_and_predict_P_category, train_evaluate_random_forest
# from cost import crop

# # Load data
# df = pd.read_csv("Crop_recommendation.csv")

# # Check DataFrame columns
# required_columns = ['N_category', 'K_category', 'P_category']
# missing_columns = [col for col in required_columns if col not in df.columns]

# if missing_columns:
#     st.error(
#         f"Error: Missing columns {', '.join(missing_columns)} in the DataFrame.")
# else:
#     st.write("DataFrame columns:", df.columns)

# # Sidebar navigation
# st.sidebar.title("Navigation")
# option = st.sidebar.radio(
#     "Choose a page:", ["Home", "Crop Yield", "Soil Minerals", "Resources"])

# if option == "Home":
#     st.title("Welcome to AgroNota 😊")
#     st.image('assets/logo-2.jpg', use_column_width=True)
#     st.write("Agronota predicts by how much you can enrich your precious soil, while informing you of its potential bounty.")
#     st.write("A farmer's dream, manifest.")

# elif option == "Crop Yield":
#     st.title("Crop Yield")

#     with st.form("crop_yield_form"):
#         selected_crop = st.selectbox("Select Crop", ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans', 'mungbean', 'blackgram', 'lentil',
#                             'pomegranate', 'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee'])
#         grain_weight = st.number_input(
#             "Grain Weight (in pounds)", min_value=0.0)
#         grain_moisture = st.number_input("Grain Moisture (%)", min_value=0.0)
#         harvested_area = st.number_input(
#             "Harvested Area (in square feet)", min_value=0.0)

#         submit_button = st.form_submit_button("Calculate Projected Yield")

#         if submit_button:
#             yield_result = crop(selected_crop, grain_weight,
#                                 grain_moisture, harvested_area)
#             st.write(f"Projected Yield: {yield_result} bushels")

# elif option == "Soil Minerals":
#     st.title("Soil Minerals")

#     with st.form("soil_minerals_form"):
#         humidity = st.number_input("Humidity (%)", min_value=0.0)
#         temperature = st.number_input(
#             "Temperature (°C)", min_value=-50.0, max_value=50.0)
#         rainfall = st.number_input("Rainfall (mm)", min_value=0.0)
#         ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0)
#         crop_id = st.selectbox("Select Crop", df['label'].unique())

#         submit_button = st.form_submit_button("Predict Optimal Nitrogen")

#         if submit_button:
#             try:
#                 result_n = train_and_predict_N_category(
#                     df, humidity, temperature, rainfall, ph, crop_id)
#                 st.write(f"Predicted Nitrogen Category: {result_n}")

#                 result_k = train_and_predict_K_category(
#                     df, humidity, temperature, rainfall, ph, crop_id)
#                 st.write(f"Predicted Potassium Category: {result_k}")

#                 result_p = train_and_predict_P_category(
#                     df, humidity, temperature, rainfall, ph, crop_id)
#                 st.write(f"Predicted Phosphorus Category: {result_p}")
#             except KeyError as e:
#                 st.error(f"KeyError: {e}")

# elif option == "Resources":
#     st.title("Important Links and Resources")

#     if st.button("Soil Testing - MSU"):
#         st.write("Link to Soil Testing - MSU")
#     if st.button("NPK Fertilizer Calculator"):
#         st.write("Link to NPK Fertilizer Calculator")
#     if st.button("United States Department of Agriculture"):
#         st.write("Link to USDA")
#     if st.button("Minority and Women Farmers and Ranchers"):
#         st.write("Link to Minority and Women Farmers and Ranchers")
#     if st.button("Soil Health Institute"):
#         st.write("Link to Soil Health Institute")
#     if st.button("How much is too much for the climate?"):
#         st.write("Link to Climate Impact Information")

import streamlit as st
import pandas as pd
from functions import train_and_predict_N_category, train_and_predict_K_category, train_and_predict_P_category, train_evaluate_random_forest
from cost import crop

# Load data
df = pd.read_csv("Crop_recommendation.csv")

# Check DataFrame columns
required_columns = ['N', 'K', 'P']
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    st.error(f"Error: Missing columns {
             ', '.join(missing_columns)} in the DataFrame.")
else:
    st.write("DataFrame columns:", df.columns)

# Sidebar navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio(
    "Choose a page:", ["Home", "Crop Yield", "Soil Minerals", "Resources"])

if option == "Home":
    st.title("Welcome to AgroNota 😊")
    st.image('assets/logo-2.jpg', use_column_width=True)
    st.write("Agronota predicts by how much you can enrich your precious soil, while informing you of its potential bounty.")
    st.write("A farmer's dream, manifest.")

elif option == "Crop Yield":
    st.title("Crop Yield")

    with st.form("crop_yield_form"):
        selected_crop = st.selectbox("Select Crop", ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans', 'mungbean', 'blackgram', 'lentil',
                                                     'pomegranate', 'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee'])
        grain_weight = st.number_input(
            "Grain Weight (in pounds)", min_value=0.0)
        grain_moisture = st.number_input("Grain Moisture (%)", min_value=0.0)
        harvested_area = st.number_input(
            "Harvested Area (in square feet)", min_value=0.0)

        submit_button = st.form_submit_button("Calculate Projected Yield")

        if submit_button:
            yield_result = crop(selected_crop, grain_weight,
                                grain_moisture, harvested_area)
            st.write(f"Projected Yield: {yield_result} bushels")

elif option == "Soil Minerals":
    st.title("Soil Minerals")

    with st.form("soil_minerals_form"):
        humidity = st.number_input("Humidity (%)", min_value=0.0)
        temperature = st.number_input(
            "Temperature (°C)", min_value=-50.0, max_value=50.0)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0)
        ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0)
        crop_id = st.selectbox("Select Crop", df['label'].unique())

        submit_button = st.form_submit_button("Predict Optimal Nitrogen")

        if submit_button:
            if not all(col in df.columns for col in ['N', 'K', 'P']):
                st.error(
                    "Required columns for prediction are missing in the DataFrame.")
            else:
                try:
                    result_n = train_and_predict_N_category(
                        df, humidity, temperature, rainfall, ph, crop_id)
                    st.write(f"Predicted Nitrogen Category: {result_n}")

                    result_k = train_and_predict_K_category(
                        df, humidity, temperature, rainfall, ph, crop_id)
                    st.write(f"Predicted Potassium Category: {result_k}")

                    result_p = train_and_predict_P_category(
                        df, humidity, temperature, rainfall, ph, crop_id)
                    st.write(f"Predicted Phosphorus Category: {result_p}")
                except KeyError as e:
                    st.error(f"KeyError: {e}")

elif option == "Resources":
    st.title("Important Links and Resources")

    if st.button("Soil Testing - MSU"):
        st.write("Link to Soil Testing - MSU")
    if st.button("NPK Fertilizer Calculator"):
        st.write("Link to NPK Fertilizer Calculator")
    if st.button("United States Department of Agriculture"):
        st.write("Link to USDA")
    if st.button("Minority and Women Farmers and Ranchers"):
        st.write("Link to Minority and Women Farmers and Ranchers")
    if st.button("Soil Health Institute"):
        st.write("Link to Soil Health Institute")
    if st.button("How much is too much for the climate?"):
        st.write("Link to Climate Impact Information")
