import streamlit as st
import random as rd
import samplePyFile as file

st.title("Deneme")
"Deneme deneme böyle mi yazılıyor"
st.title("ikinci başlık ")

def multiply_numbers(num1, num2):
    return num1 * num2

st.title('Multiplication App')

num1 = st.number_input("Enter the first parameter",value = 0,format = "%d")
num2 = st.number_input("Enter the second parameter",value = 0,format = "%d")

result = rd.randint(0,100)

st.write("The result of ML model is : " + str(result))
st.write(file.multiply(num1,num2))
