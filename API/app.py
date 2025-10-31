from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate 
from langchain_openai import ChatOpenAI
from langserve import add_routes
import os
import uvicorn
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')
app=FastAPI(
    title="langchain server",
    version="1.0",
    description="Asinple API server"
)
add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
model=ChatOpenAI()
llm=Ollama(model="gemma3:1b")
prompt1=ChatPromptTemplate.from_template("write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("write an poem about {topic} for five year child ")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)
add_routes(
    app,
    prompt2|llm,
    path="/poem"
)
if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
