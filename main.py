import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from src.transformers import CombinedAttributesAdder

# Data Information: 
# Median Income is scaled and capped (0.5 to 15.0) in the original dataset.
# A value of 3.0 represents $30,000. 

# Load model and pipeline
@st.cache_resource
def load_model():
    base_dir = os.path.dirname(__file__)
    model_path = os.path.join(base_dir, "model", "housing_pipeline.pkl")
    pipeline = joblib.load(model_path)
    return pipeline

def main():
    st.set_page_config(page_title="California Housing Prediction", layout="wide")
    
    st.title("🏡 California Housing Price Prediction")
    st.markdown("""
    This app predicts the **Median House Value** in California based on various features.
    """)

    st.sidebar.header("User Input Features")

    def user_input_features():
        longitude = st.sidebar.slider("Longitude", -124.35, -114.31, -124.35)
        latitude = st.sidebar.slider("Latitude", 32.54, 41.95, 32.54)
        housing_median_age = st.sidebar.slider("Housing Median Age", 1.0, 52.0, 28.0)
        total_rooms = st.sidebar.number_input("Total Rooms", 2, 40000, 2)
        total_bedrooms = st.sidebar.number_input("Total Bedrooms", 1, 6500, 1)
        population = st.sidebar.number_input("Population", 3, 36000, 3)
        households = st.sidebar.number_input("Households", 1, 6200, 1)
        
        # Input in actual dollars
        actual_income = st.sidebar.number_input("Median Income (in $)", min_value=5000, max_value=200000, value=35000, step=1000)
        # Scale it for the model (e.g., $35,000 becomes 3.5)
        median_income = actual_income / 10000.0
        ocean_proximity = st.sidebar.selectbox("Ocean Proximity", 
                                             ("<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"))
        
        data = {
            'longitude': longitude,
            'latitude': latitude,
            'housing_median_age': housing_median_age,
            'total_rooms': total_rooms,
            'total_bedrooms': total_bedrooms,
            'population': population,
            'households': households,
            'median_income': median_income,
            'ocean_proximity': ocean_proximity
        }
        features = pd.DataFrame(data, index=[0])
        return features

    input_df = user_input_features()

    st.subheader("User Input Parameters")
    st.write(input_df)

    try:
        pipeline = load_model()
        
        # Preparation and Prediction
        prediction = pipeline.predict(input_df)

        st.subheader("Prediction")
        st.write(f"### Predicted Median House Value: **${prediction[0]:,.2f}**")
        
    except FileNotFoundError:
        st.error("Model files not found. Please run 'train_and_export.py' first.")

if __name__ == "__main__":
    main()