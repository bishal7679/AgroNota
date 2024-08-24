# import streamlit as st
# import pandas as pd
# from functions import train_and_predict_N_category, train_evaluate_random_forest
# from cost import crop
# import webbrowser

# # Load data
# df = pd.read_csv("Crop_recommendation.csv")

# # Define crop options and IDs
# crop_ids = {
#     'rice': 1, 'maize': 2, 'chickpea': 3, 'kidneybeans': 4, 'pigeonpeas': 5,
#     'mothbeans': 6, 'mungbean': 7, 'blackgram': 8, 'lentil': 9, 'pomegranate': 10,
#     'banana': 11, 'mango': 12, 'grapes': 13, 'watermelon': 14, 'muskmelon': 15,
#     'apple': 16, 'orange': 17, 'papaya': 18, 'coconut': 19, 'cotton': 20,
#     'jute': 21, 'coffee': 22
# }

# # Sidebar navigation
# st.sidebar.title("Navigation")
# option = st.sidebar.radio(
#     "Choose a page:", ["Home", "Crop Yield", "Soil Minerals", "Resources"])

# if option == "Home":
#     st.title("Welcome to AgroNota 😊")
#     st.image('assets/logo-2.jpg', width=500)
#     st.write("Agronota predicts by how much you can enrich your precious soil, while informing you of its potential bounty.")
#     st.write("A farmer's dream, manifest ✨")

# elif option == "Crop Yield":
#     st.title("🌾 Crop Yield")

#     with st.form("crop_yield_form"):
#         selected_crop = st.selectbox("Select Crop", list(crop_ids.keys()))
#         grain_weight = st.number_input(
#             "Grain Weight (in pounds)", min_value=0.0)
#         grain_moisture = st.number_input("Grain Moisture (%)", min_value=0.0)
#         harvested_area = st.number_input(
#             "Harvested Area (in square feet)", min_value=0.0)
#         submit_button = st.form_submit_button("Calculate Projected Yield")

#         if submit_button:
#             yield_result = crop(selected_crop, grain_weight,
#                                 grain_moisture, harvested_area)
#             st.write(f"The crop yield for {selected_crop} in the specified conditions is projected to be {
#                      yield_result} megagram per hectare.")

# elif option == "Soil Minerals":
#     st.title("🌱 Predict Optimal Nitrogen Value")

#     with st.form("soil_minerals_form"):
#         humidity = st.number_input("Humidity (%)", min_value=0.0)
#         temperature = st.number_input(
#             "Temperature (°C)", min_value=-50.0, max_value=50.0)
#         rainfall = st.number_input("Rainfall (mm)", min_value=0.0)
#         ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0)
#         selected_crop = st.selectbox("Select Crop", list(crop_ids.keys()))
#         submit_button = st.form_submit_button("Predict Optimal Nitrogen")

#         if submit_button:
#             crop_id = crop_ids[selected_crop]
#             result_n = train_and_predict_N_category(
#                 df, humidity, temperature, rainfall, ph, crop_id)
#             best_practices = train_evaluate_random_forest(
#                 df, result_n, temperature, humidity, ph, rainfall)
#             st.write(f"Optimal Nitrogen content for {
#                      selected_crop}: {result_n}")
#             st.write(f"Recommended for this soil: {best_practices}")

# elif option == "Resources":
#     st.title("📚 Important Links and Resources")

#     if st.button("Soil Testing - MSU"):
#         webbrowser.open("https://homesoiltest.msu.edu/get-started")
#     if st.button("NPK Fertilizer Calculator"):
#         webbrowser.open("https://aesl.ces.uga.edu/soil/fertcalc/")
#     if st.button("United States Department of Agriculture"):
#         webbrowser.open("https://www.usda.gov/")
#     if st.button("Minority and Women Farmers and Ranchers"):
#         webbrowser.open(
#             "https://www.fsa.usda.gov/programs-and-services/farm-loan-programs/minority-and-women-farmers-and-ranchers/index")
#     if st.button("Soil Health Institute"):
#         webbrowser.open("https://soilhealthinstitute.org/")
#     if st.button("How much is too much for the climate?"):
#         webbrowser.open(
#             "https://msutoday.msu.edu/news/2014/how-much-fertilizer-is-too-much-for-the-climate")
        
