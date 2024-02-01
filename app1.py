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
        pregnancies = st.number_input('Pregnancies', value=0)

    with col2:
        glucose = st.number_input('Glucose', value=0)

    with col3:
        blood_pressure = st.number_input('Blood Pressure', value=0)

    col4, col5, col6 = st.columns(3)

    with col4:
        skin_thickness = st.number_input('Skin Thickness', value=0)

    with col5:
        insulin = st.number_input('Insulin', value=0)

    with col6:
        bmi = st.number_input('BMI', value=0)

    col7, col8, col9 = st.columns(3)

    with col7:
        diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', value=0)

    with col8:
        age = st.number_input('Age', value=0)

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