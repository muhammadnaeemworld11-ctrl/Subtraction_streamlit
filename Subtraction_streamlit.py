import streamlit as st 
st.title("SIMPLE SUBTRACTION CALCULATOR ")

num1 = st.number_input("Enter first number to subtrac: ")
num2 = st.number_input("Enter second number to subtrac: ")
st.success(num1 - num2)