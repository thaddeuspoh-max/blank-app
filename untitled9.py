import streamlit as st

st.title("🎓 GPA Calculator")

grades = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "F": 0.0
}

num_courses = st.number_input("How many courses?", min_value=1, max_value=10, step=1)

total_points = 0
total_credits = 0

for i in range(num_courses):
    st.subheader(f"Course {i+1}")
    credit = st.number_input(f"Credit Hours for Course {i+1}", min_value=0.5, step=0.5, key=f"credit_{i}")
    grade = st.selectbox(f"Grade for Course {i+1}", options=grades.keys(), key=f"grade_{i}")
    total_points += credit * grades[grade]
    total_credits += credit

if total_credits > 0:
    gpa = round(total_points / total_credits, 2)
    st.success(f"Your GPA is: {gpa}")
else:
    st.warning("Please input valid credit hours.")
