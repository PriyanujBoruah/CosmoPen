import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

GOOGLE_API_KEY = 'AIzaSyDmF4D2f_ibz6UZi_sFZyydkSmUrz7x8_k'
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.0-pro')
modelx = genai.GenerativeModel('gemini-1.5-flash')




# # # # # # # # # # # # # # # # # # # # # # # # CONTENT CREATORS & INFLUENCERS # # # # # # # # # # # # # # # # # # # # # # # #

def BLOG_POST_IDEA_GENERATOR(VARIANT, TONE, BLOG_IDEA_TARGET, BLOG_IDEA_NICHE, BLOG_IDEA_LENGTH, BLOG_IDEA_KEYWORDS, BLOG_IDEA_CTA):
    BLOG_POST_IDEA = modelx.generate_content(f"""
Generate {VARIANT} detailed blog post ideas with a {TONE} tone
for a blog targeting {BLOG_IDEA_TARGET} in the niche of {BLOG_IDEA_NICHE}.
The blog posts should be {BLOG_IDEA_LENGTH} and include the following keywords: {BLOG_IDEA_KEYWORDS}.
Each idea should have a call to action focused on {BLOG_IDEA_CTA}."
""")
    return BLOG_POST_IDEA.text

def BLOG_POST_GENERATOR(VARIANT, TONE, BLOG_POST_TOPIC, BLOG_POST_TARGET, BLOG_POST_LENGTH, BLOG_POST_CONTENT):
    BLOG_POST = modelx.generate_content(f"""
Write {VARIANT} blog posts with a {TONE} tone
on the topic: '{BLOG_POST_TOPIC}' targeting {BLOG_POST_TARGET}.
The blog posts should be {BLOG_POST_LENGTH} and follow this content outline: {BLOG_POST_CONTENT}.
""")
    return BLOG_POST.text

def NEWS_ARTICLE_WRITER(VARIANT, TONE, NEWS_ARTICLE_NICHE, NEWS_ARTICLE_TARGET, NEWS_ARTICLE_LENGTH, NEWS_ARTICLE_CONTENT, NEWS_ARTICLE_DATE):
    NEWS_ARTICLE = modelx.generate_content(f"""
Write {VARIANT} news articles in a {TONE} tone "
about {NEWS_ARTICLE_NICHE} for {NEWS_ARTICLE_TARGET} audience. "
The articles should be {NEWS_ARTICLE_LENGTH}, follow this content outline: {NEWS_ARTICLE_CONTENT}, "
and be written as if published on {NEWS_ARTICLE_DATE}.
""")
    return NEWS_ARTICLE.text

def CREATIVE_WRITING_PROMPT(VARIANT, TONE, CREATIVE_WRITING_GENRE, CREATIVE_WRITING_SETTING, CREATIVE_WRITING_THEME, CREATIVE_WRITING_TYPE, CREATIVE_WRITING_UNIQUE):
    CREATIVE_WRITING = modelx.generate_content(f"""
Generate {VARIANT} creative writing prompts with a {TONE} tone in the genre of {CREATIVE_WRITING_GENRE}.
The setting should be {CREATIVE_WRITING_SETTING}, with a theme of {CREATIVE_WRITING_THEME}.
The writing type should be {CREATIVE_WRITING_TYPE}, and include the unique concept of {CREATIVE_WRITING_UNIQUE}.
""")
    return CREATIVE_WRITING.text

def VIDEO_SCRIPT_WRITER(VARIANT, TONE, VIDEO_SCRIPT_TYPE, VIDEO_SCRIPT_TARGET, VIDEO_SCRIPT_CTA, VIDEO_SCRIPT_KEYWORDS, VIDEO_SCRIPT_LENGTH):
    VIDEO_SCRIPT = modelx.generate_content(f"""
Write {VARIANT} video scripts with a {TONE} tone
for a {VIDEO_SCRIPT_LENGTH} {VIDEO_SCRIPT_TYPE} video targeting {VIDEO_SCRIPT_TARGET}.
Incorporate these keywords: {VIDEO_SCRIPT_KEYWORDS} and end with a call to action to {VIDEO_SCRIPT_CTA}.
""")
    return VIDEO_SCRIPT.text

