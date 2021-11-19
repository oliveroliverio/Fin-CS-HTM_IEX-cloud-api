import streamlit as st
import requests

st.title("Fundamentals Dashboard")

symbol = st.sidebar.text_input("Symbol", value="AAPL")

screen = st.sidebar.selectbox("View", ('Overiew', 'Fundamentals', 'News', 'Ownership', 'Technicals'))
# st.write(symbol)
st.title(screen)

if screen == 'Overview':
  # get stock info via api key
  url = "https://cloud.iexapis.com/stable/stock/aapl/quote?token={config.IEX_API_TOKEN}"

if screen == 'Fundamentals':
  pass