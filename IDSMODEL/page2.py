import streamlit


import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

pickle_in = open("model/svm_model.sav", "rb")
VSM = pickle.load(pickle_in)


def predict_note_authentication(
    radius_mean,
    texture_mean,
    smoothness_mean,
    compactness_mean,
    symmetry_mean,
    fractal_dimension_mean,
    radius_se,
    texture_se,
    smoothness_se,
    compactness_se,
    symmetry_se,
    fractal_dimension_se,
):
    prediction = VSM.predict(
        [
            [
                radius_mean,
                texture_mean,
                smoothness_mean,
                compactness_mean,
                symmetry_mean,
                fractal_dimension_mean,
                radius_se,
                texture_se,
                smoothness_se,
                compactness_se,
                symmetry_se,
                fractal_dimension_se,
            ]
        ]
    )
    print(prediction)
    return prediction


def show_page2():
    st.title("👨‍⚕️Professional Assistant")
    st.write(
        "Special Classification this a assitant to help Dr to get the breast Cancer which is M or B"
    )

    radius_mean = st.number_input("radius_mean", key="radius_mean_input")
    st.write("The BMI is ", radius_mean)

    st.write("<hr>", unsafe_allow_html=True)

    texture_mean = st.number_input("texture_mean", key="texture_mean_input")
    st.write("The current texture_mean is ", texture_mean)

    st.write("<hr>", unsafe_allow_html=True)

    smoothness_mean = st.number_input("smoothness_mean", key="smoothness_mean_input")
    st.write("The current smoothness_mean is ", smoothness_mean)

    st.write("<hr>", unsafe_allow_html=True)

    compactness_mean = st.number_input("compactness_mean", key="compactness_mean")
    st.write("The current compactness_mean is ", compactness_mean)

    st.write("<hr>", unsafe_allow_html=True)

    symmetry_mean = st.number_input("symmetry_mean", key="symmetry_mean_input")
    st.write("The current symmetry_mean is ", symmetry_mean)

    st.write("<hr>", unsafe_allow_html=True)

    fractal_dimension_mean = st.number_input(
        "fractal_dimension_mean", key="fractal_dimension_mean_input"
    )
    st.write("The current fractal_dimension_mean is ", fractal_dimension_mean)

    st.write("<hr>", unsafe_allow_html=True)

    radius_se = st.number_input("radius_se", key="radius_se_input")
    st.write("The current radius_se is ", radius_se)

    st.write("<hr>", unsafe_allow_html=True)

    texture_se = st.number_input("texture_se", key="texture_se_input")
    st.write("The current texture_se is ", texture_se)

    st.write("<hr>", unsafe_allow_html=True)

    smoothness_se = st.number_input("smoothness_se", key="smoothness_se_input")
    st.write("The current smoothness_se is ", smoothness_se)

    st.write("<hr>", unsafe_allow_html=True)

    compactness_se = st.number_input("compactness_se", key="compactness_se_input")
    st.write("The current compactness_se is ", compactness_se)

    st.write("<hr>", unsafe_allow_html=True)

    symmetry_se = st.number_input("symmetry_se", key="symmetry_se_input")
    st.write("The current symmetry_se is ", symmetry_se)

    st.write("<hr>", unsafe_allow_html=True)

    fractal_dimension_se = st.number_input(
        "fractal_dimension_se", key="fractal_dimension_se_input"
    )
    st.write("The current fractal_dimension_se is ", fractal_dimension_se)

    # radius_mean', 'texture_mean', 'smoothness_mean',
    #        '', 'symmetry_mean', 'fractal_dimension_mean',
    #        'radius_se', 'texture_se', 'smoothness_se', 'compactness_se',
    #        'symmetry_se', 'fractal_dimension_se'

    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(
            radius_mean,
            texture_mean,
            smoothness_mean,
            compactness_mean,
            symmetry_mean,
            fractal_dimension_mean,
            radius_se,
            texture_se,
            smoothness_se,
            compactness_se,
            symmetry_se,
            fractal_dimension_se,
        )
        if result == 0:
            result_text = "Benign"
        elif result == 1:
            result_text = "Malignant"
        else:
            result_text = "Unknown"

        st.success(f"The Breast Cancer has the high probability is {result_text}")
