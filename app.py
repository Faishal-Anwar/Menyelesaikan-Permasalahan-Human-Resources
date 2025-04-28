import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('xgb_attrition_model.pkl')  # Sesuaikan nama file modelmu

st.title('🚀 Prediksi Attrition Karyawan')

st.subheader('📋 Masukkan Data Karyawan (10 Fitur Terpilih)')

# Form input untuk 10 fitur
age = st.number_input('Umur', min_value=18, max_value=60, value=30)
daily_rate = st.number_input('Daily Rate', min_value=100, max_value=1500, value=500)
distance_from_home = st.number_input('Distance From Home', min_value=1, max_value=50, value=10)
hourly_rate = st.number_input('Hourly Rate', min_value=30, max_value=100, value=60)
monthly_income = st.number_input('Monthly Income', min_value=1000, max_value=20000, value=5000)
monthly_rate = st.number_input('Monthly Rate', min_value=2000, max_value=30000, value=15000)
over_time = st.selectbox('Over Time (0=No, 1=Yes)', [0, 1])
percent_salary_hike = st.number_input('Percent Salary Hike', min_value=0, max_value=100, value=15)
total_working_years = st.number_input('Total Working Years', min_value=0, max_value=40, value=10)
years_at_company = st.number_input('Years at Company', min_value=0, max_value=40, value=5)

# Prediksi
if st.button('Prediksi'):
    input_df = pd.DataFrame({
        'age': [age],
        'daily_rate': [daily_rate],
        'distance_from_home': [distance_from_home],
        'hourly_rate': [hourly_rate],
        'monthly_income': [monthly_income],
        'monthly_rate': [monthly_rate],
        'over_time': [over_time],
        'percent_salary_hike': [percent_salary_hike],
        'total_working_years': [total_working_years],
        'years_at_company': [years_at_company]
    })

    # Prediksi
    pred = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0]

    st.subheader('📈 Hasil Prediksi:')
    st.write(f"Attrition: **{'Yes' if pred == 1 else 'No'}**")
    st.write(f"Confidence Score: **{round(max(proba)*100, 2)}%**")
