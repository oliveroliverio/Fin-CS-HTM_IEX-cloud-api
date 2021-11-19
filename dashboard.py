import streamlit as st
import requests

st.title("Fundamentals Dashboard")

symbol = st.sidebar.text_input("Symbol", value="AAPL")

st.write(symbol)

