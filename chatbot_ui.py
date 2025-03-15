import streamlit as st
import json

# Load chatbot responses from chatbot_results.json
with open("chatbot_results.json", "r", encoding="utf-8") as f:
    chatbot_data = json.load(f)

# Extract Groq responses
groq_responses = {item["question"]: item["answer"] for item in chatbot_data["Groq LLaMA3-70B"]}

# Streamlit UI Configuration
st.set_page_config(page_title="AI Chatbot - Professional & Interactive", page_icon="💬", layout="wide")

# **🎨 Professional UI Styles**
custom_css = """
<style>
    body {
        background-color: #E3F2E1; /* Light green background */
        color: black; /* Set all text to black */
    }
    .stApp {
        background-color: #E3F2E1;
    }
    .stTextInput > div > div > input {
        border: 2px solid #4CAF50 !important;
        border-radius: 10px;
        font-weight: bold;
        color: white !important; /* User input text is now white */
        background-color: #2C5F2D !important; /* Dark green input box */
        padding: 10px;
    }
    .stButton>button {
        background-color: #4CAF50 !important; /* Green button */
        color: white !important;
        font-size: 16px !important;
        padding: 10px 20px !important;
        border-radius: 10px !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45A049 !important;
    }
    .stMarkdown {
        font-size: 18px;
        font-weight: bold;
        color: black !important; /* Ensure all text is black */
    }
    .example-questions {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        font-size: 16px;
    }
    .example-questions div {
        background-color: #C8E6C9;
        padding: 10px 15px;
        border-radius: 8px;
        border: 2px solid #2C5F2D;
        width: 45%;
        text-align: center;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# **💬 Professional Header**
st.markdown(
    """
    <h1 style='text-align: center;'>💬 AI Chatbot - Professional & Interactive</h1>
    <p style='text-align: center; font-size: 18px;'>Ask any question about my background, experience, or research. The AI will respond as <b>if it were me.</b></p>
    """,
    unsafe_allow_html=True,
)

# **💡 Example Questions - Professionally Aligned**
st.markdown("### 💡 Example Questions")
st.markdown(
    """
    <div class="example-questions">
        <div>🔹 What is your highest level of education?</div>
        <div>🔹 How many years of work experience do you have?</div>
        <div>🔹 What are your research interests?</div>
        <div>🔹 Can you describe your current role?</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# **🔍 User Input Field**
user_question = st.text_input("🔍 Ask a question:", help="Type your question here.")

# **🟢 Submit Button**
if st.button("Get Answer"):
    if user_question.strip():
        with st.spinner("🤖 Thinking..."):
            # Retrieve answer from JSON
            answer = groq_responses.get(user_question, "I'm sorry, I don't have an answer to that question.")

            # **💬 Display Answer in a Professional Styled Box**
            st.markdown(
                f"""
                <div style='background-color: #F5F5F5; padding: 15px; border-radius: 10px; border: 2px solid black;'>
                    <b>🗨️ Response:</b>  
                    {answer}
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.warning("⚠️ Please enter a question!")