def VIDEO_DESCRIPTION_WRITER(VARIANT, TONE, VIDEO_DESCRIPTION_TITLE, VIDEO_DESCRIPTION_TARGET, VIDEO_DESCRIPTION_TYPE, VIDEO_DESCRIPTION_KEYWORDS, VIDEO_DESCRIPTION_CTA, VIDEO_DESCRIPTION_CONTENT):
    VIDEO_DESCRIPTION = modelx.generate_content(f"""
Write {VARIANT} YouTube video descriptions with a {TONE} tone for a video titled '{VIDEO_DESCRIPTION_TITLE}' targeting {VIDEO_DESCRIPTION_TARGET}.
The video is a {VIDEO_DESCRIPTION_TYPE} about {VIDEO_DESCRIPTION_CONTENT}.
Use these keywords: {VIDEO_DESCRIPTION_KEYWORDS} and include a call to action to {VIDEO_DESCRIPTION_CTA}.
""")
    return VIDEO_DESCRIPTION.text

def HASHTAG_GENERATOR(VARIANT, TONE, HASHTAG_TOPIC, HASHTAG_NAME, HASHTAG_TARGET, HASHTAG_KEYWORDS):
    HASHTAG = modelx.generate_content(f"""
Generate {VARIANT} hashtags with a {TONE} tone related to {HASHTAG_TOPIC} for {HASHTAG_NAME}, targeting {HASHTAG_TARGET}.
Consider these keywords: {HASHTAG_KEYWORDS}.
""")
    return HASHTAG.text




# # # # # # # # # # # # # # # # # # # # # # # # MARKETING & ADVERTISING SPECIALISTS # # # # # # # # # # # # # # # # # # # # # # # #

def CONTENT_PROMOTION_GENERATOR(VARIANT, TONE, CONTENT_PROMO_TYPE, CONTENT_PROMO_PLATFORM, CONTENT_PROMO_TARGET, CONTENT_PROMO_KEYWORDS, CONTENT_PROMO_CTA):
    CONTENT_PROMOTION = modelx.generate_content(f"""
Generate {VARIANT} social media posts with a {TONE} tone
to promote a {CONTENT_PROMO_TYPE} on {CONTENT_PROMO_PLATFORM}
targeting {CONTENT_PROMO_TARGET}. Use the following keywords: {CONTENT_PROMO_KEYWORDS}
and include a call to action to {CONTENT_PROMO_CTA}.
""")
    return CONTENT_PROMOTION.text

def AD_COPYWRITER(VARIANT, TONE, AD_COPY_FORMAT, AD_COPY_TARGET, AD_COPY_LENGTH, AD_COPY_CONTENT):
    AD_COPY = modelx.generate_content(f"""
Write {VARIANT} ad copies with a {TONE} tone
for a {AD_COPY_LENGTH} {AD_COPY_FORMAT} targeting {AD_COPY_TARGET}.
The ad copy should highlight the following product/service description: {AD_COPY_CONTENT}.
""")
    return AD_COPY.text

def CALL_TO_ACTION_GENERATOR(VARIANT, TONE, CTA_CONTENT, CTA_TARGET, CTA_ACTION):
    CALL_TO_ACTION = modelx.generate_content(f"""
Generate {VARIANT} calls to action with a {TONE} tone "
related to {CTA_CONTENT}, targeting {CTA_TARGET}, "
and encouraging them to {CTA_ACTION}.
""")
    return CALL_TO_ACTION.text

