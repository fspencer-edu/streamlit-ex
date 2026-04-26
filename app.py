import streamlit as st

from components.inputs import render_inputs
from components.data import render_data
from components.charts import render_charts
from components.forms import render_forms
from components.upload import render_upload
from utils.state import render_state

st.set_page_config(page_title="Streamlet Playground", layout="wide")

st.title("Streamlit Playground")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.selectbox(
    "Choose Section",
    ["Inputs", "Data", "Charts", "Forms", "Upload", "State"]
)

# Routing
if page == "Inputs":
    render_inputs()
    
elif page == "Data":
    render_data()
    
elif page == "Charts":
    render_charts()
    
elif page == "Forms":
    render_forms()
    
elif page == "Upload":
    render_upload()
    
elif page == "State":
    render_state()
    
