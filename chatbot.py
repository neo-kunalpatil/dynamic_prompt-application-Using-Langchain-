from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()

st.header("welcome to Kunal ChatBot")

model= GoogleGenerativeAI(model= "gemini-3.8-flash")


user_input= st.chat_input("write prompt: ")
if user_input:
    if user_input=="exit":
        st.write("good bye")
    else:
         with st.spinner("Thinking..."):
          result= model.invoke(user_input)
          st.write(result)