def AIDA_COPYWRITER(VARIANT, TONE, AIDA_COPY_CONTENT, AIDA_COPY_TARGET, AIDA_COPY_CTA, AIDA_COPY_PROBLEM, AIDA_COPY_SOLUTION, AIDA_COPY_BENEFIT):
    AIDA_COPY = modelx.generate_content(f"""
Write {VARIANT} marketing copy variations with a {TONE} tone
for {AIDA_COPY_CONTENT} targeting {AIDA_COPY_TARGET} using the AIDA framework.
Problem/Pain Point: {AIDA_COPY_PROBLEM}
Solution: {AIDA_COPY_SOLUTION}
Benefit: {AIDA_COPY_BENEFIT}
Call to Action: {AIDA_COPY_CTA}
""")
    return AIDA_COPY.text

def PAS_COPYWRITER(VARIANT, TONE, PAS_COPY_CONTENT, PAS_COPY_TARGET, PAS_COPY_CTA, PAS_COPY_PROBLEM, PAS_COPY_SOLUTION, PAS_COPY_AGITATION):
    PAS_COPY = modelx.generate_content(f"""
Write {VARIANT} marketing copy variations with a {TONE} tone
for {PAS_COPY_CONTENT} targeting {PAS_COPY_TARGET} using the PAS framework.
Problem/Pain Point: {PAS_COPY_PROBLEM}
Solution: {PAS_COPY_SOLUTION}
Agitation: {PAS_COPY_AGITATION}
Call to Action: {PAS_COPY_CTA}
""")
    return PAS_COPY.text

def GOOGLE_AD_GENERATOR(VARIANT, TONE, GOOGLE_AD_KEYWORDS, GOOGLE_AD_CTA, GOOGLE_AD_URL, GOOGLE_AD_CONTENT):
    GOOGLE_AD = modelx.generate_content(f"""
Generate {VARIANT} Google Ads with a {TONE} tone
for a product/service described as {GOOGLE_AD_CONTENT}.
Use the keywords: {GOOGLE_AD_KEYWORDS},
include a call to action to {GOOGLE_AD_CTA},
and lead to this landing page: {GOOGLE_AD_URL}
""")
    return GOOGLE_AD.text

def SOCIAL_MEDIA_AD_GENERATOR(VARIANT, TONE, SOCIAL_MEDIA_AD_PLATFORM, SOCIAL_MEDIA_AD_FORMAT, SOCIAL_MEDIA_AD_CTA, SOCIAL_MEDIA_AD_TARGET, SOCIAL_MEDIA_AD_CONTENT):
    SOCIAL_MEDIA_AD = modelx.generate_content(f"""
Generate {VARIANT} social media ad copies with a {TONE} tone
for a {SOCIAL_MEDIA_AD_PLATFORM} {SOCIAL_MEDIA_AD_FORMAT} ad
targeting {SOCIAL_MEDIA_AD_TARGET}.
Product/Service Description: {SOCIAL_MEDIA_AD_CONTENT}
Call to Action: {SOCIAL_MEDIA_AD_CTA}
""")
    return SOCIAL_MEDIA_AD.text

def MARKETING_EMAIL_WRITER(VARIANT, TONE, EMAIL_WRITER_TYPE, EMAIL_WRITER_TARGET, EMAIL_WRITER_CTA, EMAIL_WRITER_CONTENT):
    MARKETING_EMAIL = modelx.generate_content(f"""
Write {VARIANT} marketing emails with a {TONE} tone
for a {EMAIL_WRITER_TYPE} targeting {EMAIL_WRITER_TARGET}.
Email Content: {EMAIL_WRITER_CONTENT}
Call to Action: {EMAIL_WRITER_CTA}
""")
    return MARKETING_EMAIL.text

def LINKEDIN_POST_GENERATOR(VARIANT, TONE, LINKEDIN_POST_TYPE, LINKEDIN_POST_TARGET, LINKEDIN_POST_CTA, LINKEDIN_POST_CONTENT):
    LINKEDIN_POST = modelx.generate_content(f"""
Generate {VARIANT} LinkedIn posts with a {TONE} tone
as a {LINKEDIN_POST_TYPE} targeting {LINKEDIN_POST_TARGET}.
Content/Idea/Keyword: {LINKEDIN_POST_CONTENT}
Call to Action: {LINKEDIN_POST_CTA}
""")
    return LINKEDIN_POST.text

