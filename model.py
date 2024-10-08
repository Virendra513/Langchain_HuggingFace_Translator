
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFacePipeline
from langchain import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables from .env file
load_dotenv()

# Step 1: Initialize the Hugging Face model for English to Hindi translation
huggingface_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
llm = HuggingFaceHub(repo_id="Helsinki-NLP/opus-mt-en-hi", token=huggingface_token)


# Step 2: Create a prompt template for translation
translation_prompt = PromptTemplate(
    input_variables=["text"],
    template="Translate the following text to Hindi: {text}"
)

# Step 3: Create the translation chain
translation_chain = LLMChain(llm=llm, prompt=translation_prompt)

# Step 4: Example usage
# text_to_translate = "Hello, I am well and wish you the best for tommorow's exam?"
# output = translation_chain({"text": text_to_translate})

def translate_text(text):
    """Function to translate text from English to Hindi."""
    return translation_chain({"text": text})