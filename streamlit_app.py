import streamlit as st

st.title("Deneme")
"Deneme deneme böyle mi yazılıyor"
st.title("ikinci başlık ")

def multiply_numbers(num1, num2):
    return num1 * num2

st.title('Multiplication App')

num1 = st.number_input('Enter the first number', value=1, format='%d')
num2 = st.number_input('Enter the second number', value=1, format='%d')

result = multiply_numbers(num1, num2)

st.write(f'The result of {num1} * {num2} is **{result}**')
