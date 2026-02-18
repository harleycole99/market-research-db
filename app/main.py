import streamlit as st
from ingestion.load import load_db
from ingestion.extract import clean_name

with st.form("details"):
    name = st.text_input("Name")
    surname = st.text_input("Surname")
    age = st.number_input("Age")
    submitted = st.form_submit_button("submit")

if submitted:
    st.write(f"Hello {name}, Your details have been saved")

cleanname = clean_name(name)
cleansurname = clean_name(surname)
load_db(cleanname, cleansurname, age)
