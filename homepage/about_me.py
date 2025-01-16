import streamlit as st

def render_about_me():
    st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
    }
    .main-header {
        color: #2c3e50;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0.5em;
    }
    .sub-header {
        color: #34495e;
        font-size: 1.2rem;
        margin-bottom: 2em;
    }
    .contact-link a {
        color: #2980b9;
        text-decoration: none;
    }
    .contact-link a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )

    # Header Section
    st.markdown("<div class='main-header'>Palak Kaushik</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>B.E. CSE (Hons AI ML) | Machine Learning Engineer | Natural Language Processing (NLP)</div>", unsafe_allow_html=True)


    st.markdown('###')
    # Layout with columns
    col1, col2 = st.columns([1, 2])  # Adjust column ratio as needed

    # Left column: Photo
    with col1:
        st.image(
        r"./assets/profile_photo.jpeg",
        #use_container_width=True,  # Keep this in sync with your desired display size
    )


    # Right column: Information
    with col2:

        st.write("I’m pursuing my Bachelor of Engineering in CSE with specialization in AI and ML. I like to keep up with the latest trends in technology and have a strong appetite for knowledge. I am a good team player and my goal is to leverage AI to solve real-world challenges, specifically in the field of healthcare and defence.")
        
        st.markdown("""
        <style>
        .links {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
    }
    .link {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 5px 10px;
        border: 1px solid #ddd;
        border-radius: 10px;
        background-color: #f9f9f9;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }
    </style>
    <div class="links">
        <div class="link">
            <span>mailboxpalak@gmail.com</span>
        </div>
        <div class="link">
            <span><a href="https://linkedin.com/in/kaushik-palak">Linkedin</a></span>
        </div>
        <div class="link">
            <span><a href="https://github.com/Palak-Kaushik">GitHub</a></span>
        </div>
        
        """, unsafe_allow_html=True)
        # st.markdown(
        #     """
        #     - **Email**: [mailboxpalak@gmail.com](mailto:mailboxpalak@gmail.com)
        #     - **GitHub**: [github.com/Palak-Kaushik](https://github.com/Palak-Kaushik)
        #     - **LinkedIn**: [linkedin.com/in/kaushik-palak](https://linkedin.com/in/kaushik-palak)
        #     - **Phone**: +91 9811097963
        #     """
        # )
#