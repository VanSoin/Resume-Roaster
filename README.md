# Resume Roaster 🔥
An AI-powered resume analyzer that gives brutally honest feedback.

## Features
- AI analysis scoring Clarity, Impact, and ATS Compatibility
- 3 specific actionable improvements
- PDF upload support with text extraction
- File size validation (2MB limit)
- Word count analysis with ideal range guidance
- Rate limiting to prevent API spam
- Caching so same resume isn't analysed twice

## Tech Stack
- Python
- Streamlit
- Groq API (Llama 3.3 70B)
- PyPDF2

## Project Structure
```
resume-roaster/
├── app.py       # Streamlit UI
├── utils.py     # Core logic (extraction, validation)
├── .env         # API key (never commit this)
└── requirements.txt
```

## How to Run Locally
1. Clone the repo
   git clone https://github.com/vanshikasoin/resume-roaster.git

2. Install dependencies
   pip install -r requirements.txt

3. Create .env file
   GROQ_API_KEY=your_key_here

4. Run the app
   streamlit run app.py

## Running with Docker

1. Build the image
   docker build -t resume-roaster .

2. Run the container
   docker run -p 8501:8501 --env-file .env resume-roaster

3. Open in browser
   http://localhost:8501

## Note
Never commit your .env file. Add it to .gitignore.
