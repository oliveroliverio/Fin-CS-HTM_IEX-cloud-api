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

