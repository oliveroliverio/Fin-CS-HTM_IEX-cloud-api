# [IEX Cloud API - Stock Fundamentals Dashboard](https://www.youtube.com/watch?v=bPPJTc3JoMI)

## create base dashboard app

```python
import streamlit as st
import requests

st.title("Fundamentals Dashboard")
symbol = st.sidebar.text_input("Symbol", value="AAPL")
st.write(symbol)
```
Run with this command
```python
streamlit run dashboard.py
```

Try playing around with adding symbols and observing the reaction

Add a sidebar
```python
screen = st.sidebar.selectbox("View", ('Overiew', 'Fundamentals', 'News', 'Ownership', 'Technicals'))
```

Refer to [Rest docs](https://iexcloud.io/docs/api/#rest-how-to)