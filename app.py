import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv(r"C:\Users\Vikrant Vivek Deo\Documents\GEN-AI\LangChain\OPENAI & OLLAMA\Ollama_Project\venv\.env")
load_dotenv()

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate #My own chat template
from langchain_core.output_parsers import StrOutputParser #removes metadata or other json etc data from o/p
load_dotenv()
#Langsmith Tracking
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_TRACING_V2"]="true"
os.environ["LANGSMITH_PROJECT"]=os.getenv("LANGSMITH_PROJECT")


##Prompt Template design
prompt=ChatPromptTemplate.from_messages(
    [("system","You are a helpful assistant. Please respond to the question asked"),
     ("user","Question:{question}")
]
)

##Streamlit Framework design:
st.title("Langchain demo with Gemma 2B")
input_text=st.text_input("Do you have any question in mind?")

## Ollama Llama2 Model:
#from langchain_community.llms import Ollama
llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()

chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))