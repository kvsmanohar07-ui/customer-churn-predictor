import streamlit as st

st.title("Customer Churn Predictor")
st.write("Made by K.V.S. Manohar Reddy - Will this customer leave?")

months = st.number_input("How many months customer is with us?", min_value=0)
buys = st.number_input("How many times did he buy last month?", min_value=0)

if st.button("Predict"):
    if buys <= 1 and months > 3:
        st.error("This customer will LEAVE - Call him and save him!")
    else:
        st.success("This customer will STAY - He is happy!")
