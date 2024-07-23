import streamlit as st
import os

# Function to serve static files
def serve_static_file(path):
    with open(path, 'r') as file:
        return file.read()

# Path to HTML file
html_file_path = os.path.join(os.getcwd(), 'index.html')

# Read HTML content
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Serve the static files (CSS and JS)
css_path = os.path.join(os.getcwd(), 'static/css/styles.css')
js_path = os.path.join(os.getcwd(), 'static/js/script.js')

with open(css_path, 'r') as file:
    css_content = file.read()

with open(js_path, 'r') as file:
    js_content = file.read()

# Set up Streamlit to use custom HTML
st.set_page_config(page_title="HeroVerge - AI Support Platform")
st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)
st.markdown(html_content, unsafe_allow_html=True)
st.markdown(f'<script>{js_content}</script>', unsafe_allow_html=True)

# Example of handling form submission
if st.button("Send"):
    user_message = st.text_area("Enter your query:")
    model_choice = st.selectbox("Choose Model:", ["llama2", "llama3_70b", "llama3_8b"])
    
    if model_choice == "llama2":
        response = prompt_llama2("System prompt here", user_message)
    elif model_choice == "llama3_70b":
        response = prompt_llama3_70b("System prompt here", user_message)
    else:
        response = prompt_llama3_8b("System prompt here", user_message)
    
    st.json(response)

# Ensure your model functions and imports are properly defined here
# from model import prompt_llama2, prompt_llama3_70b, prompt_llama3_8b
