import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

"Deneme deneme böyle mi yazılıyor"

def multiply_numbers(num1, num2):
    return num1 * num2

st.title('Multiplication App')

num1 = st.number_input('Enter the first number', value=1, format='%d')
num2 = st.number_input('Enter the second number', value=1, format='%d')

result = multiply_numbers(num1, num2)

st.write(f'The result of {num1} * {num2} is **{result}**')