def FACEBOOK_POST_GENERATOR(VARIANT, TONE, FACEBOOK_POST_TYPE, FACEBOOK_POST_TARGET, FACEBOOK_POST_CTA, FACEBOOK_POST_CONTENT):
    FACEBOOK_POST = modelx.generate_content(f"""
Generate {VARIANT} Facebook posts with a {TONE} tone
as a {FACEBOOK_POST_TYPE} targeting {FACEBOOK_POST_TARGET}.
Content/Idea/Keyword: {FACEBOOK_POST_CONTENT}
Call to Action: {FACEBOOK_POST_CTA}
""")
    return FACEBOOK_POST.text




# # # # # # # # # # # # # # # # # # # # # # # # JOB SEEKERS & PROFESSIONALS # # # # # # # # # # # # # # # # # # # # # # # #

def JOB_APPLICATION_WRITER(VARIANT, TONE, JOB_APPLICATION_JOB, JOB_APPLICATION_INDUSTRY, JOB_APPLICATION_EXPERIENCE, JOB_APPLICATION_TARGET, JOB_APPLICATION_REQUIREMENTS, JOB_APPLICATION_WORK_TEXT, JOB_APPLICATION_PERSONAL_TEXT, JOB_APPLICATION_SKILLS_TEXT, JOB_APPLICATION_EDUCATION_TEXT):
    JOB_APPLICATION = modelx.generate_content(f"""
Create {VARIANT} {TONE} resume and cover letter for a {JOB_APPLICATION_EXPERIENCE} {JOB_APPLICATION_JOB}
in the {JOB_APPLICATION_INDUSTRY} industry, applying to {JOB_APPLICATION_TARGET}.
The job requirements are: {JOB_APPLICATION_REQUIREMENTS}.
Here's some information about the candidate:
Work Experience: {JOB_APPLICATION_WORK_TEXT}
Skills and Expertise: {JOB_APPLICATION_SKILLS_TEXT}
Education: {JOB_APPLICATION_EDUCATION_TEXT}
Personal Interests: {JOB_APPLICATION_PERSONAL_TEXT}
""")
    return JOB_APPLICATION.text

def INTERVIEW_QUESTION_GENERATOR(VARIANT, TONE, INTERVIEW_NUMBER, INTERVIEW_JOB, INTERVIEW_DESCRIPTION, INTERVIEW_STAGE, INTERVIEW_CATEGORY):
    INTERVIEW_QUESTION = modelx.generate_content(f"""
Generate [{INTERVIEW_NUMBER}] interview questions for the position of [{INTERVIEW_JOB}] 
at the [{INTERVIEW_STAGE}] stage. 

[If job description is provided:]
Job Description:
{INTERVIEW_DESCRIPTION}

[If question categories are selected:]
Focus on these question categories: [{INTERVIEW_CATEGORY}]

Make the questions relevant, insightful, and appropriate for the interview stage.

Give {VARIANT} variations.
""")
    return INTERVIEW_QUESTION.text

def JOB_DESCRIPTION_GENERATOR(VARIANT, TONE, JOB_DESCRIPTION_JOB, JOB_DESCRIPTION_COMPANY, JOB_DESCRIPTION_INDUSTRY, JOB_DESCRIPTION_EXPERIENCE, JOB_DESCRIPTION_RESPONSIBILITIES):
    JOB_DESCRIPTION = modelx.generate_content(f"""
Generate job description for the position of [{JOB_DESCRIPTION_JOB}] at [{JOB_DESCRIPTION_COMPANY}] in the [{JOB_DESCRIPTION_INDUSTRY}] industry. 
The ideal candidate will have [{JOB_DESCRIPTION_EXPERIENCE}] years of experience.
Key responsibilities include: [{JOB_DESCRIPTION_RESPONSIBILITIES}]. 
The tone of voice should be: [{TONE}].
Give {VARIANT} variations.
""")
    return JOB_DESCRIPTION.text

