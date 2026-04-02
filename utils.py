#analyzing word count-doing a function on my own
#no int or any decleration required for varaibles
#no flower brackets in python, no int declertions in python
#no semilicons in python
# & is written as and in python
#f{} this is an fstring to print input and also make sure INDENTATION is correct
#else-if is written as elif and then end with :
# no paranthesis required for if in python, but at end we need :
#reader opens the pdf and understands its structure
#for pages...goes through each page in pdf one by one
#text+= adds each page's text to a growing string
#return text hands back all the text combined.
import PyPDF2
def analyze_word_count(resume_text):
    count_of_words = len(resume_text.strip().split())
    
    if count_of_words < 400:
        return f"Ideal range is 400-600, your resume has {count_of_words} words"
    elif count_of_words > 600:
        return f"Ideal range is 400-600, your resume has {count_of_words} words"
    else:
        return f"Your resume meets the ideal range, it has {count_of_words} words"

# test it, this has to be in same indented with def if its inside def it won't work
print(analyze_word_count("some resume text here"))
print(analyze_word_count("word " * 450))
print(analyze_word_count("word " * 1000))

def extract_text_from_pdf(uploaded_file):
    reader=PyPDF2.PdfReader(uploaded_file)
    text=""
    for page in reader.pages:
        text+=page.extract_text()
    return text

#2MB validation function
def validate_file_size(uploaded_file):
    size_of_file=uploaded_file.size
    if size_of_file>2*1024*1024:
        return False
    else:
        return True
