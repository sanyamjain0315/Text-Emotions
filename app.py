import streamlit as st 
import joblib

model=joblib.load('Emotion Detector')

st.title('Text Emotion Detector')
x=st.text_input('Enter text....')
y=model.predict([x])
if st.button('Predict'):
  st.success(op[0])

  
