# Proyek Akhir: Menyelesaikan Permasalahan Human Resources di Perusahaan Jaya Jaya Maju

## Business Understanding

**Jaya Jaya Maju** adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan. Perusahaan ini menghadapi tantangan dalam hal tingginya tingkat *attrition* (pergantian karyawan), yang berdampak negatif terhadap operasional dan biaya.

## Permasalahan Bisnis

- Tingginya tingkat attrition (>10%) menyebabkan gangguan produktivitas dan beban rekrutmen baru.
- Tidak adanya alat prediktif untuk mendeteksi karyawan yang berpotensi resign.
- Perlu solusi berbasis data untuk pengambilan keputusan di departemen HR.

## Cakupan Proyek

- Analisis faktor-faktor penyebab attrition.
- Visualisasi data dan insight melalui **Tableau Public**.
- Pembuatan model machine learning menggunakan algoritma Machine Learning.
- Deployment model menggunakan streamlit untuk bisa memprediksi secara daring.

## Persiapan

### Sumber Data
Dataset diambil dari:  
🔗 [Employee Data - GitHub](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

## Dashboard Analitik - Tableau Public
untuk link dashboard bisa diakses melalui

link dashboard 1 : [link dashboard 11](https://public.tableau.com/views/JayaJayaMajuDicoding/Dashboard3?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

link dashboard 2 : [link dashboard 2](https://public.tableau.com/views/JayaJayaMajuDicoding2/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

![image](https://github.com/user-attachments/assets/24963151-707c-43b6-8540-8d008e210d54)
![image](https://github.com/user-attachments/assets/c3c43c23-1ace-4c3f-8efa-d20b75741ade)



Komponen Dashboard:

- Education & Department Distribution : Mayoritas karyawan berlatar pendidikan Bachelor, dan departemen terbesar adalah R&D.

- Job Satisfaction : Sekitar 60% karyawan memiliki kepuasan kerja tinggi, namun attrition tetap terjadi di berbagai level.

- Environment Satisfaction : Tingkat kepuasan lingkungan kerja sangat memengaruhi keputusan keluar.

- Work Life Balance : Karyawan dengan WLB "Excellent" cenderung bertahan. Nilai "Bad" memiliki attrition lebih tinggi.

- Overall Attrition Distribution : 16.99% dari seluruh karyawan mengalami attrition (berdasarkan pie chart utama).

- Attrition vs Overtime Status : Karyawan yang bekerja lembur memiliki kecenderungan keluar lebih besar. Contoh: 81 dari 179 karyawan yang lembur mengalami attrition.

- Job Satisfaction by Role and Attrition : Menunjukkan distribusi attrition berdasarkan peran dan tingkat kepuasan kerja. Beberapa role seperti Sales Executive dan Laboratory Technician menunjukkan tingkat attrition tinggi.

- Environment Satisfaction by Role and Attrition : Role tertentu dengan kepuasan lingkungan kerja rendah menunjukkan peningkatan risiko attrition.

## Sistem Machine Learning

### Eksperimen Model

Proses pemodelan dilakukan menggunakan 4 algoritma yang berbeda untuk mengetahui model mana yang terbaik.

#### Langkah-langkah:
1. Preprocessing data: Meliputi penanganan fitur kategorikal, numerik, dan missing value. Selain itu, dilakukan feature selection menggunakan RFE (Recursive Feature Elimination) untuk memilih fitur terbaik, serta penanganan data tidak seimbang menggunakan SMOTE (Synthetic Minority Over-sampling Technique).

2. Pelatihan model menggunakan 4 algoritma yang berbeda yaitu Logistic Regression, Random Forest, XGBoost, SVM.

3. Evaluasi dan bandingkan berbagai model berdasarkan metrik seperti accuracy, Precision, recall, dan F1-score.

| Model            | Accuracy | Precision | Recall   | F1-Score |
|------------------|----------|-----------|----------|----------|
| Logistic Regression | 0.844340 | 0.714286  | 0.138889 | 0.232558 |
| Random Forest       | 0.839623 | 0.625000  | 0.138889 | 0.227273 |
| XGBoost            | 0.816038 | 0.421053  | 0.222222 | 0.290909 |
| SVM                | 0.830189 | 0.000000  | 0.000000 | 0.000000 |


Dari hasil eksperimen, model **XGBoost** dipilih sebagai model terbaik berdasarkan keseimbangan skor di seluruh metrik tersebut.

###  Model Terpilih:
- **XGBoost (Extreme Gradient Boosting)r**  
XGBoost adalah algoritma pembelajaran mesin berbasis teknik Gradient Boosting yang dirancang untuk meningkatkan performa model klasifikasi dan regresi. XGBoost merupakan implementasi yang sangat efisien dan terkenal karena kemampuannya untuk menangani data besar dan kompleks dengan sangat baik. Salah satu keunggulannya adalah kemampuannya untuk mengurangi overfitting dan meningkatkan akurasi melalui regularisasi yang efektif, seperti L1 (Lasso) dan L2 (Ridge).

## Deployment dengan streamlit
Langkah-langkah menggunakan sistem machine learning berbasis XGBoost adalah sebagai berikut.

1. Membuka link: https://m7e6p7ufh6ul4wt8sepkbe.streamlit.app/
2. Mengisi data yang dibutuhkan. Perlu diperhatikan bahwa pengguna harus menekan enter agar dapat menyimpan data numerik.
3. Hasil prediksi akan tampil di bagian bawah.
![image](https://github.com/user-attachments/assets/2eedf8f4-15f9-4ee9-821e-34a56da807b1)

---

## Kesimpulan
- Grafik "Attrition vs Overtime Status" menunjukkan bahwa karyawan yang bekerja lembur memiliki kemungkinan keluar yang jauh lebih tinggi. Dari 179 karyawan yang lembur, 98 orang mengalami attrition (sekitar 55%), jauh lebih tinggi dibandingkan mereka yang tidak lembur. Ini memperkuat bahwa overtime adalah salah satu faktor paling signifikan dalam keputusan karyawan untuk meninggalkan perusahaan.

- Dari grafik distribusi berdasarkan peran, terlihat bahwa posisi Sales Executive mendominasi jumlah attrition di hampir semua level kepuasan lingkungan dan pekerjaan. Meskipun bukan satu-satunya peran dengan tingkat keluar yang tinggi, jumlah karyawan keluar dari posisi ini secara absolut adalah yang tertinggi, menunjukkan bahwa divisi ini perlu perhatian lebih. Jadi, bukan seluruh departemen Sales, tapi spesifik pada Sales Executive.

- Karyawan dengan kepuasan rendah terhadap lingkungan kerja maupun pekerjaan lebih cenderung keluar, terlihat dari tingginya jumlah attrition (warna oranye) pada kategori "Low" di kedua grafik Job Satisfaction dan Environment Satisfaction. Hal ini menekankan pentingnya menciptakan lingkungan kerja yang positif dan memberikan pekerjaan yang memuaskan untuk menekan attrition.

- Dengan pola attrition yang cukup jelas (misalnya keterkaitan dengan overtime dan kepuasan), model seperti Extra Trees Classifier yang bekerja baik pada data tabular dan mampu menangani non-linearitas bisa sangat efektif untuk memprediksi attrition. Model ini cocok untuk digunakan sebagai dasar sistem peringatan dini bagi HR dalam mengantisipasi potensi kehilangan karyawan.

## Rekomendasi Action Items
- Karena lembur terbukti sebagai indikator kuat attrition, perusahaan perlu Meninjau ulang distribusi beban kerja dan Menerapkan pembatasan jam lembur. Memastikan lembur bersifat sukarela dan diberikan kompensasi yang adil. Melacak pola lembur sebagai indikator risiko resign secara proaktif.
- Karena Sales Executive merupakan peran dengan attrition tertinggi, disarankan: Melakukan audit mendalam terhadap job description, target penjualan, dan budaya kerja di posisi ini. Menilai apakah ekspektasi realistis dan mendukung kesejahteraan karyawan. Kembangkan Program Retensi, Pelatihan, dan Engagement
- Fokus pada peningkatan kepuasan kerja dan lingkungan melalui: Program pelatihan pengembangan karier. Coaching dan mentoring rutin. Forum komunikasi dua arah antara manajemen dan karyawan. Lakukan Exit Interview yang Terstruktur dan Analitis
- Gunakan hasil exit interview sebagai umpan balik sistematis untuk: Mengidentifikasi akar masalah berdasarkan role, departemen, dan kepuasan kerja. Mengintegrasikan temuan ini ke dalam strategi HR untuk mencegah attrition di masa depan.

## Referensi
1. fahadrehman07 - Kagle. Diakses pada 20 April 2025 dari (https://www.kaggle.com/code/fahadrehman07/salifort-motors-providing-data-driven-suggestions)
2. Google Colab. Diakses pada 20 April 2025 dari (https://colab.research.google.com/drive/1iVo19vQtD5hk-Kcjuqb2Vg33bMnA1vLu?usp=sharing)

