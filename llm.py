from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

st.title("Lokesh new chatbot")
input_text=st.text_input("Please enter your queries")

prompt=ChatPromptTemplate.from_messages(
    [("system","you are a helpful AI assistant."),
     ("user","user query:{query}")
    ])

llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"query":input_text}))