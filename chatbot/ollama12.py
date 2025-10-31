#LANGCHAIN_API_KEY=""
#OPENAI_API_KEY=""
#LANGCHAIN_PROJECT="myproject1"

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama 

import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()


os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are helpful assistance. please provied the user responce to the user queries "),
        ("user","Question: {question}")
    ]
)
st.title("Langchain Demo with Ollama API")
input_text=st.text_input("search the topic you want")

llm=Ollama(model="gemma3:1b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
