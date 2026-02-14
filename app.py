import streamlit as st

st.set_page_config(page_title="Take It Smart Project")
st.title("🚀 Welcome to Take It Smart")
st.subheader("Internship Dashboard")
st.write("Streamlit is successfully configured in this directory.")

import streamlit as st
import pandas as pd

# Display Profile
st.title("My Streamlit Portfolio")
st.write("**Name:** Ranusingh S.")
st.write("**Role:** Final Year BE Student (AI & ML)")
st.write("**Skills:** Python, Data Science, Machine Learning, Power BI")

# User Input with Button
st.subheader("User Information")
user_name = st.text_input("Enter your name")
user_age = st.number_input("Enter your age", min_value=0, max_value=100)

if st.button("Submit Info"):
    st.write(f"Hello {user_name}, you are {user_age} years old!")
    st.success("Information submitted successfully!") # Success message

# --- TASK: SHOW/HIDE TEXT ---
st.divider() # Adds a horizontal line for neatness
if st.checkbox("Show/Hide My Career Goal"):
    st.info("My goal is to become a Data Scientist and excel in the GATE 2026 DA exam!")

# --- TASK: SELECTBOX ---
st.subheader("Language Preference")
language = st.selectbox(
    "Choose a programming language you are mastering:",
    ["Python", "SQL", "Java", "C++", "JavaScript"]
)
st.write(f"You are currently focusing on: **{language}**")

# --- TASK: DISPLAY DATAFRAME ---
st.subheader("Internship Task List")
tasks_df = pd.DataFrame({
    "Task Number": [1, 2, 3],
    "Task Name": ["Setup Streamlit", "Build UI Components", "Data Integration"],
    "Status": ["Completed", "In Progress", "Pending"]
})
st.table(tasks_df) # 'st.table' is static, 'st.dataframe' is interactive

# --- TASK: CSV FILE UPLOADER ---
st.subheader("Data Analysis Tool")
uploaded_file = st.file_uploader("Upload your internship CSV file here", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of Uploaded Data")
    st.dataframe(df.head()) # Shows the first 5 rows
    st.success("File uploaded successfully!")

    # --- TASK: SIMPLE COUNTER ---
st.subheader("Simple Click Counter")
count = 0
if st.button("Click to Increment"):
    count += 1

st.write(f"The current count is: {count}")
st.caption("Note: This resets every time you interact with other widgets because no session state is used.")

# --- TASK: SIDEBAR MENU ---
st.sidebar.title("Education Portal")
st.sidebar.header("Available Courses")

# Radio button inside the sidebar
selected_course = st.sidebar.radio(
    "Select a course to view details:",
    ["Data Science", "Full Stack Python", "Full Stack Java", "Oracle"]
)

# Display content based on sidebar selection
st.sidebar.write(f"You have selected the **{selected_course}** track.")

if selected_course == "Data Science":
    st.sidebar.info("Focus: Python, ML, and Data Analytics.")

    # --- TASK: DISPLAY AN IMAGE ---
st.subheader("Visual Assets")

try:
    # We use the exact name you provided: img.jpg
    st.image("img.jpg", caption="Internship Project Image", width=400)
    st.success("Image loaded successfully!")
except Exception as e:
    st.error("Image file not found. Make sure 'img.jpg' is in the 'take it smart' folder.")
    # This helps you see the actual error if it's not a file-not-found issue
    st.write(f"Error detail: {e}")