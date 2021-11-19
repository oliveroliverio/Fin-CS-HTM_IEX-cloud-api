import streamlit as st
import requests
import config

st.title("Fundamentals Dashboard")

symbol = st.sidebar.text_input("Symbol", value="AAPL")

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'News', 'Ownership', 'Technicals'))
st.write(symbol)
st.title(screen)

if screen == 'Overview':
    # get stock info via api key
    url = f"https://cloud.iexapis.com/stable/stock/aapl/quote?token={config.IEX_API_TOKEN}"
    r = requests.get(url)
    print(r.json())
    # response_json = r.json()
    # st.image(response_json['url'])

    # if screen == 'Fundamentals':
    #   pass

