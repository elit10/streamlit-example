import streamlit as st
import samplePyFile as file
import random as rd

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

if st.button('HESAPLA'):
    st.write(file.multiply(num1,num2))


def page1():
    st.title("Page 1")
    st.write("Welcome to page 1!")

def page2():
    st.title("Page 2")
    st.write("Welcome to page 2!")

pages = {
    "Page 1": page1,
    "Page 2": page2
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))
pages(selection)
