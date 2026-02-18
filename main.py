import streamlit as st
from sqlalchemy import text


def clean_name(name_string):
    cleaned = name_string.strip().capitalize()
    if cleaned.isalpha():
        return cleaned
    else:
        return None


conn = st.connection("neon", type="sql")


def insert_respondent(first_name, last_name, age):
    with conn.session as session:
        session.execute(
            text(
                """
            CREATE TABLE IF NOT EXISTS respondents (
                id SERIAL PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                age INT
            );
        """
            )
        )
        session.execute(
            text(
                "INSERT INTO respondents (first_name, last_name, age) VALUES (:first, :last, :age);"
            ),
            {"first": first_name, "last": last_name, "age": age},
        )
        session.commit()


with st.form("details"):
    name = st.text_input("Name")
    surname = st.text_input("Surname")
    age = st.number_input("Age")
    submitted = st.form_submit_button("submit")

if submitted:
    cleanname = clean_name(name)
    cleansurname = clean_name(surname)
    # load_db(cleanname, cleansurname, age)
    insert_respondent(cleanname, cleansurname, age)

    st.write(f"Hello {name}, Your details have been saved")
