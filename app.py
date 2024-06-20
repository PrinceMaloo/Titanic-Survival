import streamlit as st
import pickle
import pandas as pd


model = pickle.load(open("Model.pkl","rb"))



st.title("Titanic Survival Prediction")

col1, col2  = st.columns(2)

Pclass = col1.number_input(label = "Enter Passenger's class", min_value = 1, max_value = 3)
Age = col2.number_input("Enter Passenger's Age",min_value = 0)
Sibsp = col2.number_input("Enter the Sibing on onboard",min_value = 0)
Parch = col2.number_input("Enter the Parent or Child Onboard Value",min_value = 0)
Fare = col1.number_input(label = "Enter Fare", min_value = 0)

# button = st.button("Predict, on_click = model.predict([]))

Sex = col1.selectbox(
    "SEX",
    ("male", "female"))

Embarked = col1.selectbox(
    "Embarked",
    ("S", "C", "Q"))

family_member = Sibsp + Parch

data = {"Pclass": [Pclass],"Sex" : [Sex], "Age" : [Age], "Fare" : [Fare], "Embarked" : [Embarked], "family_member" : [family_member]}
df = pd.DataFrame(data)


if st.button('Predict'):


    result = model.predict(df)[0]
    if result == 1:
        st.header("Survived")
    else:
        st.header("Not Survived")