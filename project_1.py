import streamlit as st
import requests
import joblib
import os
import streamlit as st
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from numerize import numerize

def projectsatu():
    st.title("Maternal Risk Level Prediction")
    
    st.write('Maternal Risk Level adalah tingkat resiko kehamilan (low, medium, high) yang dapat diperkirakan berdasarkan beberapa variabel.'\
         ' Atas hal tersebut, silakan masukan data kesehatan yang dibutuhkan dibawah ini untuk mengetahui tingkat resiko kehamilan anda.')
    
    data = pd.read_csv('Maternal Health Risk Data Set.csv', sep=',')
    data['RiskLevel'] = data['RiskLevel'].str.lower()
    dt_joblib = joblib.load('dt_joblib')

    with st.form("Prediction Form"): 

        age, sis, dias, bs, hr, bt = st.columns(6,vertical_alignment="bottom")

        with age:
            usia = st.number_input('Usia (tahun):', value=0)

        with sis:
            sistolyc = st.number_input('Tekanan Darah-Sistolik (mmHg):', value=0)
    
        with dias:
            diastolyc = st.number_input('Tekanan Darah-Diastolik (mmHg):', value=0)

        with bs:
            glucose = st.number_input('Kadar Gula (mmol/L):', value=0)
    
        with hr:
            heartrate = st.number_input('Detak Jantung (per menit):', value=0)
    
        with bt:
            bodytemp = st.number_input('Suhu Badan (Celcius):', value=0)

        data_predict = {'usia':usia,'sistolyc':sistolyc,'diastolyc':diastolyc,
                    'glucose':glucose,'heartrate':heartrate,'bodytemp':bodytemp
                    }
        data_predict= pd.DataFrame(data_predict, index=[0])

        data_predict.rename(columns={
            'usia':'Age',
            'bodytemp': 'BodyTemp_C',
            'diastolyc': 'DiastolicBP',
            'glucose': 'BS',
            'heartrate': 'HeartRate',
            'sistolyc': 'SystolicBP',
        }, inplace=True)

        data_predict = data_predict[['Age', 'SystolicBP', 'DiastolicBP', 'BS','HeartRate', 'BodyTemp_C']]
        
        submitted = st.form_submit_button("Predict")
        if submitted:
            res1= st.columns(1)
            for item in res1:
                predict = dt_joblib.predict(data_predict)
                predict = int(predict[0])
                st.write('**Risk Level of Maternity :**')

                if predict ==1:
                    st.info('Low Risk')
                    st.write('I am very happy knowing that you are in a very good condition. Jaga pola makan,berolahraga dan rutinlah cek kesehatan ke dokter')
                elif predict ==2:
                    st.info('Medium Risk')
                    st.write('Jaga pola makan,berolahraga dan rutinlah cek kesehatan ke dokter')
                elif predict ==3:
                    st.info('High Risk')
                    st.write('Kamu harus berhati-hati. Jaga pola makan,berolahraga dan rutinlah cek kesehatan ke dokter')