import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_page.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
dashborad_page = st.Page(
    "views/dashborad_page.py",
    title="Skills Dashboard",
    icon=":material/bar_chart:",
)
project_page = st.Page(
    "views/project_page.py",
    title="My Chatbot ",
    icon=":material/smart_toy:",
)


pg = st.navigation({
    "info": [about_page],
    "Projects": [project_page, dashborad_page],
})

#st.title("Welcome")
st.sidebar.text("Made with ❤️ by Gazali")
st.logo("assets/logo.jpg")
st.write()


# --- RUN NAVIGATION ---
pg.run()