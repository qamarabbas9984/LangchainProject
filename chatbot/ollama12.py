#LANGCHAIN_API_KEY="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"
#OPENAI_API_KEY="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"
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