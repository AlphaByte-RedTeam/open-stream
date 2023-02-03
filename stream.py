import os
import streamlit as st
import openai

with open("./SECRETS.env") as f:
    for line in f:
        name, value = line.strip().split("=")
        os.environ[name] = value

api_key = os.getenv("OPENAI_KEY")
openai.api_key = api_key


def generate_response(usr_prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=usr_prompt,
        temperature=0.5,
        n=1,
        stop=None,
        max_tokens=1024,
    )

    return response.choices[0].text


st.title("OpenAI Code Completion")

prompt = st.text_input("Place your instruction here..")

if st.button("Code generations"):
    res = generate_response(prompt)
    st.write(res)
