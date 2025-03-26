# project 9: BMI Calculator
import streamlit as st
import pandas as pd

st.title('BMI Calculator')

height =st.slider("Enter your height(in cm):",100,250,150)
weight = st.slider("Enter your weight(in kg):",30,200,60, 5)

bmi = weight / ((height/100)**2)
st.title(f"Your BMI is {bmi:.2f}")
st.write(" BMI Categories")
st.write("- Underweight: BMI is less than 18.5")

st.write("- Normal weight: BMI is 18.5 to 24.9")
st.write("- Overweight: BMI is 25 to 29.9")
st.write("- Obesity: BMI is 30 or more")


# token = st.secrets["token"]ngrok config add-authtoken 2tj0nRD6lxqL6o0rXmh7Q18JOS6_6t3BhUAFNVRmpMvj3EL4A
# https://colab.research.google.com/drive/10_fDwOkVN0MRWapVEiSgDP2W10_56wS1#scrollTo=eEBW9V8wmTym&line=25&uniqifier=1