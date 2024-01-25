import streamlit as st
import pickle
import bz2
import numpy as np

# Load the model and scaler
scalarobject = bz2.BZ2File("Model/standardScalar.pkl", "rb")
scaler = pickle.load(scalarobject)

modelforpred = bz2.BZ2File("Model/modelForPrediction.pkl", "rb")
model = pickle.load(modelforpred)

# Streamlit app
def main():
    st.title('Diabetes Prediction')

    # Input form
    pregnancies = st.number_input('Pregnancies', value=0)
    glucose = st.number_input('Glucose', value=0)
    blood_pressure = st.number_input('Blood Pressure', value=0)
    skin_thickness = st.number_input('Skin Thickness', value=0)
    insulin = st.number_input('Insulin', value=0)
    bmi = st.number_input('BMI', value=0)
    diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', value=0)
    age = st.number_input('Age', value=0)

    # Predict button
    if st.button('Predict'):
        new_data = scaler.transform([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
        prediction = model.predict(new_data)

        if prediction[0] == 1:
            result = 'Diabetic'
        else:
            result = 'Non-Diabetic'

        st.success(f'The Person is {result}')

if __name__ == '__main__':
    main()
