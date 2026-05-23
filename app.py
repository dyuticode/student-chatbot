import streamlit as st
from google import genai

# Page setup
st.set_page_config(
    page_title="AI Student Assistant",
    page_icon="🤖"
)

# Title
st.title("🤖 AI Student Assistant")

st.write("Ask study-related questions!")

# API key input
api_key = st.text_input(
    "Enter Gemini API Key",
    type="password"
)

if api_key:

    # Gemini client
    client = genai.Client(api_key=api_key)

    # User question
    prompt = st.text_input("Ask your question")

    if prompt:

        # AI response
        response = client.models.generate_content(
            
            model="gemini-2.5-flash",
            contents=prompt
        )

        # Show response
        st.write(response.text)

else:
    st.warning("Please enter Gemini API key.")