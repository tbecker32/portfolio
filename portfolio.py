import streamlit as st
import info
import pandas as pd

#about me
def about_me_section():
    st.header("About Me")
    st.image(info.profile_picture, width = 200)
    st.write(info.about_me)
    st.write("---")
about_me_section()

#sidebar

def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn!")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width="75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True) # function to use html code
    st.sidebar.text("Check out my work!")
    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="Github" width="65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Email me!")
    email_html = f'<a href="{info.my_email_address}"><img src="{info.email_image_url}" alt="Email" width="75" height="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)
links_section()

#education
def education_section(education_data, course_data):
    st.header("Education")
    st.subheader(f'**{education_data["Institution"]}**')
    st.write(f'**Degree:** {education_data["Degree"]}')
    st.write(f'**Graduation Date:** {education_data["Graduation Date"]}')
    st.write(f'**GPA:** {education_data["GPA"]}')
    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Number",
        "names": "Course Name",
        "semester_taken": "Semester Taken",
        "skills": st.column_config.TextColumn("Skills Learned", width="large")},
        hide_index=True,
        )
    st.write("---")
education_section(info.education_data, info.course_data)

#experience
def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title, (dates, job_desc, img) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(img, width=100)
        expander.subheader(dates)
        for bullet in job_desc:
            expander.write(bullet)
    st.write("---")
experience_section(info.experience_data)

#projects
def projects_section(projects_data):
    st.header("Projects")
    for project_name, project_desc in projects_data.items():
        expander = st.expander(f"{project_name}")
        for bullet in project_desc:
            expander.write(bullet)
    st.write("---")
projects_section(info.projects_data)

#skills
def skills_section(programming_data, communication_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, level in programming_data.items():
        st.write(f"{skill}{info.programming_icons.get(skill,'')}")
        st.progress(level)

    st.subheader("Communication")
    expander = st.expander("Communication Skills:")
    for skill in communication_data:
        expander.write(skill)
    st.write("---")
skills_section(info.programming_data, info.communication_data)

#activities
def activities_section(leadership_data, activity_data, interests_data):
    st.header("Activities")
    tab1, tab2, tab3 = st.tabs(["Leadership", "Community Service", "Interests"])
    with tab1:
        st.subheader("Leadership")
        for title, (dates, details, image) in leadership_data.items():
            expander = st.expander(f"{title}: {dates}")
            expander.image(image, width=100)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Service")
        for title, dates in activity_data.items():
            st.write(f"{title}: {dates}")
    with tab3:
        st.subheader("Interests")
        for activity in interests_data:
            st.write(activity)
activities_section(info.leadership_data, info.activity_data, info.interests_data)