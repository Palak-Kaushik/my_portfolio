import streamlit as st

def render_work_exp():
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