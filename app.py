import streamlit as st
import pandas as pd
from datetime import date

st.title("🚀 Team Daily Status")

# Form for colleagues
with st.form("report_form"):
    name = st.text_input("Full Name")
    task = st.text_area("What did you work on today?")
    status = st.selectbox("Status", ["Completed", "In Progress", "Blocked"])
    submit = st.form_submit_button("Submit to WhatsApp Group")

if submit:
    if name and task:
        # Create the message for WhatsApp
        report_msg = f"*Daily Report - {date.today()}*%0A*Name:* {name}%0A*Task:* {task}%0A*Status:* {status}"
        
        # This creates a link that opens WhatsApp with the message ready
        wa_url = f"https://wa.me/?text={report_msg}"
        
        st.success("Report Generated!")
        st.markdown(f'[👉 Click here to send to WhatsApp Group]({wa_url})')
    else:
        st.warning("Please fill in your name and tasks.")