def PROFESSIONAL_EMAIL_WRITER(VARIANT, TONE, PRO_EMAIL_TYPE, PRO_EMAIL_RECIPIENT, PRO_EMAIL_PURPOSE, PRO_EMAIL_INFO_TEXT):
    PROFESSIONAL_EMAIL = modelx.generate_content(f"""
Write a {VARIANT} {TONE} professional email of type '{PRO_EMAIL_TYPE}'
with the purpose of '{PRO_EMAIL_PURPOSE}'
to this recipient: '{PRO_EMAIL_RECIPIENT}'.
Additional information: {PRO_EMAIL_INFO_TEXT}
""")
    return PROFESSIONAL_EMAIL.text

def DOCUMENT_SUMMARIZER(VARIANT, TONE, DOC_SUMMARY_FILE, DOC_SUMMARY_LENGTH, DOC_SUMMARY_POINTS_TEXT):
    DOCUMENT_SUMMARY = modelx.generate_content(f"""
Generate {VARIANT} {DOC_SUMMARY_LENGTH} summary with a {TONE} tone
of the document '{DOC_SUMMARY_FILE}'.
Key points to include: {DOC_SUMMARY_POINTS_TEXT}
""")
    return DOCUMENT_SUMMARY.text

def MEETING_NOTES_SUMMARIZER(VARIANT, TONE, MEETING_SUMMARY_FILE, MEETING_SUMMARY_LENGTH, MEETING_SUMMARY_TOPIC):
    MEETING_NOTES = modelx.generate_content(f"""
Provide {VARIANT} {MEETING_SUMMARY_LENGTH} summary with a {TONE} tone
of the meeting notes in the file '{MEETING_SUMMARY_FILE}'
The main topic of the meeting was: {MEETING_SUMMARY_TOPIC}
""")
    return MEETING_NOTES.text

def COVER_LETTER_GENERATOR(VARIANT, TONE, COVER_LETTER_JOB, COVER_LETTER_COMPANY, COVER_LETTER_SKILLS, COVER_LETTER_EXPERIENCE):
    COVER_LETTER = modelx.generate_content(f"""
Write {VARIANT} {TONE} cover letter for the position of {COVER_LETTER_JOB} at {COVER_LETTER_COMPANY}.
The candidate's skills and qualifications include: {COVER_LETTER_SKILLS}
The candidate's relevant experience includes: {COVER_LETTER_EXPERIENCE}
""")
    return COVER_LETTER.text

def BUSINESS_PITCH_GENERATOR(VARIANT, TONE, PITCH_FORMAT, PITCH_BUSINESS, PITCH_PROBLEM, PITCH_SOLUTION, PITCH_TARGET):
    BUSINESS_PITCH = modelx.generate_content(f"""
Generate a [{PITCH_FORMAT}] for a [{PITCH_BUSINESS}] that targets [{PITCH_TARGET}].

Problem: [{PITCH_PROBLEM}]
Solution: [{PITCH_SOLUTION}]

The tone of the pitch should be [{TONE}].

Give {VARIANT} variations.
""")
    return BUSINESS_PITCH.text

def MEETING_AGENDA_GENERATOR(VARIANT, TONE, MEETING_AGENDA_TOPIC, MEETING_AGENDA_PURPOSE, MEETING_AGENDA_ATTENDEES, MEETING_AGENDA_POINTS, MEETING_AGENDA_TIME, MEETING_AGENDA_ACTION):
    MEETING_AGENDA = modelx.generate_content(f"""
Generate {VARIANT} meeting agenda with a {TONE} tone :
Meeting Topic: {MEETING_AGENDA_TOPIC}
Purpose: {MEETING_AGENDA_PURPOSE}
Attendees: {MEETING_AGENDA_ATTENDEES}
Discussion Points: {MEETING_AGENDA_POINTS}
Time Allocation: {MEETING_AGENDA_TIME}
Action Items: {MEETING_AGENDA_ACTION}
""")
    return MEETING_AGENDA.text




