import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.title("AI Physics Tutor")

question = st.text_input("Ask your Physics doubt:")

if st.button("Get Answer"):
    if question == "":
        st.write("Please type a question.")
    else:
        response = client.responses.create(
            model="gpt-5-nano",
          input="""
You are an expert JEE/NEET Physics teacher.
Explain step by step in simple English.
Use formulas only when needed.
Give one small example.
Student question:
""" + question
        )

        st.write(response.output_text)
