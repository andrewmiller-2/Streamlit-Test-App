import streamlit as st

st.title("Test App")
st.write("Welcome to your first Streamlit app.")

name = st.text_input("Hey what's your name?")

if name:
    st.success(f"Hello, {name}, welcome to the app.")