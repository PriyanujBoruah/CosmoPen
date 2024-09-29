import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

GOOGLE_API_KEY = 'AIzaSyDmF4D2f_ibz6UZi_sFZyydkSmUrz7x8_k'
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.0-pro')
modelx = genai.GenerativeModel('gemini-1.5-flash')

def RESEARCH_PAPER_SUMMARIZER(RESEARCH_SUMMARY_FOCUS, RESEARCH_SUMMARY_LENGTH, RESEARCH_SUMMARY_TEXT):
    RESEARCH_SUMMARY = modelx.generate_content(f"""
Provide a summary of the research paper below, focusing on {RESEARCH_SUMMARY_FOCUS}.
The summaries should be in the form of a {RESEARCH_SUMMARY_LENGTH.replace(' Summary ', ' ').replace('(', '').replace(')', '')}.

Research Paper:
[
{RESEARCH_SUMMARY_TEXT}
]
""")
    return RESEARCH_SUMMARY.text

def CHAPTER_EXPLAINER(CHAPTER_EXPLAINER_BOOK, CHAPTER_EXPLAINER_TARGET):
        CHAPTER_EXPLAINER = modelx.generate_content([f"""
You are an AI assistant helping a student understand a chapter from a PDF document. 
Chapter Text: [
{CHAPTER_EXPLAINER_BOOK}
]
Student Grade: [{CHAPTER_EXPLAINER_TARGET}]
Provide a detailed explanation of the chapter that is clear, concise, and informative.
Make sure to cover and explain every topic in the chapter.
    """],
    safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH
        })
        return CHAPTER_EXPLAINER.text

def QUESTION_PAPER_GENERATION(QUESTION_PAPER_SUBJECT, QUESTION_PAPER_LEVEL, QUESTION_PAPER_TYPES, QUESTION_PAPER_NUMBERS, QUESTION_PAPER_TIME, QUESTION_PAPER_BOOK):
        QUESTION_PAPER = modelx.generate_content([f"""
Generate a question paper for [{QUESTION_PAPER_SUBJECT}] at the [{QUESTION_PAPER_LEVEL}] level for the given chapter.

Include these question types: [{QUESTION_PAPER_TYPES}]
The question paper should only have [{QUESTION_PAPER_NUMBERS}] questions. 
[Optional: The estimated time limit is [{QUESTION_PAPER_TIME} minutes]. 

Make the questions clear, concise, and relevant to the specified learning objectives.

Chapter Text:
[
{QUESTION_PAPER_BOOK}
]

Give the answer key at the end of the question paper.
    """],
    safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH
        })
        return QUESTION_PAPER.text

def STUDY_GUIDE_CREATOR(STUDY_GUIDE_TYPE, STUDY_GUIDE_BOOK):
    FORMAT_TYPE = ', '.join(STUDY_GUIDE_TYPE)
    STUDY_GUIDE = modelx.generate_content(f"""
Create a study guide from the text below, including the following elements: {FORMAT_TYPE}.
Study Material:
[
{STUDY_GUIDE_BOOK}
]
""")
    return STUDY_GUIDE.text