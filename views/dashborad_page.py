import streamlit as st
import pandas as pd

# CONFIGS
DATA_URL = "assets/devops_tools.csv"
START_YEAR = 2014
END_YEAR = 2024

st.title("DevOps Skills Dashboard")

@st.cache_data
def get_and_prepare_data(data):
    df = pd.read_csv(data).assign(
        date_of_use=lambda df: pd.to_datetime(df["date_of_use"]),
        year=lambda df: df["date_of_use"].dt.year,
    )
    return df

df = get_and_prepare_data(DATA_URL)

# Filter data for the years of interest
df = df[(df["year"] >= START_YEAR) & (df["year"] <= END_YEAR)]

# Group by year and calculate total skills and experience growth
yearly_skills_data = (
    df.groupby("year")["skills"]
    .count()
    .reset_index(name="Number of Skills")
)

# Display the skills count over years
st.header("Skills Growth Over Years")
st.line_chart(yearly_skills_data.set_index("year")["Number of Skills"], height=400)

# Display additional insights
st.header("Additional Insights")

# Show top tools by skills count over the years
top_tools = (
    df.groupby("tool_name")["skills"]
    .count()
    .sort_values(ascending=False)
    .head(10)
)

st.subheader("Top Tools by Skills Count")
st.bar_chart(top_tools, height=400)

# Show experience growth over the years
experience_growth = (
    df.groupby("year")["projects_count"]
    .sum()
    .reset_index(name="Total Projects")
)

st.subheader("Experience Growth Over Years")
st.line_chart(experience_growth.set_index("year")["Total Projects"], height=400)

# Detailed Data Table
st.header("Detailed Data")
st.dataframe(df)
