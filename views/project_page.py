import random
import time
import streamlit as st

# Streamed response emulator
def response_generator():
    devops_responses = [
        "Hey there! I have experience with Docker and Kubernetes for containerization and orchestration.",
        "Hi! I've worked extensively with CI/CD pipelines using Jenkins and GitLab CI.",
        "Hello! My experience includes setting up monitoring with Prometheus and Grafana.",
        "Hey! I have strong skills in infrastructure as code using Terraform and Ansible.",
        "Hi there! I'm proficient in automating tasks with scripting languages like Python and Bash.",
        "Hello! I've implemented security best practices using tools like Vault and AWS IAM.",
        "Hey! I have a deep understanding of cloud platforms, especially AWS and Azure.",
        "Hi! I've been involved in performance tuning and optimization of server configurations.",
        "Hello! I've worked with various logging and alerting tools like ELK Stack and Splunk.",
        "Hey there! I have experience in setting up and managing CI/CD for microservices architectures."
    ]
    response = random.choice(devops_responses)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title("DevOps Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask me anything about DevOps!"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
