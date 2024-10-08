import streamlit as st
from model import translate_text


st.markdown(
    """
    <style>
    body {
        background-color: #F0F2F5;  /* Background color */
    }

    .big-font {
        font-size: 20px !important;
        color: gray;
         text-align: center;  /* Change to your desired color */
    }
    .custom-title {
        font-size: 40px !important;
        color: black;
        text-align: center;
        font-weight: bold;
        text-decoration: underline;  /* Change to your desired color */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Title in the sidebar
st.sidebar.title("Anuvadak- The Transalator")

# Paragraph in the sidebar
st.sidebar.write("""Welcome to our English to Hindi translator application! This tool leverages the powerful LLM (Large Language Model) "Helsinki-NLP/opus-mt-en-hi" model, which is renowned for its high-quality translation capabilities. By utilizing the Langchain-HuggingFace framework, we have created a seamless user experience that allows you to effortlessly translate English text into Hindi.
""")


st.markdown('<p class="custom-title">English to Hindi Translator</p>',unsafe_allow_html=True)
st.write("")


# User input
text_to_translate = st.text_area("Enter/Paste text in English:")

# Button to trigger translation
if st.button("Translate"):
    if text_to_translate:
        # Call the translation function
        output = translate_text(text_to_translate)
        st.write("Translation in Hindi Language is :", output['text'])
    else:
        st.error("Please enter/paste valid to translate.")

st.write("")  # Adds an empty line
st.write("")  # Adds an empty line
st.write("")  # Adds an empty line
st.write("")  # Adds an empty line
st.write("")  # Adds an empty line
st.write("")  # Adds an empty line
st.write("")  # Adds an empty line
st.write("")  # Adds an empty line
st.write("")  # Adds an empty line
st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("")  

st.markdown('<p class="big-font">Designed and Developed by Virendra S    @2024</p>', unsafe_allow_html=True)
