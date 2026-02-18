import streamlit as st

conn = st.connection("neon", type="sql")
try:
    df = conn.query("SELECT 1;")
    st.success("You are officially connected to the Cloud! 🚀")
    st.write(df)
except Exception as e:
    st.error(f"Connection failed: {e}")
