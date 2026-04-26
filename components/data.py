import streamlit as st
import pandas as pd

def render_data():
    st.header("Data + Metrics")
    
    df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr"],
        "Revenue": [1200, 1800, 1500, 2200],
        "Users": [100, 150, 130, 190]
    })
    
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Revenue", "$2200", "+12%")
    col2.metric("Users", "190", "+20")
    col3.metric("Conversion", "4.8%", "-0.3%")

    st.dataframe(df)

    edited = st.data_editor(df)
    st.write("Edited:", edited)