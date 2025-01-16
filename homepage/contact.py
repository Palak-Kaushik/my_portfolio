import streamlit as st


def render_contact_me():
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
        <form action="https://formsubmit.co/d527885a16d5a4293c47f66b7b4e3428" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your Message" rows="5" required></textarea>
            <button type="submit">Send Message</button>
        </form>

    </div>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

