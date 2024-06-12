import streamlit as st

st.title('Job Tracker')

st.write("This is a simple job application tracker")

# Initialize connection
conn = st.connection("postgresql", type = "sql")

df = conn.query("SELECT * FROM position ORDER BY ID ASC;")
df.columns = ['ID', 'Title', 'Company', 'Salary', 'City', 'State', 'Job Type', 'Applied On', 'Application Status']
st.table(df.style.hide_index())