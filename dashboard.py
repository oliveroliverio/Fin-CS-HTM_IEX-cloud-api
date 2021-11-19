import streamlit as st
import requests

st.title("Fundamentals Dashboard")

symbol = st.sidebar.text_input("Symbol", value="AAPL")

screen = st.sidebar.selectbox("View", ('Overiew', 'Fundamentals', 'News', 'Ownership', 'Technicals'))
# st.write(symbol)
st.title(screen)

if screen == 'Overview':
  # just testing for now
  pass

if screen == 'Fundamentals':
  pass