#     st.write("Made with ❤️")

import streamlit as st
import pandas as pd
from functions import train_and_predict_N_category, train_evaluate_random_forest
from cost import crop
import webbrowser

# Load data
df = pd.read_csv("Crop_recommendation.csv")

# Define crop options and IDs
crop_ids = {
    'rice': 1, 'maize': 2, 'chickpea': 3, 'kidneybeans': 4, 'pigeonpeas': 5,
    'mothbeans': 6, 'mungbean': 7, 'blackgram': 8, 'lentil': 9, 'pomegranate': 10,
    'banana': 11, 'mango': 12, 'grapes': 13, 'watermelon': 14, 'muskmelon': 15,
    'apple': 16, 'orange': 17, 'papaya': 18, 'coconut': 19, 'cotton': 20,
    'jute': 21, 'coffee': 22
}

# Sidebar navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio(
    "Choose a page:", ["Home", "Crop Yield", "Soil Minerals", "Resources"])

if option == "Home":
    st.title("Welcome to AgroNota 😊")
    st.image('assets/logo-2.jpg', width=500)
    st.write("Agronota predicts by how much you can enrich your precious soil, while informing you of its potential bounty.")
    st.write("A farmer's dream, manifest ✨")

elif option == "Crop Yield":
    st.title("🌾 Crop Yield")

    with st.form("crop_yield_form"):
        selected_crop = st.selectbox("Select Crop", list(crop_ids.keys()))
        grain_weight = st.number_input(
            "Grain Weight (in pounds)", min_value=0)
        grain_moisture = st.number_input("Grain Moisture (%)", min_value=0)
        harvested_area = st.number_input(
            "Harvested Area (in square feet)", min_value=0)
        submit_button = st.form_submit_button("Calculate Projected Yield")

        if submit_button:
            yield_result = crop(selected_crop, grain_weight,
                                grain_moisture, harvested_area)
            st.write("The crop yield for {} in the specified conditions is projected to be {} megagram per hectare.".format(
                selected_crop, yield_result))

elif option == "Soil Minerals":
    st.title("🌱 Predict Optimal Nitrogen Value")

    with st.form("soil_minerals_form"):
        humidity = st.number_input("Humidity (%)", min_value=0)
        temperature = st.number_input(
            "Temperature (°C)", min_value=-50, max_value=50)
        rainfall = st.number_input("Rainfall (mm)", min_value=0)
        ph = st.number_input("Soil pH (<=14)", min_value=0, max_value=14)
        selected_crop = st.selectbox("Select Crop", list(crop_ids.keys()))
        submit_button = st.form_submit_button("Predict Optimal Nitrogen")

        if submit_button:
            crop_id = crop_ids[selected_crop]
            result_n = train_and_predict_N_category(
                df, humidity, temperature, rainfall, ph, crop_id)
            best_practices = train_evaluate_random_forest(
                df, result_n, temperature, humidity, ph, rainfall)
            st.write("Optimal Nitrogen content for {}: {}".format(
                selected_crop, result_n))
            st.write("Recommended for this soil: {}".format(best_practices))

elif option == "Resources":
    st.title("📚 Important Links and Resources")

    if st.button("Soil Testing - MSU"):
        webbrowser.open("https://homesoiltest.msu.edu/get-started")
    if st.button("NPK Fertilizer Calculator"):
        webbrowser.open("https://aesl.ces.uga.edu/soil/fertcalc/")
    if st.button("United States Department of Agriculture"):
        webbrowser.open("https://www.usda.gov/")
    if st.button("Minority and Women Farmers and Ranchers"):
        webbrowser.open(
            "https://www.fsa.usda.gov/programs-and-services/farm-loan-programs/minority-and-women-farmers-and-ranchers/index")
    if st.button("Soil Health Institute"):
        webbrowser.open("https://soilhealthinstitute.org/")
    if st.button("How much is too much for the climate?"):
        webbrowser.open(
            "https://msutoday.msu.edu/news/2014/how-much-fertilizer-is-too-much-for-the-climate")

    st.write("Made with ❤️")
