import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("model_attrition.pkl")  # Ganti dengan model Anda

st.set_page_config(page_title="Prediksi Employee Attrition", layout="centered")
st.title("🧠 Prediksi Employee Attrition")

st.markdown("Masukkan data karyawan untuk memprediksi apakah mereka berpotensi keluar dari perusahaan.")

# Form input
with st.form("prediction_form"):
    age = st.slider("Usia", 18, 60, 30)
    daily_rate = st.number_input("Daily Rate", min_value=100, max_value=2000, value=1100)
    distance_from_home = st.slider("Jarak dari Rumah (km)", 1, 30, 10)
    hourly_rate = st.number_input("Hourly Rate", min_value=10, max_value=150, value=60)
    monthly_income = st.number_input("Monthly Income", min_value=1000, max_value=30000, value=5000)
    monthly_rate = st.number_input("Monthly Rate", min_value=1000, max_value=30000, value=15000)
    num_companies_worked = st.slider("Jumlah Perusahaan Sebelumnya", 0, 10, 2)
    over_time = st.selectbox("Lembur?", ["No", "Yes"])
    total_working_years = st.slider("Total Tahun Bekerja", 0, 40, 10)
    years_at_company = st.slider("Tahun di Perusahaan Sekarang", 0, 40, 5)

    submitted = st.form_submit_button("Prediksi")

# Proses prediksi saat tombol ditekan
if submitted:
    over_time_val = 1 if over_time == "Yes" else 0

    # Urutan fitur sesuai training
    input_data = np.array([[age, daily_rate, distance_from_home, hourly_rate,
                            monthly_income, monthly_rate, num_companies_worked,
                            over_time_val, total_working_years, years_at_company]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.markdown("---")
    if prediction == 1:
        st.error(f"🚨 Karyawan **berisiko keluar** dari perusahaan.")
    else:
        st.success(f"✅ Karyawan **tidak berisiko** keluar.")

    st.markdown(f"**Probabilitas keluar:** `{probability:.2%}`")
