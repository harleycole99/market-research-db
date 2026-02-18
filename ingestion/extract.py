import streamlit as st

with st.form("details"):
    name = st.text_input("Name")
    surname = st.text_input("Surname")
    submitted = st.form_submit_button("submit")

if submitted:
    st.write("Hello {name} {surname}")
