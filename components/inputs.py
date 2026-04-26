import streamlit as st

def render_inputs():
    st.header("Inputs")
    
    name = st.text_input("Your name")
    
    st.text_area("Text area")
    st.number_input("Number input", 0, 100, 10)
    st.slider("Slider", 0, 100, 25)
    st.selectbox("Selectbox", ["Python", "JS", "SQL"])
    st.multiselect("Multiselect", ["Streamlit", "Pandas", "ChromaDB"])
    st.radio("Radio", ["Beginner", "Intermediate", "Advanced"])
    st.checkbox("Check me")
    
    if st.button("Submit"):
        st.success(f"Hello {name}!")