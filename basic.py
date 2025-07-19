import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)


generation_config = genai.GenerationConfig(
    max_output_tokens=1000,
    temperature=0.3
)

def generate_response(prompt):
    try:  # Place the try block inside the function
        contents = [
            {
                "role": "model",  # You may need to specify "model" role
                "parts": "You are a sweet and wholesome chatbot. You are very kind to the user and always try to make them happy. You are always eager to chat and help the user.",
                "parts": "You are funny and warm-hearted. Give the user a compliment and make them smile."
            },
            {
                "role": "user",  # Specify "user" role for the prompt
                "parts": prompt
            }
        ]
        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(contents, generation_config=generation_config)
        return response.text
    
    except Exception as e:  # Catch exceptions raised during execution
        st.error(f"Something went wrong: {e}")
        print(f"Error: {e}")
        return None  # Return None or an appropriate fallback value



try:
    st.set_page_config(layout="wide")
    st.title("Wholesome Chatbot")  
    st.write("Welcome to the Wholesome Chatbot!")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("User Prompt")
        user_prompt = st.text_area("Enter your prompt here:")
        generate_code = ""
        if st.button("Generate"):  # Move the button here
            if user_prompt:
                generate_code = generate_response(user_prompt)
            else:
                st.warning("Please enter a prompt to generate a response.")

    with col2:
        if user_prompt:
            st.subheader("Generated response:")
            st.text_area("Response:", value=generate_code, height=400)

except Exception as e:
    st.error(f"Something went wrong")
    print(f"Error: {e}")