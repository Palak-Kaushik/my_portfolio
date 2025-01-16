import streamlit as st

def render_skills():
    st.header("Skills")


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
    [About Me](#palak-kaushik)

    [Skills](#skills)

    [Work Experience](#work-experience)

    [Projects](#projects)

    [Achievements](#achievements)

    [Publications](#publications)

    [Contact Me](#contact-me)
    """, unsafe_allow_html=True)

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
            <span>Machine Learning</span>
        </div>
        <div class="tech-item">
            <span>Natural Language Processing</span>
        </div>
        <div class="tech-item">
            <span>Computer Vision</span>
        </div>
        <div class="tech-item">
            <span>Neural Networks</span>
        </div>
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
            <img src="https://upload.wikimedia.org/wikipedia/commons/7/77/Streamlit-logo-primary-colormark-darktext.png" alt="Jupyter">
            <span>Streamlit</span>
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



