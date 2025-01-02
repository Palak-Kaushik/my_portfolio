import streamlit as st

# Set up the page
st.set_page_config(page_title="Palak Kaushik | ML Developer")


st.title("Palak Kaushik")
st.markdown('###')
# Layout with columns
col1, col2 = st.columns([1, 2])  # Adjust column ratio as needed

# Left column: Photo
with col1:
    st.image(
    r"./assets/profile_photo.jpeg",
    width=200,  # Keep this in sync with your desired display size
    use_column_width=False
)


# Right column: Information
with col2:
    st.write("B.E. CSE (Hons AI ML) | Machine Learning Engineer | Natural Language Processing (NLP)")
    st.markdown(
        """
        - **Email**: [mailboxpalak@gmail.com](mailto:mailboxpalak@gmail.com)
        - **GitHub**: [github.com/Palak-Kaushik](https://github.com/Palak-Kaushik)
        - **LinkedIn**: [linkedin.com/in/kaushik-palak](https://linkedin.com/in/kaushik-palak)
        - **Phone**: +91 9811097963
        """
    )


###########################################################33


# About Me Section
st.header("About Me")
st.write("""
I’m pursuing my Bachelor of Engineering in CSE with specialization in AI and ML. I like to keep up with the latest trends in technology and have a strong appetite for knowledge. I am a good team player and my goal is to leverage AI to solve real-world challenges, specifically in the field of healthcare and defence.

""")

#############################################################3

# Skills Section
st.header("Skills")
# Sidebar for index navigation
import streamlit as st

# Sidebar content with proper markdown links
st.sidebar.title("Sections")
st.sidebar.markdown("""
                    
<style>
    a {
        text-decoration: none;
        color: inherit;
    }
    a:hover {
        text-decoration: none;
        color: inherit;
    }
</style>
[Profile](#palak-kaushik)

[About Me](#about-me)

[Skills](#skills)

[Work Experience](#work-experience)

[Projects](#projects)

[Achievements](#achievements)

[Publications](#publications)

[Contact Me](#contact-me)
""", unsafe_allow_html=True)



st.write("Machine Learning, Natural Language Processing, Computer Vision, Neural Networks")

# HTML for Tech Stack with Icons
st.markdown("""
<style>
.tech-stack {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
}
.tech-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 5px 10px;
    border: 1px solid #ddd;
    border-radius: 10px;
    background-color: #f9f9f9;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
}
.tech-item img {
    height: 25px;
}
</style>
<div class="tech-stack">
    <div class="tech-item">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg">
        <span>Sci-Kit Learn</span>
    </div>
    <div class="tech-item">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/ab/TensorFlow_logo.svg">
        <span>TensorFlow</span>
    </div>
    <div class="tech-item">
        <img src="https://upload.wikimedia.org/wikipedia/commons/1/10/PyTorch_logo_icon.svg">
        <span>PyTorch</span>
    </div>
    <div class="tech-item">
        <img src="https://upload.wikimedia.org/wikipedia/commons/9/94/MERN-logo.png">
        <span>MERN Stack</span>
    </div>
    <div class="tech-item">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/c2/GitHub_Invertocat_Logo.svg">
        <span>GitHub</span>
    </div>
    <div class="tech-item">
        <img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg">
        <span>Linux</span>
    </div>
    <div class="tech-item">
        <img src="https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg">
        <span>Jupyter Notebook</span>
    </div>
    <div class="tech-item">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/ae/Keras_logo.svg">
        <span>Keras</span>
    </div>
    <div class="tech-item">
        <img src="https://upload.wikimedia.org/wikipedia/commons/8/88/SpaCy_logo.svg" alt="TensorFlow">
        <span>spaCy</span>
    </div>
    <div class="tech-item">
        <img src="https://miro.medium.com/v2/resize:fit:592/1*YM2HXc7f4v02pZBEO8h-qw.png" alt="PyTorch">
        <span>NLTK</span>
    </div>
    <div class="tech-item">
        <img src="https://registry.npmmirror.com/@lobehub/icons-static-png/latest/files/dark/langchain-color.png" alt="Node.js">
        <span>Langchain</span>
    </div>
    <div class="tech-item">
        <img src="https://cdn.prod.website-files.com/6645c0129428882861d078b8/66603a39bd44aeb85269ceea_655df7e9805dd2bd768367ef_llamaindex-removebg-preview.png" alt="GitHub">
        <span>Llama-index</span>
    </div>
    <div class="tech-item">
        <img src="https://static-00.iconduck.com/assets.00/flask-icon-1594x2048-84mjydzf.png" alt="Linux">
        <span>Flask</span>
    </div>
    <div class="tech-item">
        <img src="https://archive.org/download/github.com-gradio-app-gradio_-_2022-10-06_12-54-59/cover.jpg" alt="Jupyter">
        <span>Gradio</span>
    </div>
    <div class="tech-item">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/03/Git_format.png" alt="Node.js">
        <span>Git</span>
    </div>
    <div class="tech-item">
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/5f/Windows_logo_-_2012.svg" alt="GitHub">
        <span>Windows</span>
    </div>
    <div class="tech-item">
        <img src="https://upload.wikimedia.org/wikipedia/commons/7/7b/Ubuntu-logo-no-wordmark-solid-o-2022.svg" alt="Linux">
        <span>Ubuntu</span>
    </div>
    <div class="tech-item">
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/4a/Debian-OpenLogo.svg" alt="Jupyter">
        <span>Debian</span>
    </div>
</div>
""", unsafe_allow_html=True)




