import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def render_charts():
    st.header("Charts")

    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["A", "B", "C"]
    )

    st.line_chart(df)
    st.bar_chart(df)
    st.area_chart(df)

    fig, ax = plt.subplots()
    ax.scatter(df["A"], df["B"])
    ax.set_title("Scatter Plot")

    st.pyplot(fig)