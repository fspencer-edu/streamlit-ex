import streamlit as st
import pandas as pd

def render_upload():
    st.header("File Upload")

    file = st.file_uploader("Upload CSV", type=["csv"])

    if file:
        df = pd.read_csv(file)
        st.dataframe(df)
        st.write("Shape:", df.shape)