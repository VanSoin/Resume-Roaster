import os
import time
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# rate limiting setup
if "last_request_time" not in st.session_state:
    st.session_state.last_request_time = 0

# caching setup
if "cache" not in st.session_state:
    st.session_state.cache = {}

st.set_page_config(page_title="Resume Roaster", page_icon="🔥")

st.title("🔥 Resume Roaster")
st.subheader("Paste your resume below and get brutally honest AI feedback")

resume_text = st.text_area("Your Resume", height=300, placeholder="Paste your resume text here...")

if st.button("Roast My Resume"):
    word_count = len(resume_text.strip().split())
    time_since_last = time.time() - st.session_state.last_request_time

    # input validation
    if resume_text.strip() == "":
        st.warning("Please paste your resume first!")
    elif word_count < 50:
        st.warning("This seems too short to be a resume. Please paste your full resume.")
    elif word_count > 2000:
        st.warning("Your resume is too long. Please trim it to under 2000 words.")

    # rate limiting
    elif time_since_last < 10:
        st.warning(f"Please wait {int(10 - time_since_last)} seconds before trying again.")

    else:
        # caching — if same resume was already analysed, return saved result
        cache_key = resume_text.strip()
        if cache_key in st.session_state.cache:
            st.info("Showing cached result for this resume.")
            st.markdown(st.session_state.cache[cache_key])

        else:
            # error handling
            try:
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

                # save result to cache and update last request time
                st.session_state.cache[cache_key] = feedback
                st.session_state.last_request_time = time.time()

                st.success("Here's your roast!")
                st.markdown(feedback)

            except Exception as e:
                st.error("Something went wrong while analysing your resume. Please try again in a moment.")