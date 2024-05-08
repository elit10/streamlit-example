import streamlit as st
import random as rd

st.title("Deneme")
"Deneme deneme böyle mi yazılıyor"
st.title("ikinci başlık ")

def multiply_numbers(num1, num2):
    return num1 * num2

st.title('Multiplication App')

num1 = st.number_input("Enter the first parameter")
num2 = st.number_input("Enter the second parameter")

result = rd.randInt(10)

st.write("The result: " + result)
