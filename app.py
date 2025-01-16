import streamlit as st
from homepage import about_me,skills,work_exp,projects,achievements,contact

# Set up the page
st.set_page_config(page_title="Palak Kaushik | ML Engineer")

about_me.render_about_me()
skills.render_skills()
work_exp.render_work_exp()
projects.render_projects()
achievements.render_achievements()



# Publications Section
st.header("Publications")
st.write("""
**P. Kaushik and A. Sharma**, "Analysing Paralinguistic Information from Human Speech and its Applications in Medicine," 
2023 International Conference on Advances in Electronics, Communication, Computing and Intelligent Information Systems (ICAECIS),
Bangalore, India, 2023, pp. 55-59, doi: 10.1109/ICAECIS58353.2023.10170105.
[IEEE Link](https://ieeexplore.ieee.org/document/10170105)
""")

contact.render_contact_me()