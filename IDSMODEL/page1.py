import pickle
import streamlit as st
import tensorflow as tf


def load(weights="model/model.h5"):
    model = tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(4,)),  # (81, 4)
            tf.keras.layers.Dense(128, activation="relu"),  # W . x + b
            tf.keras.layers.Dense(512, activation="relu"),
            tf.keras.layers.Dense(1, activation="sigmoid"),
        ]
    )
    model.load_weights(weights)
    return model


model = load()
predict = lambda x: int(model.predict([x]).squeeze().item())

# pickle_in = open("model.pkl","rb")
# rf=pickle.load(pickle_in)


def predict_note_authentication(Age, BMI, Glucose, Resistin):
    prediction = predict([Age, BMI, Glucose, Resistin])
    print(prediction)
    return prediction


def show_page1():
    st.title("🩺Cancer Breast Prediction For Normal Help")
    st.write(
        "This Model is Simple way to detect the model for more information please have a Professional Examination at hospital, hopeful you help you as much as possible"
    )

    Age = st.slider("**How old are you?**", 0, 100, 5, key="age_input")
    st.write("I'm ", Age, "years old")

    BMI = st.number_input("**BMI**", key="bmi_input")
    st.write("The BMI is ", BMI)

    Glucose = st.number_input("**Glucose**", key="glucose_input")
    st.write("The current Glucose is ", Glucose)

    Resistin = st.number_input("**Resistin**", key="resistin_input")
    st.write("The current Resistin is ", Resistin)

    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(Age, BMI, Glucose, Resistin)
        if result == 0:
            result_text = "Healthy"
        elif result == 1:
            result_text = "High probability of having breast cancer"
        else:
            result_text = "Unknown"

        st.success(f"The output is {result_text}")


def main():
    show_page1()


if __name__ == "__main__":
    main()
