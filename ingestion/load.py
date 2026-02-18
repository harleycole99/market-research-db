# import psycopg2
# import os

from dotenv import load_dotenv
import streamlit as st

### ---- ONLINE load ---- ###


def insert_respondent(first_name, last_name, age):
    conn = st.connection("neon", type="sql")

    with conn.session as session:
        session.execute(
            "INSERT INTO respondents (first_name, last_name, age) VALUES (:first, :last, :age);",
            {"first": first_name, "last": last_name, "age": age},
        )
        session.commit()


### ---- Local load ---- ###

# load_dotenv()

# db_password = os.getenv("DB_PASS")
# db_user = os.getenv("DB_USER")

# database_url = os.getenv(
#     "postgresql://neondb_owner:npg_iIuUr2PXO4vj@ep-dawn-surf-ajjl1b3a-pooler.c-3.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
# )


# # 1. Open the connection
# def load_db(name, surname, age):
#     try:
#         with psycopg2.connect(database_url) as conn:
#             with conn.cursor() as cur:
#                 cur.execute(
#                     """
#                     CREATE TABLE IF NOT EXISTS participant_data (
#                     id SERIAL PRIMARY KEY,
#                     name TEXT,
#                     surname TEXT,
#                     age INT
#                     );
#                     """
#                 )

#                 cur.execute(
#                     "INSERT INTO participant_data (name, surname, age) VALUES (%s, %s, %s)",
#                     (name, surname, age),
#                 )

#     except Exception as error:
#         print(f"Connection failed: {error}")
