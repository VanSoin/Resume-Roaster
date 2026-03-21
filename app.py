import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Resume Roaster", page_icon="🔥")

st.title("🔥 Resume Roaster")
st.subheader("Paste your resume below and get brutally honest AI feedback")

resume_text = st.text_area("Your Resume", height=300, placeholder="Paste your resume text here...")

if st.button("Roast My Resume"):
    if resume_text.strip() == "":
        st.warning("Please paste your resume first!")
    else:
        with st.spinner("Analysing your resume..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a brutally honest resume reviewer. Analyse the resume and give scores out of 10 for: Clarity, Impact, and ATS Compatibility. Then list 3 specific improvements."
                    },
                    {
                        "role": "user",
                        "content": f"Review this resume:\n\n{resume_text}"
                    }
                ]
            )
            feedback = response.choices[0].message.content

        st.success("Here's your roast!")
        st.markdown(feedback)