# # # # # # # # # # # # # # # # # # # # # # # # SEO PROFESSIONALS # # # # # # # # # # # # # # # # # # # # # # # #

def SEO_CONTENT_WRITER(VARIANT, TONE, SEO_CONTENT_TYPES, SEO_CONTENT_LENGTH, SEO_CONTENT_TARGET, SEO_CONTENT_KEYWORDS):
    SEO_CONTENT = modelx.generate_content(f"""
Write {VARIANT} SEO-optimized pieces of content with a {TONE} tone
for a {SEO_CONTENT_TYPES} targeting {SEO_CONTENT_TARGET}.
The content should be {SEO_CONTENT_LENGTH} and focus on the keyword '{SEO_CONTENT_KEYWORDS}'.
""")
    return SEO_CONTENT.text

def KEYWORD_EXTRACTOR(VARIANT, TONE, KEYWORD_EXTRACT_CONTENT, KEYWORD_EXTRACT_COUNT, KEYWORD_EXTRACT_TYPE):
    KEYWORD_EXTRACTED = modelx.generate_content(f"""
Extract {KEYWORD_EXTRACT_COUNT} {KEYWORD_EXTRACT_TYPE} keywords from this text: \n\n{KEYWORD_EXTRACT_CONTENT}

Give {VARIANT} variations.
""")
    return KEYWORD_EXTRACTED.text

def KEYWORD_GENERATOR(VARIANT, TONE, KEYWORD_GENERATOR_TARGET, KEYWORD_GENERATOR_COUNT, KEYWORD_GENERATOR_TYPE, KEYWORD_GENERATOR_SEED):
    KEYWORD_GENERATED = modelx.generate_content(f"""
Generate {KEYWORD_GENERATOR_COUNT} {KEYWORD_GENERATOR_TYPE} keywords relevant to {KEYWORD_GENERATOR_TARGET}
using '{KEYWORD_GENERATOR_SEED}' as a seed keyword.

Give {VARIANT} variations with {TONE} tone.
""")
    return KEYWORD_GENERATED.text

def META_TITLE_GENERATOR(VARIANT, TONE, META_TITLE_PAGE, META_TITLE_KEYWORDS, META_TITLE_LIMIT):
    META_TITLE = modelx.generate_content(f"""
Generate {VARIANT} meta titles with a {TONE} tone
for a page titled '{META_TITLE_PAGE}', using the keyword '{META_TITLE_KEYWORDS}'
and keeping it under {META_TITLE_LIMIT} characters.
""")
    return META_TITLE.text

def META_DESCRIPTION_GENERATOR(VARIANT, TONE, META_DESCRIPTION_PAGE, META_DESCRIPTION_KEYWORDS, META_DESCRIPTION_LIMIT, META_DESCRIPTION_CONTENT):
    META_DESCRIPTION = modelx.generate_content(f"""
Generate {VARIANT} meta descriptions with a {TONE} tone
for a page titled '{META_DESCRIPTION_PAGE}' with the following content:\n\n{META_DESCRIPTION_CONTENT} \n\n
Use the keyword '{META_DESCRIPTION_KEYWORDS}' and keep it under {META_DESCRIPTION_LIMIT} characters.
""")
    return META_DESCRIPTION.text

def WEBSITE_COPYWRITER(VARIANT, TONE, WEBSITE_COPY_TYPE, WEBSITE_COPY_TARGET, WEBSITE_COPY_CONTENT):  
    WEBSITE_COPY = modelx.generate_content(f"""
Write {VARIANT} website copy variations with a {TONE} tone "
for a {WEBSITE_COPY_TYPE} page targeting {WEBSITE_COPY_TARGET}. "
The primary call to action on this page is {WEBSITE_COPY_TYPE}. "
Highlight these points:\n\n{WEBSITE_COPY_CONTENT}
""")
    return WEBSITE_COPY.text