# Custom CSS for timeline styling
st.markdown(
    """
    <style>
    .timeline {
        display: flex;
        flex-direction: column;
        margin: 0;
        padding: 0;
        list-style: none;
    }

    .timeline-item {
        display: flex;
        margin: 20px 0;
    }

    .timeline-time {
        flex: 1;
        max-width: 150px;
        font-size: 0.9rem;
        color: #7f8c8d;
        text-align: right;
        padding-right: 20px;
        border-right: 2px solid #2c3e50;
    }

    .timeline-content {
        flex: 3;
        padding-left: 20px;
    }

    .timeline-content h3 {
        margin: 0;
        font-size: 1.2rem;
        color: #2c3e50;
    }

    .timeline-content p {
        margin: 5px 0 0;
        font-size: 1rem;
        color: #34495e;
    }

    .certificate-link {
        font-size: 0.9rem;
        color: #2980b9;
        text-decoration: none;
    }

    .certificate-link:hover {
        text-decoration: underline;
    }

    
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.header("Work Experience")

# Timeline structure
st.markdown(
    """
    <ul class="timeline">
        <li class="timeline-item">
            <div class="timeline-time">Sep 2024 - Nov 2024</div>
            <div class="timeline-content">
                <h3>AI Intern</h3>
                <p>Crystal Ball AI Technologies Pvt Ltd</p>
                <p>Worked on aParently, which enables parents to ask queries about their children. Contributed to a domain-specific LLM that personalizes responses based on user preferences and history, and worked on recommendation systems. </p>
            </div>
        </li>
        <li class="timeline-item">
            <div class="timeline-time">Jul 2024 - Aug 2024</div>
            <div class="timeline-content">
                <h3>Machine Learning Engineer Intern</h3>
                <p>Kishiva</p>
                <p>Developed UniGPT, which allows users to efficiently search and query their own organizational documents, enabling easy retrieval of relevant information from large document repositories.</p>
            </div>
        </li>
        <li class="timeline-item">
            <div class="timeline-time">Jun 2023 - Dec 2023</div>
            <div class="timeline-content">
                <h3>Secretary</h3>
                <p>IEEE Computational Intelligence Society, CUSB</p>
                <p>As the Secretary at IEEE CIS CUSB, I acquired experience in team management, leadership, and making critical time sensitive decisions.</p>
            </div>
        </li>
    </ul>
    """,
    unsafe_allow_html=True,
)


###################################


# Projects Section
st.header("Projects")
projects = [
    {
        "name": "Accelerated LLM",
        "description": "Increases efficiency of LLMs by 95 percent by reducing computations performed while preserving response quality and reduces hallucinations in responses, thereby reducing response time and increasing the accuracy. Runner up in IEEE CIS Flame Technical Challenge, ranking number 4 globaly.",
        "link": "https://huggingface.co",
        
    },
    {
        "name": "Vyakriti SAR",
        "description": "Detects man-made changes from SAR images; Field Programmable Gate Array optimised to perform change detection, which speeds up the process by 3.68 times than a GPU and 9.01 times than CPU; automatically explains the change detected in SAR image. Finalist in Smart India Hackathon 2024.",
        "link": "https://earthengine.google.com/",
    },
    {
        "name": "Port Surveillance",
        "description": "Performs 2 factor authentication on all incoming and outgoing vehicles on port region to identify each vessel; detects anomalies and unauthenticated vessels from security perspective.",
        "link": "https://www.raspberrypi.org/",
    },
    {
        "name": "First Aid Helpline LLM",
        "description": "Provides immediate, multilingual (English, Hindi) first aid advice during emergencies over a helpline number; reduces fatalities during the critical period before an ambulance arrives; uses RAG to ensure quality responses.",
        "link": "https://www.twilio.com/",
    },
    {
        "name": "Women’s Health Recommendation System",
        "description": "Predicts current phase of menstrual cycle (menstrual, follicular, ovulatory and luteal); uses a RAG powered LLM (Flan-T5) to provide answers to user queries about women's health; all datasets for the LLM have been self-created ensuring accuracy and relevance.",
        "link": "https://huggingface.co",
    },
]

for project in projects:
    st.subheader(project["name"])
    st.write(f"{project['description']}")
    st.markdown(f"[Project Link]({project['link']})")

###############################################


# Custom CSS for achievements section
st.markdown(
    """
    <style>
    .achievement {
        margin: 20px 0;
        padding: 10px;
        border-left: 5px solid #2980b9;
        background-color: #ecf0f1;
        font-size: 1.1rem;
        color: #34495e;
    }

    .achievement-title {
        font-weight: bold;
        font-size: 1.2rem;
        color: #2c3e50;
    }

    .achievement-description {
        margin-top: 5px;
        margin-left: 20px;
        font-size: 1rem;
        color: #7f8c8d;
    }

    .achievement-image {
        height: 60px;
        margin-right: 15px;
        vertical-align: middle;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header for Achievements
st.header("Achievements")

# Achievement 1
st.markdown(
    """
    <div class="achievement">
        <img src="https://edu.ieee.org/in-reva/wp-content/uploads/sites/33/IEEE-CIS-logo-RGB-300ppi.png" class="achievement-image" alt="IEEE CIS Flame Logo">
        <div class="achievement-title">IEEE CIS Flame Technical Challenge Runner-Up</div>
        <div class="achievement-description">
            My team, VYAKRITI 2.0 secured fourth position globally by optimizing LLMs to reduce computational time and space complexity by 95% while preserving response quality.
        </div>
        
    </div>
    """,
    
    unsafe_allow_html=True,
)
st.image("./assets/flame1.jpeg", use_column_width=True)
#st.image("./assets/flame2.jpeg", use_column_width=True)

# Achievement 2
st.markdown(
    """
    <div class="achievement">
        <img src="https://www.sih.gov.in/img1/logo/SIH_logo_2024_horizontal.png" class="achievement-image" alt="Smart India Hackathon 2024 Logo">
        <div class="achievement-title">Smart India Hackathon 2024 Finalist</div>
        <div class="achievement-description">
            Ranked among the top 5 teams in India, demonstrating skills in teamwork, problem-solving, ability to come up with novel solutions as well as expertise in remote sensing.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Achievement 3
st.markdown(
    """
    <div class="achievement">
        <img src="https://i0.wp.com/opportunitycell.com/wp-content/uploads/2022/03/SIH2.png?fit=327%2C345&ssl=1" class="achievement-image" alt="Smart India Hackathon 2023 Logo">
        <div class="achievement-title">Smart India Hackathon 2023 Finalist</div>
        <div class="achievement-description">
            Ranked among the top 7 teams, demonstrating teamwork and the ability to develop innovative solutions.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Achievement 4
st.markdown(
    """
    <div class="achievement">
        <img src="https://d112y698adiu2z.cloudfront.net/photos/production/challenge_thumbnails/002/206/981/datas/original.png" class="achievement-image" alt="IC Hack 2.0 Logo">
        <div class="achievement-title">IC Hack 2.0 Top 10 - Computer Vision Track</div>
        <div class="achievement-description">
            Secured top 10 position in Computer Vision track by developing an innovative solution to prevent road accidents caused by driver drowsiness.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)



################################################

# Publications Section
st.header("Publications")
st.write("""
**P. Kaushik and A. Sharma**, "Analysing Paralinguistic Information from Human Speech and its Applications in Medicine," 
2023 International Conference on Advances in Electronics, Communication, Computing and Intelligent Information Systems (ICAECIS),
Bangalore, India, 2023, pp. 55-59, doi: 10.1109/ICAECIS58353.2023.10170105.
[IEEE Link](https://ieeexplore.ieee.org/document/10170105)
""")





# Contact Section
st.header("Contact Me")
st.markdown("""
Feel free to reach out to me for collaborations, opportunities, or just to say hello! Use the form below to send me a message.
""")

contact_form = """
<style>
    .form-container {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        background: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .form-container input, .form-container textarea {
        width: calc(100% - 20px);
        margin: 10px 0;
        padding: 10px;
        font-size: 16px;
        border: 1px solid #ddd;
        border-radius: 5px;
        box-sizing: border-box;
    }
    .form-container button {
        background: #00c4ff;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .form-container button:hover {
        background: #008bb0;
    }
</style>
<div class="form-container">
    <form action="https://formsubmit.co/mailboxpalak@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" rows="5" required></textarea>
        <button type="submit">Send Message</button>

</div>
"""
st.markdown(contact_form, unsafe_allow_html=True)

