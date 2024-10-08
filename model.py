import langchain_huggingface
import os
from dotenv import load_dotenv
from langchain import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

import os
from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()

# Step 1: Initialize the Hugging Face model for English to Hindi translation
llm = HuggingFaceHub(repo_id="Helsinki-NLP/opus-mt-en-hi")

# Step 2: Create a prompt template for translation
translation_prompt = PromptTemplate(
    input_variables=["text"],
    template="{text}"
)

# Step 3: Create the translation chain
translation_chain = LLMChain(llm=llm, prompt=translation_prompt)
# text_to_translate = "Hello, I am well and wish you the best for tommorow's exam?"
# output = translation_chain({"text": text_to_translate})
# print(output)


def translate_text(text):
    """Function to translate text from English to Hindi."""
    return translation_chain({"text": text})
