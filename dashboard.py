import streamlit as st
import requests
import config

st.title("Fundamentals Dashboard")

symbol = st.sidebar.text_input("Symbol", value="AAPL")

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'News', 'Ownership', 'Technicals'))
st.write(symbol)
st.title(screen)

if screen == 'Overview':
    # get stock logo via api token
    url = f"https://cloud.iexapis.com/stable/stock/{symbol}/logo?token={config.IEX_API_TOKEN}"
    r = requests.get(url)
    print(r.json())
    response_json = r.json()
    st.image(response_json['url'])

    # get company data via api token
    # display json info below icon
    url = f"https://cloud.iexapis.com/stable/stock/{symbol}/company?token={config.IEX_API_TOKEN}"
    r = requests.get(url)
    response_json = r.json()
    st.write(response_json)

if screen == 'Fundamentals':
    pass