def PRODUCT_DESCRIPTION_GENERATOR(VARIANT, TONE, PRODUCT_DESCRIPTION_NAME, PRODUCT_DESCRIPTION_CATEGORY, PRODUCT_DESCRIPTION_FEATURES, PRODUCT_DESCRIPTION_TARGET):
    PRODUCT_DESCRIPTION = modelx.generate_content(f"""
Generate {VARIANT} compelling product description for a [{PRODUCT_DESCRIPTION_NAME}], 
which is a [{PRODUCT_DESCRIPTION_CATEGORY}] with a {TONE} tone. 

Key features/benefits: 
[{PRODUCT_DESCRIPTION_FEATURES}] 

Target audience: [{PRODUCT_DESCRIPTION_TARGET}]

Use a [{TONE}] tone of voice.  
Focus on highlighting the benefits of the features for the target audience.
""")
    return PRODUCT_DESCRIPTION.text




# # # # # # # # # # # # # # # # # # # # # # # # EDUCATORS & STUDENTS # # # # # # # # # # # # # # # # # # # # # # # #

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




# # # # # # # # # # # # # # # # # # # # # # # # PERSONAL USE & CREATIVITY # # # # # # # # # # # # # # # # # # # # # # # #

def SONG_LYRICS_GENERATOR(VARIANT, TONE, SONG_GENRE, SONG_THEME, SONG_KEYWORDS):
    SONG_LYRICS = modelx.generate_content(f"""
Generate {VARIANT} song lyrics with a {TONE} tone
in the genre of {SONG_GENRE} about the theme of {SONG_THEME},
incorporating these keywords: {SONG_KEYWORDS}.
""")
    return SONG_LYRICS.text

def POEM_GENERATOR(VARIANT, TONE, POEM_TYPE, POEM_THEME, POEM_KEYWORDS):
    POEM = modelx.generate_content(f"""
Write {VARIANT} poems with a {TONE} tone "
in the style of {POEM_TYPE} about {POEM_THEME}, "
using these keywords: {POEM_KEYWORDS}.
""")
    return POEM.text

def STORY_GENERATOR(VARIANT, TONE, STORY_GENRE, STORY_THEME, STORY_SETTING, STORY_CHARACTERS, STORY_PLOT):
    STORY = modelx.generate_content(f"""
Write {VARIANT} short stories with a {TONE} tone
in the genre of {STORY_GENRE} with a {STORY_THEME} theme.
The story should be set in a {STORY_SETTING} and feature these characters: {STORY_CHARACTERS}.
The plot should revolve around these key points: {STORY_PLOT}.
""")
    return STORY.text

def PERSONALIZED_RECIPE_GENERATOR(VARIANT, TONE, RECIPE_CUISINE, RECIPE_RESTRICTION, RECIPE_LEVEL, RECIPE_INGREDIENTS):
    PERSONALIZED_RECIPE = modelx.generate_content(f"""
Generate {VARIANT} {RECIPE_LEVEL} recipes with a {TONE} tone
featuring {RECIPE_INGREDIENTS} from {RECIPE_CUISINE} cuisine,
suitable for {RECIPE_RESTRICTION} diets.
""")
    return PERSONALIZED_RECIPE.text

def RECIPE_GENERATOR(VARIANT, TONE, QUICK_RECIPE_CUISINE, QUICK_RECIPE_TYPE, QUICK_RECIPE_INGREDIENTS):
    RECIPE = modelx.generate_content(f"""
Generate {VARIANT} {QUICK_RECIPE_TYPE} recipes with a {TONE} tone
from {QUICK_RECIPE_CUISINE} cuisine using only these ingredients: {QUICK_RECIPE_INGREDIENTS}.
""")
    return RECIPE.text

