import re
import streamlit as st
import requests

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        message = st.text_input("Your Message")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        if not WEBHOOK_URL:
            st.error("Email service isnt set up.. Please try again later", icon="✉️")
            st.stop()
        if not name:
            st.error("Please provide your name",icon="👤")
            st.stop()
        if not is_valid_email(email):
            st.error("Please Provide a vaild email",icon="📩")
        if not message:
            st.error("Please provide message", icon="💬")
            st.stop()

        # Prepare data for Slack
        slack_data = {
            "text": f"New Contact Form Submission:\n*Name:* {name}\n*Email:* {email}\n*Message:* {message}"
        }

        # Send data to Slack
        response = requests.post(WEBHOOK_URL, json=slack_data)

        if response.status_code == 200:
            st.success("Your message has been sent successfully")
        else:
            st.error("There was an error sending your message", icon="🚫")

        # data = {"email": email, "name": name,"message": message}
        # response = requests.post(WEBHOOK_URL, json=data)
        #
        # if response.status_code == 200:
        #     st.success("Your message has been send successfully")
        # else:
        #     st.error("There was an error in sending your message", icon="🚫")