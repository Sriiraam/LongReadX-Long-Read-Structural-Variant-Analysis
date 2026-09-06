import pandas as pd
import streamlit as st


@st.cache_data
def load_csv(path):
    return pd.read_csv(path)


@st.cache_data
def load_text(path):
    with open(path) as f:
        return f.read()
