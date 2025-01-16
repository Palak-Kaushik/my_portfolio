import streamlit as st

def render_projects():
    st.header("Projects")
    projects = [
        {
            "name": "Accelerated LLM",
            "description": "Increases efficiency of LLMs by 95 percent by reducing computations performed while preserving response quality and reduces hallucinations in responses, thereby reducing response time and increasing the accuracy. Runner up in IEEE CIS Flame Technical Challenge, ranking number 4 globaly.",
            #"link": "",
            
        },
        {
            "name": "Vyakriti SAR",
            "description": "Detects man-made changes from SAR images; Field Programmable Gate Array optimised to perform change detection, which speeds up the process by 3.68 times than a GPU and 9.01 times than CPU; automatically explains the change detected in SAR image. Finalist in Smart India Hackathon 2024.",
            #"link": "https://earthengine.google.com/",
        },
        {
            "name": "Port Surveillance",
            "description": "Performs 2 factor authentication on all incoming and outgoing vehicles on port region to identify each vessel; detects anomalies and unauthenticated vessels from security perspective.",
            #"link": "https://www.raspberrypi.org/",
        },
        {
            "name": "First Aid Helpline LLM",
            "description": "Provides immediate, multilingual (English, Hindi) first aid advice during emergencies over a helpline number; reduces fatalities during the critical period before an ambulance arrives; uses RAG to ensure quality responses.",
            #"link": "https://www.twilio.com/",
        },
        {
            "name": "Women’s Health Recommendation System",
            "description": "Predicts current phase of menstrual cycle (menstrual, follicular, ovulatory and luteal); uses a RAG powered LLM (Flan-T5) to provide answers to user queries about women's health; all datasets for the LLM have been self-created ensuring accuracy and relevance.",
            #"link": "https://huggingface.co",
        },
    ]

    for project in projects:
        st.subheader(project["name"])
        st.write(f"{project['description']}")
        #st.markdown(f"[Project Link]({project['link']})")

