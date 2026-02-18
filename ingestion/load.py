import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

db_password = os.getenv("DB_PASS")
db_user = os.getenv("DB_USER")


# 1. Open the connection
def load_db(name, surname, age):
    try:
        with psycopg2.connect(
            host="localhost",
            database="marketresearch",
            user=db_user,
            password=db_password,
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS participant_data (
                    id SERIAL PRIMARY KEY,
                    name TEXT,
                    surname TEXT,
                    age INT
                    );
                    """
                )

                cur.execute(
                    "INSERT INTO participant_data (name, surname, age) VALUES (%s, %s, %s)",
                    (name, surname, age),
                )

    except Exception as error:
        print(f"Connection failed: {error}")
