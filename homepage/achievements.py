import streamlit as st

def render_achievements():
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
            color: #000000;
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
            <div class="links">
            <div class="link">
            <a href="https://cis.ieee.org/activities/educational-activites/competitions/flame-technical-challenge-2024-final-submissions"> Finalists
            </div>
            <div class="link">
            <a href="https://youtu.be/Op2wBcxx0TA"> Video
            </div>
            </div>
            
        </div>
        """,
        
        unsafe_allow_html=True,
    )
    st.image("./assets/flame1.jpeg")

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


    col1, col2 = st.columns(2)
    # Display images in each column
    with col1:
        st.image("./assets/sih24_1.jpeg",)# use_container_width=True)

    with col2:
        st.image("./assets/sih24_3.jpeg",)# use_container_width=True)

    with col1:
        st.image("./assets/sih24_2.jpeg",)# use_container_width=True)

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
    st.image("./assets/ichack.png")

