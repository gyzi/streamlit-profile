import streamlit as st

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

#---- Profile Section -----
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile.jpg",width=230)

with col2:
    st.title("Algazali Hamid", anchor=False)
    st.write("Sr. Cloud and DevOps Engineer")
    if st.button("️✉️ Contact Me"):
        show_contact_form()

import streamlit as st

# --- Experience and Qualifications -----
st.write("\n")
st.subheader("Experience and Qualifications", anchor=False)
st.write(
    """
    - 10+ Years of experience in DevOps and Infrastructure Management
    - Extensive hands-on experience with CI/CD pipelines, containerization, and cloud platforms
    - Deep understanding of automation, orchestration, and security best practices
    - Proven track record in optimizing performance, managing infrastructure as code, and implementing monitoring solutions
    """
)
st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
    - Programming & Scripting: Python, Bash, PowerShell
    - CI/CD Tools: Jenkins, GitLab CI, CircleCI
    - Containerization & Orchestration: Docker, Kubernetes, OpenShift
    - Cloud Platforms: AWS, Azure, Google Cloud
    - Infrastructure as Code: Terraform, Ansible, CloudFormation
    - Monitoring & Logging: Prometheus, Grafana, ELK Stack, Splunk
    - Security: Vault, AWS IAM, Azure Security Center
    """
)
