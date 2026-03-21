import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

resume_text = """
John Doe
Software Engineer
Did some projects in college. Know Python and Java.
Worked at a startup for 2 months.
"""

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

print(response.choices[0].message.content)