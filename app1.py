import streamlit as st
import pickle
import bz2
import numpy as np

# Load the model and scaler
scalar_object = bz2.BZ2File("Model/standardScalar.pkl", "rb")
scaler = pickle.load(scalar_object)

model_for_pred = bz2.BZ2File("Model/modelForPrediction.pkl", "rb")
model = pickle.load(model_for_pred)

# Streamlit app
def main():
    st.title('Diabetes Prediction 🩺')

    # Input form
    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = float(st.text_input('Pregnancies', value='0', help='Number of times pregnant'))

    with col2:
        glucose = float(st.text_input('Glucose', value='0', help='Plasma glucose concentration'))

    with col3:
        blood_pressure = float(st.text_input('Blood Pressure', value='0', help='Diastolic blood pressure'))

    col4, col5, col6 = st.columns(3)

    with col4:
        skin_thickness = float(st.text_input('Skin Thickness', value='0', help='Triceps skin fold thickness'))

    with col5:
        insulin = float(st.text_input('Insulin', value='0', help='Insulin levels'))

    with col6:
        bmi = float(st.text_input('BMI', value='0', help='Body Mass Index (BMI)'))

    col7, col8, col9 = st.columns(3)

    with col7:
        diabetes_pedigree_function = float(st.text_input('Diabetes Pedigree Function', value='0', help='Assign a value of 0 if it is not available.'))

    with col8:
        age = float(st.text_input('Age', value='0', help='Age of the patient'))

    # Predict button
    if st.button('Predict'):
        new_data = scaler.transform([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
        prediction = model.predict(new_data)

        if prediction[0] == 1:
            result = 'Diabetic'
            result_color = 'red'
        else:
            result = 'Non-Diabetic'
            result_color = 'green'

        # Styling the output text with larger font size and color using HTML/CSS
        st.markdown(f'<p style="color:{result_color}; font-size:50px;">The Person is {result}</p>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
