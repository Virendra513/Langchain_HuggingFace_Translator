import streamlit as st
from model import translate_text

st.title("English to Hindi Translator")

# User input
text_to_translate = st.text_area("Enter text in English:")

# Button to trigger translation
if st.button("Translate"):
    if text_to_translate:
        # Call the translation function
        output = translate_text(text_to_translate)
        st.write("Translation in Hindi:", output)
    else:
        st.error("Please enter some text to translate.")
