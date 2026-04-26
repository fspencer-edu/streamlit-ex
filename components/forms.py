import streamlit as st

def render_forms():
    st.header("Form Example")

    with st.form("form"):
        name = st.text_input("Name")
        feedback = st.text_area("Feedback")
        rating = st.slider("Rating", 1, 5, 3)

        submitted = st.form_submit_button("Submit")

        if submitted:
            st.success("Submitted!")
            st.write({
                "name": name,
                "feedback": feedback,
                "rating": rating
            })