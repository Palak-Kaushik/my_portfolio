import streamlit as st

def render_projects():
    st.markdown("#")
    st.header("Projects")
    projects = [
        {
            "name": "Accelerated LLM",
            "description": "Increases efficiency of LLMs by 95 percent by reducing computations performed while preserving response quality and reduces hallucinations in responses, thereby reducing response time and increasing the accuracy. Runner up in IEEE CIS Flame Technical Challenge, ranking number 4 globally.",
            "link": "https://www.youtube.com/watch?v=Op2wBcxx0TA",
        },
        {
            "name": "Vyakriti SAR",
            "description": "Detects man-made changes from SAR images; Field Programmable Gate Array optimized to perform change detection, which speeds up the process by 3.68 times than a GPU and 9.01 times than CPU; automatically explains the change detected in SAR image. Finalist in Smart India Hackathon 2024.",
            # "link": "https://earthengine.google.com/",
        },
        {
            "name": "Port Surveillance",
            "description": "Performs 2-factor authentication on all incoming and outgoing vehicles on port regions to identify each vessel; detects anomalies and unauthenticated vessels from a security perspective.",
            # "link": "https://www.raspberrypi.org/",
        },
        {
            "name": "First Aid Helpline LLM",
            "description": "Provides immediate, multilingual (English, Hindi) first aid advice during emergencies over a helpline number; reduces fatalities during the critical period before an ambulance arrives; uses RAG to ensure quality responses.",
            # "link": "https://www.twilio.com/",
        },
        {
            "name": "Women’s Health Recommendation System",
            "description": "Predicts the current phase of the menstrual cycle (menstrual, follicular, ovulatory, and luteal); uses a RAG-powered LLM (Flan-T5) to provide answers to user queries about women's health; all datasets for the LLM have been self-created ensuring accuracy and relevance.",
            # "link": "https://huggingface.co",
        },
    ]

    # Loop through projects and display them in a styled layout
    for project in projects:
        with st.container():
            st.markdown("---")  # Divider line for better separation
            col1, col2 = st.columns([3, 5])  # Adjust column widths

            with col1:
                st.subheader(project["name"])

            with col2:
                
                st.write(project["description"])
                # Uncomment if links are available
                if project.get("link"):
                    st.markdown(f"[Learn More]({project['link']})", unsafe_allow_html=True)

    st.markdown("---")  # Final divider for consistency

