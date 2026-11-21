import numpy as np
import joblib
import streamlit as st 


model = joblib.load('wine_model.joblib')

cols = [
    'fixed acidity',
    'volatile acidity',
    'citric acid',
    'residual sugar',
    'chlorides',
    'free sulfur dioxide',
    'total sulfur dioxide',
    'density',
    'pH',
    'sulphates',
    'alcohol'
]

st.title('Wine Quality App')
In=[]

for i in cols:
    v=st.number_input(f'enter {i} value:')
    In.append(v)
if st.button('predict quality'):
    out=model.predict([In])
    st.success(f"Predecited quality of wine is:{out}")