# -*- coding: utf-8 -*-
"""testing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vRn23jPfnW9aBX35AsP3yixNTJ2rxkQ8
"""

import pandas as pd
import streamlit as st

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df= pd.DataFrame(data)

st.dataframe(df)
st.button("click the df")
st.button("Click me")