def PERSONALIZED_EMAIL_GENERATOR(VARIANT, TONE, PERSONALIZED_EMAIL_CONTENT, PERSONALIZED_EMAIL_TYPE, PERSONALIZED_EMAIL_RECIPIENT, PERSONALIZED_EMAIL_EXTRA_CONTENT):  
    PERSONALIZED_EMAIL = modelx.generate_content(f"""
Write {VARIANT} personalized emails with a {TONE} tone
for a {PERSONALIZED_EMAIL_TYPE} to {PERSONALIZED_EMAIL_RECIPIENT}.
Email Content: {PERSONALIZED_EMAIL_CONTENT} "
Additional Information: {PERSONALIZED_EMAIL_EXTRA_CONTENT}
""")
    return PERSONALIZED_EMAIL.text




# # # # # # # # # # # # # # # # # # # # # # # # CODING & TECHNICAL TOOLS # # # # # # # # # # # # # # # # # # # # # # # #

def CODE_GENERATOR(VARIANT, TONE, CODE_INSTRUCTION, CODE_LANGUAGE, CODE_EXAMPLE_TEXT):
    CODE = modelx.generate_content(f"""
Generate {VARIANT} code snippets with a {TONE} tone in the language [{CODE_LANGUAGE}]
that fulfills the following task: '{CODE_INSTRUCTION}'.
Include a code example like this: {CODE_EXAMPLE_TEXT} 
""")
    return CODE.text

def TECHNICAL_DOCUMENTATION_WRITER(VARIANT, TONE, DOCUMENTATION_TYPE, DOCUMENTATION_LEVEL, DOCUMENTATION_CONTENT):
    DOCUMENTATION = modelx.generate_content(f"""
Generate {VARIANT} technical documentation pieces with a {TONE} tone
for a {DOCUMENTATION_TYPE} aimed at a {DOCUMENTATION_LEVEL} audience.
Use these code snippets as reference: {DOCUMENTATION_CONTENT}
""")
    return DOCUMENTATION.text




# # # # # # # # # # # # # # # # # # # # # # # # ADDITIONALS TOOLS # # # # # # # # # # # # # # # # # # # # # # # #

def GRAMMAR_CHECKER(VARIANT, TONE, GRAMMAR_CONTENT, GRAMMAR_LEVEL):
    GRAMMAR = modelx.generate_content(f"""
Proofread and improve the following text, {GRAMMAR_CONTENT},
providing a {GRAMMAR_LEVEL} level of feedback.

Give {VARIANT} variations.
""")
    return GRAMMAR.text

def SENTENCE_REWORDER(VARIANT, TONE, REWORD_CONTENT):
    REWORD = modelx.generate_content(f"""
Generate {VARIANT} variations of this sentence, rephrased with a {TONE} tone: {REWORD_CONTENT}
""")
    return REWORD.text

def TEXT_INFLATOR(VARIANT, TONE, INFLATOR_CONTENT, INFLATOR_LEVEL):
    INFLATE = modelx.generate_content(f"""
Expand the following text with a {TONE} tone, using a {INFLATOR_LEVEL} inflation level:\n{INFLATOR_CONTENT}.

Give {VARIANT} variations.
""")
    return INFLATE.text

def SENTENCE_SHORTENER(VARIANT, TONE, SHORTENER_CONTENT, SHORTENER_LEVEL):
    SHORTENED = modelx.generate_content(f"""
Shorten the following text using this shortening style: {SHORTENER_LEVEL}\n{SHORTENER_CONTENT}.

Give {VARIANT} variations with a {TONE} tone.
""")
    return SHORTENED.text

def SUMMARIZER(VARIANT, TONE, SUMMARY_CONTENT, SUMMARY_LENGTH):
    SUMMARY = modelx.generate_content(f"""
Summarize the following text with a {TONE} tone, aiming for a {SUMMARY_LENGTH} summary:\n{SUMMARY_CONTENT}.

Give {VARIANT} variations.
""")
    return SUMMARY.text

def TRANSLATOR(VARIANT, TONE, TRANSLATOR_CONTENT, TRANSLATOR_LANGUAGE):  
    TRANSLATED = modelx.generate_content(f"""
Translate the following text into {TRANSLATOR_LANGUAGE}:\n{TRANSLATOR_CONTENT}.

Give {VARIANT} variations with a {TONE} tone.
""")
    return TRANSLATED.text