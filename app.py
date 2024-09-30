import streamlit as st
import mysql.connector
from datetime import date, timedelta
import google.generativeai as genai
from pypdf import PdfReader
from generative_functions import (BLOG_POST_IDEA_GENERATOR, BLOG_POST_GENERATOR, NEWS_ARTICLE_WRITER, CREATIVE_WRITING_PROMPT,
                                  VIDEO_SCRIPT_WRITER, VIDEO_DESCRIPTION_WRITER, HASHTAG_GENERATOR, CONTENT_PROMOTION_GENERATOR,
                                  AD_COPYWRITER, CALL_TO_ACTION_GENERATOR, AIDA_COPYWRITER, PAS_COPYWRITER, GOOGLE_AD_GENERATOR,
                                  SOCIAL_MEDIA_AD_GENERATOR, MARKETING_EMAIL_WRITER, LINKEDIN_POST_GENERATOR, FACEBOOK_POST_GENERATOR,
                                  JOB_APPLICATION_WRITER, INTERVIEW_QUESTION_GENERATOR, JOB_DESCRIPTION_GENERATOR, PROFESSIONAL_EMAIL_WRITER,
                                  DOCUMENT_SUMMARIZER, MEETING_NOTES_SUMMARIZER, COVER_LETTER_GENERATOR, BUSINESS_PITCH_GENERATOR,
                                  MEETING_AGENDA_GENERATOR, SEO_CONTENT_WRITER, KEYWORD_EXTRACTOR, KEYWORD_GENERATOR, META_TITLE_GENERATOR,
                                  META_DESCRIPTION_GENERATOR, WEBSITE_COPYWRITER, PRODUCT_DESCRIPTION_GENERATOR, RESEARCH_PAPER_SUMMARIZER,
                                  CHAPTER_EXPLAINER, QUESTION_PAPER_GENERATION, STUDY_GUIDE_CREATOR, SONG_LYRICS_GENERATOR, POEM_GENERATOR,
                                  STORY_GENERATOR, PERSONALIZED_RECIPE_GENERATOR, RECIPE_GENERATOR, PERSONALIZED_EMAIL_GENERATOR, CODE_GENERATOR,
                                  TECHNICAL_DOCUMENTATION_WRITER, GRAMMAR_CHECKER, SENTENCE_REWORDER, TEXT_INFLATOR, SENTENCE_SHORTENER,
                                  SUMMARIZER, TRANSLATOR) 
from users import USERS

st.set_page_config(page_title="CosmoPen", page_icon=None, layout="wide", initial_sidebar_state="collapsed", menu_items=None)

def login_page():
    st.title("Welcome to CosmoPen")
    with st.container(border=True):
        USER = st.text_input("Please Enter Pilot Id:")
        if st.button("Login"):
            if USER in USERS:
                st.session_state.user = USER  # Store name in session state
                st.session_state.page = "two"
def dashboard():
    if "user" in st.session_state:
        USER = st.session_state.user
        CREDIT = USERS.get(USER)
    else:
        st.write("USER not found. Please go back to Page One.")

    return USER, CREDIT



TONES_TIER1 = [
        "Clear", "Concise", "Confident", "Direct", "Enthusiastic",
        "Formal", "Friendly", "Helpful", "Informative", "Motivational",
        "Appreciative", "Casual", "Creative", "Curious", "Empathetic", 
        "Funny", "Inspirational", "Passionate", "Persuasive", "Professional", 
        "Urgent", "Serious", "Apologetic", "Excited", "Grateful" 
    ]
LANGUAGES_FOR_TRANSLATION = [
    'English', 'French', 'German', 'Spanish',
    'Italian', 'Portuguese', 'Dutch', 'Swedish',
    'Norwegian', 'Danish', 'Arabic', 'Chinese (Simplified)',
    'Chinese (Traditional)', 'Japanese', 'Korean', 'Russian',
    'Hindi', 'Finnish', 'Polish', 'Romanian',
    'Turkish', 'Ukrainian', 'Hungarian', 'Czech',
    'Slovak', 'Bulgarian', 'Greek', 'Persian',
    'Hebrew', 'Vietnamese', 'Thai', 'Indonesian',
    'Malay', 'Filipino', 'Afrikaans', 'Albanian',
    'Amharic', 'Armenian', 'Azerbaijani', 'Bengali',
    'Catalan', 'Croatian', 'Estonian', 'Gujarati',
    'Icelandic', 'Kannada', 'Latvian', 'Lithuanian',
    'Macedonian', 'Malayalam', 'Marathi', 'Serbian',
    'Slovenian', 'Swahili', 'Tamil', 'Telugu', 'Urdu'
]
LANGUAGES_FOR_CODE = [
    'Python', 'R', 'C#',
    'C++', 'Java', 'HTML',
    'CSS', 'JavaScript', 'SQL',
    'Swift', 'Go', 'Kotlin',
    'Ruby', 'PHP'
]

GOOGLE_API_KEY = 'AIzaSyDmF4D2f_ibz6UZi_sFZyydkSmUrz7x8_k'
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.0-pro')
modelx = genai.GenerativeModel('gemini-1.5-flash')

OUTPUT = """"""
VALID = False

# --- App Flow Control ---
if "page" not in st.session_state:
    st.session_state.page = "one"  # Default to page one

if st.session_state.page == "one":
    login_page()
elif st.session_state.page == "two":
    USER, CREDIT = dashboard()
    HERO_COL1, HERO_COL2, HERO_COL3, HERO_COL4 = st.columns(4)

    with HERO_COL1:
        with st.popover("**Account Settings**", use_container_width=True):
            st.subheader(USER)
            st.write(f"Remaining Credit: {CREDIT}")


    with HERO_COL2:
        with st.popover("**AI Generator Mode**", help="Note: Selecting the mode will reset the content.", use_container_width=True):
            MODE_SELECTION = st.radio(
            "**Generate for**",
            ["**Content Creator & Influencer**", "**Marketing & Advertising Specialists**", "**Job Seekers & Professionals**", "**SEO Professionals**",
            "**Students & Educators**", "**Personal Use & Creativity**", "**Coding & Technical Tools**", "**Additional Tools**"],
            captions=[
                "Create and write blogs, articles, video descriptions and more.",
                "Write high-quality ad copies, marketing posts, and more.",
                "Write job applications, resumes, cover letters and more.",
                "Generate high-quality SEO content.",
                "Create and get lesson summaries, question papers and more.",
                "Generate creative content for personal use.",
                "Get accurate code snippets and technical documentation.",
                "Extra tools for even more tasks.",
            ],
        )
    with HERO_COL4:
        if MODE_SELECTION == "**Content Creator & Influencer**":

            with st.popover(f"**Generative Task**", help="Note: Selecting the mode will reset the content.", use_container_width=True):
                SELECTION = st.radio(
                "**Generation Type**",
                ["**Blog Post Idea Generator**", "**Blog Post Writer**", "**News Article Writer**", "**Creative Writing Prompts**",
                "**Video Script Writer**", "**Video Description Writer**", "**Hashtag Generator**"],
                captions=[
                    "Spark new ideas for your next blog post.",
                    "Write high-quality content with ease.",
                    "Create compelling news stories.",
                    "Fuel your imagination with fresh writing prompts.",
                    "Craft compelling video scripts that captivate your audience.",
                    "Optimize your video descriptions for search engines.",
                    "Find relevant hashtags to increase your reach."
                ],
            )
                
        if MODE_SELECTION == "**Marketing & Advertising Specialists**":
            
            with st.popover(f"**Generative Task**", help="Note: Selecting the mode will reset the content.", use_container_width=True):
                SELECTION = st.radio(
                "**Generation Type**",
                ["**Content Promotion Posts**", "**Ad Copywriter**", "**Call to Action Generator**", "**AIDA Copywriter**",
                "**PAS Copywriter**", "**Google Ads Generator**", "**Social Media Ads Generator**", "**Marketing Email Writer**",
                "**LinkedIn Post Generator**", "**Facebook Post Generator**"],
                captions=[
                    "Write compelling posts to promote your content and drive engagement.",
                    "Craft persuasive ad copy that converts visitors into customers.",
                    "Create strong calls to action that encourage visitors to take the desired action.",
                    "Generate ad copy that follows the Attention, Interest, Desire, Action (AIDA) framework.",
                    "Write copy using the Problem, Agitate, Solution (PAS) formula to highlight benefits.",
                    "Create effective Google Ads campaigns tailored to your business goals.",
                    "Design engaging social media ads for platforms like Facebook, Instagram, and Twitter.",
                    "Compose personalized marketing emails that nurture leads and drive sales.",
                    "Generate engaging LinkedIn posts to build your professional network and showcase expertise.",
                    "Create attention-grabbing Facebook posts to reach your target audience and increase engagement."
                ],
            )
        
        if MODE_SELECTION == "**Job Seekers & Professionals**":
            with st.popover(f"**Generative Task**", help="Note: Selecting the mode will reset the content.", use_container_width=True):
                SELECTION = st.radio(
                "**Generation Type**",
                ["**Job application writer (resume & cover letter)**", "**Interview question generator**", "**Job description generator**", "**Professional email writer**",
                "**Document summarizer**", "**Meeting notes summarizer**", "**Cover letter generator**", "**Business pitch generator**", "**Meeting agenda generator**"],
                captions=[
                    "Tailor your application to any job.",
                    "Prepare for your interview with realistic questions.",
                    "Attract top talent with effective job postings.",
                    "Compose professional emails with ease.",
                    "Quickly summarize any document.",
                    "Capture key points from your meetings.",
                    "Craft a personalized cover letter for every job.",
                    "Convince investors with a compelling pitch.",
                    "Plan effective meetings with ease."
                ],
            )
        
        if MODE_SELECTION == "**SEO Professionals**":
            with st.popover(f"**Generative Task**", help="Note: Selecting the mode will reset the content.", use_container_width=True):
                SELECTION = st.radio(
                "**Generation Type**",
                ["**SEO content writer**", "**Keyword extractor**", "**AI keyword generator**", "**Meta title generator**",
                "**Meta description generator**", "**Website copywriter**", "**Product description generator**"],
                captions=[
                    "Create optimized content that ranks higher in search engines.",
                    "Identify relevant keywords for your content.",
                    "Discover new keywords to target.",
                    "Craft compelling meta titles for your pages.",
                    "Write persuasive meta descriptions that entice clicks.",
                    "Write engaging copy that converts visitors into customers.",
                    "Create persuasive product descriptions that sell."
                ],
            )
        
        if MODE_SELECTION == "**Students & Educators**":
            with st.popover(f"**Generative Task**", help="Note: Selecting the mode will reset the content.", use_container_width=True):
                SELECTION = st.radio(
                "**Generation Type**",
                ["**Research Paper Summarizer**", "**Lesson Explainer**",
                "**Question Paper Generator**", "**Study Guide Creator**"],
                captions=[
                    ":blue[Quickly grasp the key points of any research paper.]",
                    ":blue[Break down complex concepts into easy-to-understand explanations.]",
                    ":blue[Create personalized practice exams.]",
                    ":blue[Organize your studies and improve your learning.]"
                ],
            )
            
        
        if MODE_SELECTION == "**Personal Use & Creativity**":
            with st.popover(f"**Generative Task**", help="Note: Selecting the mode will reset the content.", use_container_width=True):
                SELECTION = st.radio(
                "**Generation Type**",
                ["**Song Lyrics Generator**", "**Poem Generator**", "**Story Generator**",
                "**Personalized Recipe Generator**", "**Recipe from Ingredients**", "**Personalized Email Writer**"],
                captions=[
                    "Write catchy and original song lyrics.",
                    "Compose beautiful and moving poems.",
                    "Create exciting and imaginative stories.",
                    "Discover delicious new recipes tailored to your tastes.",
                    "Create delicious meals with the ingredients you have.",
                    "Craft emails that resonate with your needs."
                ],
            )
            
        if MODE_SELECTION == "**Coding & Technical Tools**":
            with st.popover(f"**Generative Task**", help="Note: Selecting the mode will reset the content.", use_container_width=True):
                SELECTION = st.radio(
                "**Generation Type**",
                ["**Code Generator**", "**Technical Documentation Writer**"],
                captions=[
                    "Generate code snippets with ease.",
                    "Create clear and comprehensive documentation."
                ],
            )
        
        if MODE_SELECTION == "**Additional Tools**":
            with st.popover(f"**Generative Task**", help="Note: Selecting the mode will reset the content.", use_container_width=True):
                SELECTION = st.radio(
                "**Generation Type**",
                ["**Grammar Checker & Improver**", "**Sentence Reworder**", "**Text Inflator**",
                "**Sentence Shortener**", "**Summarizer**", "**Translator**"],
                captions=[
                    "Write with confidence and clarity.",
                    "Rephrase your sentences for better impact.",
                    "Add more details and depth to your writing.",
                    "Simplify your writing without losing meaning.",
                    "Quickly grasp the key points of any text.",
                    "Translate text into multiple languages accurately."
                ],
            )

    






    if MODE_SELECTION == "**Content Creator & Influencer**":
        DASH_COL1, DASH_COL2 = st.columns(2, gap="medium")

        with DASH_COL1:

            # # # # # V A R I E N T S / T O N E S # # # # #

            HEAD_COL1, HEAD_COL2 = st.columns(2)
            with HEAD_COL1:
                VARIANT = st.selectbox("Variants", options=("1 varient", "2 varients", "3 varients"), key="varient1")
            with HEAD_COL2:
                TONE = st.selectbox("Select Tone / Voice", options=TONES_TIER1, key="tone1")

            # # # # # S E L E C T I O N # # # # #

            with st.container(border=False, height=350):

                # # # # # M O D E 1 # # # # #

                if SELECTION == "**Blog Post Idea Generator**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        BLOG_IDEA_TARGET = st.selectbox("Target Audience", options=("Angel Investors", "Venture Capitalists", "Crowdfunding Platform", "Others (Specify)"), key="target1")
                    with SMOL2:
                        BLOG_IDEA_NICHE = st.selectbox("Blog Niche", options=("Angel Investors", "Venture Capitalists", "Crowdfunding Platform", "Others (Specify)"))
                    with SMOL3:
                        BLOG_IDEA_LENGTH = st.selectbox("Desired Length", options=("Short", "Medium", "Long"), key="length1")
                    SMOL4, SMOL5 = st.columns(2)
                    with SMOL4:
                        BLOG_IDEA_KEYWORDS = st.text_input("Keywords", key="keywords1")
                    with SMOL5:
                        BLOG_IDEA_CTA = st.selectbox("Call to Action", options=("Angel Investors", "Venture Capitalists", "Crowdfunding Platform", "Others (Specify)"), key="cta1")

                    if BLOG_IDEA_TARGET and BLOG_IDEA_NICHE and BLOG_IDEA_LENGTH and BLOG_IDEA_KEYWORDS and BLOG_IDEA_CTA:
                        VALID = True

                # # # # # M O D E 2 # # # # #

                if SELECTION == "**Blog Post Writer**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        BLOG_POST_TOPIC = st.text_input("Topic", key="topic2")
                    with SMOL2:
                        BLOG_POST_TARGET = st.selectbox("Target Audience", options=("Angel Investors", "Venture Capitalists", "Crowdfunding Platform", "Others (Specify)"), key="target2")
                    with SMOL3:
                        BLOG_POST_LENGTH = st.selectbox("Desired Length", options=("Short", "Medium", "Long"), key="length2")
                    BLOG_POST_CONTENT = st.text_area("Content Outline", key="content2")

                    if BLOG_POST_TOPIC and BLOG_POST_TARGET and BLOG_POST_LENGTH and BLOG_POST_CONTENT:
                        VALID = True

                # # # # # M O D E 3 # # # # #

                if SELECTION == "**News Article Writer**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        NEWS_ARTICLE_NICHE = st.text_input("Title for Job Description")
                    with SMOL2:
                        NEWS_ARTICLE_TARGET = st.selectbox("Target Audience", options=("Angel Investors", "Venture Capitalists", "Crowdfunding Platform", "Others (Specify)"), key="target3")
                    with SMOL3:
                        NEWS_ARTICLE_LENGTH = st.selectbox("Desired Length", options=("Short", "Medium", "Long"), key="length3")
                    SMOL4, SMOL5 = st.columns(2)
                    with SMOL4:
                        NEWS_ARTICLE_CONTENT = st.text_area("Content Outline", key="content3")
                    with SMOL5:
                        NEWS_ARTICLE_DATE = st.text_input("Article Date", key="date3")

                    if NEWS_ARTICLE_NICHE and NEWS_ARTICLE_TARGET and NEWS_ARTICLE_LENGTH and NEWS_ARTICLE_CONTENT and NEWS_ARTICLE_DATE:
                        VALID = True

                # # # # # M O D E 4 # # # # #

                if SELECTION == "**Creative Writing Prompts**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        CREATIVE_WRITING_GENRE = st.selectbox("Genre", options=("Fantasy", "Science fiction", "Romance", "Mystery", "Thriller"), key="genre4")
                    with SMOL2:
                        CREATIVE_WRITING_SETTING = st.selectbox("Setting", options=("Medieval kingdom", "Post-apocalyptic world", "Space station", "Haunted house"))
                    with SMOL3:
                        CREATIVE_WRITING_THEME = st.selectbox("Theme", options=("Love and loss", "Good vs. evil", "Hope and despair", "The power of choice"))
                    SMOL4, SMOL5, SMOL6 = st.columns(3)
                    with SMOL4:
                        CREATIVE_WRITING_TYPE = st.selectbox("Writing Type", options=("Short story", "Novel excerpt", "Poem"))
                    with SMOL5:
                        CREATIVE_WRITING_UNIQUE = st.selectbox("Unique Concept", options=("Artificial intelligence with consciousness", "Parallel universes", "Magical creatures", "Others (Specify)"))
                    with SMOL6:
                        if CREATIVE_WRITING_UNIQUE == "Others (Specify)":
                            CREATIVE_WRITING_UNIQUE = st.text_input("Specify")
                    if CREATIVE_WRITING_GENRE and CREATIVE_WRITING_SETTING and CREATIVE_WRITING_THEME and CREATIVE_WRITING_TYPE and CREATIVE_WRITING_UNIQUE:
                        VALID = True

                # # # # # M O D E 5 # # # # #

                if SELECTION == "**Video Script Writer**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        VIDEO_SCRIPT_TYPE = st.selectbox("Video Type", options=("Explainer video", "Product demo", "Testimonial", "Documentary", "Others (Specify)"))
                    with SMOL2:
                        VIDEO_SCRIPT_TARGET = st.selectbox("Target Audience", options=("Consumers", "Businesses", "Students", "General audience"), key="target5")
                    with SMOL3:
                        VIDEO_SCRIPT_CTA = st.selectbox("Call to Action", options=("Visit our website", "Download our app", "Subscribe to our channel"), key="cta5")
                    SMOL4, SMOL5 = st.columns(2)
                    with SMOL4:
                        VIDEO_SCRIPT_KEYWORDS = st.text_input("Keywords", key="keywords5")
                    with SMOL5:
                        VIDEO_SCRIPT_LENGTH = st.selectbox("Call to Action", options=("Short (30-60 seconds)", "Medium (1-3 minutes)", "Long (5+ minutes)"), key="length5")
                    
                    if VIDEO_SCRIPT_TYPE and VIDEO_SCRIPT_TARGET and VIDEO_SCRIPT_CTA and VIDEO_SCRIPT_KEYWORDS and VIDEO_SCRIPT_LENGTH:
                        VALID = True

                # # # # # M O D E 6 # # # # #

                if SELECTION == "**Video Description Writer**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        VIDEO_DESCRIPTION_TITLE = st.text_input("Video Title")
                    with SMOL2:
                        VIDEO_DESCRIPTION_TARGET = st.selectbox("Target Audience", options=("Consumers", "Businesses", "Students", "General audience"), key="target6")
                    with SMOL3:
                        VIDEO_DESCRIPTION_TYPE = st.selectbox("Video Type", options=("Gameplay", "Tutorial", "Vlog", "Review"))
                    SMOL4, SMOL5, SMOL6 = st.columns(3)
                    with SMOL4:
                        VIDEO_DESCRIPTION_KEYWORDS = st.text_input("Keywords", key="keywords6")
                    with SMOL5:
                        VIDEO_DESCRIPTION_CTA = st.selectbox("Call to Action", options=("Visit our website", "Download our app", "Subscribe to our channel"), key="cta6")
                    with SMOL6:
                        VIDEO_DESCRIPTION_CONTENT = st.text_area("Video Content")

                    if VIDEO_DESCRIPTION_TITLE and VIDEO_DESCRIPTION_TARGET and VIDEO_DESCRIPTION_TYPE and VIDEO_DESCRIPTION_KEYWORDS and VIDEO_DESCRIPTION_CTA and VIDEO_DESCRIPTION_CONTENT:
                        VALID = True

                # # # # # M O D E 7 # # # # #

                if SELECTION == "**Hashtag Generator**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        HASHTAG_TOPIC = st.selectbox("Topic", options=("Artificial intelligence", "Fashion", "Travel", "Food"))
                    with SMOL2:
                        HASHTAG_NAME = st.text_input("BrandName / ProductName")
                    with SMOL3:
                        HASHTAG_TARGET = st.selectbox("Target Audience", options=("Tech enthusiasts", "Fashion lovers", "Travel bloggers"), key="target8")
                    HASHTAG_KEYWORDS = st.text_input("Keywords", key="keywords8")

                    if HASHTAG_TOPIC and HASHTAG_NAME and HASHTAG_TARGET and HASHTAG_KEYWORDS:
                        VALID = True


            GENERATE = st.button("Generate", use_container_width=True, type="primary", key="button1")


        with DASH_COL2:
            container = st.container(border=True, height=500)
            if not GENERATE:
                container.write("**Generated content will be displayed here**")
            if GENERATE:
                if SELECTION == "**Blog Post Idea Generator**":
                    container.write(BLOG_POST_IDEA_GENERATOR(VARIANT, TONE, BLOG_IDEA_TARGET, BLOG_IDEA_NICHE, BLOG_IDEA_LENGTH, BLOG_IDEA_KEYWORDS, BLOG_IDEA_CTA))
                if SELECTION == "**Blog Post Writer**":
                    container.write(BLOG_POST_GENERATOR(VARIANT, TONE, BLOG_POST_TOPIC, BLOG_POST_TARGET, BLOG_POST_LENGTH, BLOG_POST_CONTENT))
                if SELECTION == "**News Article Writer**":
                    container.write(NEWS_ARTICLE_WRITER(VARIANT, TONE, NEWS_ARTICLE_NICHE, NEWS_ARTICLE_TARGET, NEWS_ARTICLE_LENGTH, NEWS_ARTICLE_CONTENT, NEWS_ARTICLE_DATE))
                if SELECTION == "**Creative Writing Prompts**":
                    container.write(CREATIVE_WRITING_PROMPT(VARIANT, TONE, CREATIVE_WRITING_GENRE, CREATIVE_WRITING_SETTING, CREATIVE_WRITING_THEME, CREATIVE_WRITING_TYPE, CREATIVE_WRITING_UNIQUE))
                if SELECTION == "**Video Script Writer**":
                    container.write(VIDEO_SCRIPT_WRITER(VARIANT, TONE, VIDEO_SCRIPT_TYPE, VIDEO_SCRIPT_TARGET, VIDEO_SCRIPT_CTA, VIDEO_SCRIPT_KEYWORDS, VIDEO_SCRIPT_LENGTH))
                if SELECTION == "**Video Description Writer**":
                    container.write(VIDEO_DESCRIPTION_WRITER(VARIANT, TONE, VIDEO_DESCRIPTION_TITLE, VIDEO_DESCRIPTION_TARGET, VIDEO_DESCRIPTION_TYPE, VIDEO_DESCRIPTION_KEYWORDS, VIDEO_DESCRIPTION_CTA, VIDEO_DESCRIPTION_CONTENT))
                if SELECTION == "**Hashtag Generator**":
                    container.write(HASHTAG_GENERATOR(VARIANT, TONE, HASHTAG_TOPIC, HASHTAG_NAME, HASHTAG_TARGET, HASHTAG_KEYWORDS))



    if MODE_SELECTION == "**Marketing & Advertising Specialists**":
        DASH_COL1, DASH_COL2 = st.columns(2, gap="medium")

        with DASH_COL1:

            # # # # # V A R I E N T S / T O N E S # # # # #

            HEAD_COL1, HEAD_COL2 = st.columns(2)
            with HEAD_COL1:
                VARIANT = st.selectbox("Variants", options=("1 varient", "2 varients", "3 varients"), key="varient1")
            with HEAD_COL2:
                TONE = st.selectbox("Select Tone / Voice", options=TONES_TIER1, key="tone1")

            # # # # # S E L E C T I O N # # # # #

            with st.container(border=False, height=350):

                # # # # # M O D E 1 # # # # #

                if SELECTION == "**Content Promotion Posts**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        CONTENT_PROMO_TYPE = st.selectbox("Content Type", options=("Blog post", "Video", "Ebook", "Webinar", "Podcast episode", "Infographic", "Case study", "White paper", "Report"), key="type1")
                    with SMOL2:
                        CONTENT_PROMO_PLATFORM = st.selectbox("Platform", options=("LinkedIn", "Facebook", "Twitter", "Instagram", "Website/Blog"), key="platform1")
                    with SMOL3:
                        CONTENT_PROMO_TARGET = st.text_input("Target Audience", key="target1")
                    SMOL4, SMOL5 = st.columns(2)
                    with SMOL4:
                        CONTENT_PROMO_KEYWORDS = st.text_input("Content Keywords", key="content1")
                    with SMOL5:
                        CONTENT_PROMO_CTA = st.selectbox("Call to Action", options=("Read the full article", "Watch the video", "Download the resource", "Register for the webinar", "Subscribe to the channel"), key="cta1")

                    if CONTENT_PROMO_TYPE and CONTENT_PROMO_PLATFORM and CONTENT_PROMO_TARGET and CONTENT_PROMO_KEYWORDS and CONTENT_PROMO_CTA:
                        VALID = True

                # # # # # M O D E 2 # # # # #

                if SELECTION == "**Ad Copywriter**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        AD_COPY_FORMAT = st.selectbox("Ad Format", options=("Text Ad", "Image Ad", "Video Ad", "Carousel Ad"), key="format2")
                    with SMOL2:
                        AD_COPY_TARGET = st.text_input("Target Audience", key="target2")
                    with SMOL3:
                        AD_COPY_LENGTH = st.selectbox("Ad Length", options=("Short (10-25 words)", "Medium (25-50 words)", "Long (50+ words)"), key="length2")
                    AD_COPY_CONTENT = st.text_area("Product / Service Description", key="content2")

                    if AD_COPY_FORMAT and AD_COPY_TARGET and AD_COPY_LENGTH and AD_COPY_CONTENT:
                        VALID = True

                # # # # # M O D E 3 # # # # #

                if SELECTION == "**Call to Action Generator**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        CTA_CONTENT = st.text_input("Content", key="content3")
                    with SMOL2:
                        CTA_TARGET = st.text_input("Target Audience", key="target3")
                    with SMOL3:
                        CTA_ACTION = st.selectbox("Desired Action", options=("Visit website", "Download a resource", "Register for an event", "Contact us", "Make a purchase", "Sign up for a newsletter", "Follow on social media"), key="cta3")

                    if CTA_CONTENT and CTA_TARGET and CTA_ACTION:
                        VALID = True

                # # # # # M O D E 4 # # # # #

                if SELECTION == "**AIDA Copywriter**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        AIDA_COPY_CONTENT = st.text_input("Product / Service Name", key="content4")
                    with SMOL2:
                        AIDA_COPY_TARGET = st.text_input("Target Audience", key="target4")
                    with SMOL3:
                        AIDA_COPY_CTA = st.selectbox("Call to Action", options=("Visit website", "Download a resource", "Register for an event", "Contact us", "Make a purchase", "Sign up for a newsletter", "Follow on social media"), key="cta4")
                    SMOL4, SMOL5, SMOL6 = st.columns(3)
                    with SMOL4:
                        AIDA_COPY_PROBLEM = st.text_area("Problem / Pain Point", key="problem4")
                    with SMOL5:
                        AIDA_COPY_SOLUTION = st.text_area("Solution", key="solution4")
                    with SMOL6:
                        AIDA_COPY_BENEFIT = st.text_area("Benefits", key="benefit4")

                    if AIDA_COPY_CONTENT and AIDA_COPY_TARGET and AIDA_COPY_CTA and AIDA_COPY_PROBLEM and AIDA_COPY_SOLUTION and AIDA_COPY_BENEFIT:
                        VALID = True

                # # # # # M O D E 5 # # # # #

                if SELECTION == "**PAS Copywriter**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        PAS_COPY_CONTENT = st.text_input("Product / Service Name", key="content5")
                    with SMOL2:
                        PAS_COPY_TARGET = st.text_input("Target Audience", key="target5")
                    with SMOL3:
                        PAS_COPY_CTA = st.selectbox("Call to Action", options=("Visit website", "Download a resource", "Register for an event", "Contact us", "Make a purchase", "Sign up for a newsletter", "Follow on social media"), key="cta5")
                    SMOL4, SMOL5, SMOL6 = st.columns(3)
                    with SMOL4:
                        PAS_COPY_PROBLEM = st.text_area("Problem / Pain Point", key="problem5")
                    with SMOL5:
                        PAS_COPY_SOLUTION = st.text_area("Solution", key="solution5")
                    with SMOL6:
                        PAS_COPY_AGITATION = st.text_area("Agitation", key="agitation5")

                    if PAS_COPY_CONTENT and PAS_COPY_TARGET and PAS_COPY_CTA and PAS_COPY_PROBLEM and PAS_COPY_SOLUTION and PAS_COPY_AGITATION:
                        VALID = True

                # # # # # M O D E 6 # # # # #

                if SELECTION == "**Google Ads Generator**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        GOOGLE_AD_KEYWORDS = st.text_input("Keywords", key="keywords6")
                    with SMOL2:
                        GOOGLE_AD_CTA = st.selectbox("Call to Action", options=("Visit website", "Download a resource", "Register for an event", "Contact us", "Make a purchase", "Sign up for a newsletter", "Follow on social media"), key="cta6")
                    with SMOL3:
                        GOOGLE_AD_URL = st.text_input("Landing Page URL", key="url6")
                    GOOGLE_AD_CONTENT = st.text_area("Product / Service Description", key="content6")

                    if GOOGLE_AD_KEYWORDS and GOOGLE_AD_CTA and GOOGLE_AD_URL and GOOGLE_AD_CONTENT:
                        VALID = True

                # # # # # M O D E 7 # # # # #

                if SELECTION == "**Social Media Ads Generator**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        SOCIAL_MEDIA_AD_PLATFORM = st.selectbox("Platform", options=("LinkedIn", "Facebook", "Twitter", "Instagram"), key="platform7")
                    with SMOL2:
                        SOCIAL_MEDIA_AD_FORMAT = st.selectbox("Ad Format", options=("Story Ad", "Image Ad", "Video Ad", "Carousel Ad"), key="format7")
                    with SMOL3:
                        SOCIAL_MEDIA_AD_CTA = st.selectbox("Call to Action", options=("Shop now", "Follow for more", "Like and comment"), key="cta7")
                    SMOL4, SMOL5 = st.columns(2)
                    with SMOL4:
                        SOCIAL_MEDIA_AD_TARGET = st.text_input("Target Audience", key="target7")
                    with SMOL5:
                        SOCIAL_MEDIA_AD_CONTENT = st.text_input("Product / Service Description", key="content7")

                    if SOCIAL_MEDIA_AD_PLATFORM and SOCIAL_MEDIA_AD_FORMAT and SOCIAL_MEDIA_AD_CTA and SOCIAL_MEDIA_AD_TARGET and SOCIAL_MEDIA_AD_CONTENT:
                        VALID = True

                # # # # # M O D E 8 # # # # #

                if SELECTION == "**Marketing Email Writer**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        EMAIL_WRITER_TYPE = st.selectbox("Email Type", options=("Newsletter", "Promotional email", "Welcome email", "Abandoned cart email", "Follow-up email"), key="type8")
                    with SMOL2:
                        EMAIL_WRITER_TARGET = st.text_input("Target Audience", key="target8")
                    with SMOL3:
                        EMAIL_WRITER_CTA = st.selectbox("Call to Action", options=("Shop now", "Follow for more", "Like and comment", "No CTA required"), key="cta8")
                    EMAIL_WRITER_CONTENT = st.text_area("Email Content", key="content8")

                    if EMAIL_WRITER_TYPE and EMAIL_WRITER_TARGET and EMAIL_WRITER_CTA and EMAIL_WRITER_CONTENT:
                        VALID = True

                # # # # # M O D E 9 # # # # #

                if SELECTION == "**LinkedIn Post Generator**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        LINKEDIN_POST_TYPE = st.selectbox("Post Type", options=("Article", "Update", "Question", "Quote", "Image/Video"), key="type9")
                    with SMOL2:
                        LINKEDIN_POST_TARGET = st.text_input("Target Audience", key="target9")
                    with SMOL3:
                        LINKEDIN_POST_CTA = st.selectbox("Call to Action", options=("Connect with me", "Read the article", "Watch the video", "Leave a comment"), key="cta9")
                    LINKEDIN_POST_CONTENT = st.text_area("Content / Idea / Keyword", key="content9")

                    if LINKEDIN_POST_TYPE and LINKEDIN_POST_TARGET and LINKEDIN_POST_CTA and LINKEDIN_POST_CONTENT:
                        VALID = True

                # # # # # M O D E 10 # # # # #

                if SELECTION == "**Facebook Post Generator**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        FACEBOOK_POST_TYPE = st.selectbox("Post Type", options=("Image", "Video", "Link", "Status update", "Event"), key="type10")
                    with SMOL2:
                        FACEBOOK_POST_TARGET = st.text_input("Target Audience", key="target10")
                    with SMOL3:
                        FACEBOOK_POST_CTA = st.selectbox("Call to Action", options=("Like", "Share", "Comment", "Visit website"), key="cta10")
                    FACEBOOK_POST_CONTENT = st.text_area("Content / Idea / Keyword", key="content10")

                    if FACEBOOK_POST_TYPE and FACEBOOK_POST_TARGET and FACEBOOK_POST_CTA and FACEBOOK_POST_CONTENT:
                        VALID = True


            GENERATE = st.button("Generate", use_container_width=True, type="primary", key="button1")


        with DASH_COL2:
            container = st.container(border=True, height=500)
            if not GENERATE:
                container.write("**Generated content will be displayed here**")
            if GENERATE:
                if SELECTION == "**Content Promotion Posts**":
                    container.write(CONTENT_PROMOTION_GENERATOR(VARIANT, TONE, CONTENT_PROMO_TYPE, CONTENT_PROMO_PLATFORM, CONTENT_PROMO_TARGET, CONTENT_PROMO_KEYWORDS, CONTENT_PROMO_CTA))
                if SELECTION == "**Ad Copywriter**":
                    container.write(AD_COPYWRITER(VARIANT, TONE, AD_COPY_FORMAT, AD_COPY_TARGET, AD_COPY_LENGTH, AD_COPY_CONTENT))
                if SELECTION == "**Call to Action Generator**":
                    container.write(CALL_TO_ACTION_GENERATOR(VARIANT, TONE, CTA_CONTENT, CTA_TARGET, CTA_ACTION))
                if SELECTION == "**AIDA Copywriter**":
                    container.write(AIDA_COPYWRITER(VARIANT, TONE, AIDA_COPY_CONTENT, AIDA_COPY_TARGET, AIDA_COPY_CTA, AIDA_COPY_PROBLEM, AIDA_COPY_SOLUTION, AIDA_COPY_BENEFIT))
                if SELECTION == "**PAS Copywriter**":
                    container.write(PAS_COPYWRITER(VARIANT, TONE, PAS_COPY_CONTENT, PAS_COPY_TARGET, PAS_COPY_CTA, PAS_COPY_PROBLEM, PAS_COPY_SOLUTION, PAS_COPY_AGITATION))
                if SELECTION == "**Google Ads Generator**":
                    container.write(GOOGLE_AD_GENERATOR(VARIANT, TONE, GOOGLE_AD_KEYWORDS, GOOGLE_AD_CTA, GOOGLE_AD_URL, GOOGLE_AD_CONTENT))
                if SELECTION == "**Social Media Ads Generator**":
                    container.write(SOCIAL_MEDIA_AD_GENERATOR(VARIANT, TONE, SOCIAL_MEDIA_AD_PLATFORM, SOCIAL_MEDIA_AD_FORMAT, SOCIAL_MEDIA_AD_CTA, SOCIAL_MEDIA_AD_TARGET, SOCIAL_MEDIA_AD_CONTENT))
                if SELECTION == "**Marketing Email Writer**":
                    container.write(MARKETING_EMAIL_WRITER(VARIANT, TONE, EMAIL_WRITER_TYPE, EMAIL_WRITER_TARGET, EMAIL_WRITER_CTA, EMAIL_WRITER_CONTENT))
                if SELECTION == "**LinkedIn Post Generator**":
                    container.write(LINKEDIN_POST_GENERATOR(VARIANT, TONE, LINKEDIN_POST_TYPE, LINKEDIN_POST_TARGET, LINKEDIN_POST_CTA, LINKEDIN_POST_CONTENT))
                if SELECTION == "**Facebook Post Generator**":
                    container.write(FACEBOOK_POST_GENERATOR(VARIANT, TONE, FACEBOOK_POST_TYPE, FACEBOOK_POST_TARGET, FACEBOOK_POST_CTA, FACEBOOK_POST_CONTENT))



    if MODE_SELECTION == "**Job Seekers & Professionals**":
        DASH_COL1, DASH_COL2 = st.columns(2, gap="medium")

        with DASH_COL1:

            # # # # # V A R I E N T S / T O N E S # # # # #

            HEAD_COL1, HEAD_COL2 = st.columns(2)
            with HEAD_COL1:
                VARIANT = st.selectbox("Variants", options=("1 varient", "2 varients", "3 varients"), key="varient1")
            with HEAD_COL2:
                TONE = st.selectbox("Select Tone / Voice", options=TONES_TIER1, key="tone1")

            # # # # # S E L E C T I O N # # # # #

            with st.container(border=False, height=350):

                # # # # # M O D E 1 # # # # #

                if SELECTION == "**Job application writer (resume & cover letter)**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        JOB_APPLICATION_JOB = st.selectbox("Job Title", options=("Software Engineer", "Data Scientist", "Marketing Manager", "Project Manager", "Accountant", "Sales Representative", "Customer Service Representative", "Teacher", "Nurse", "Doctor", "Lawyer", "Writer", "Designer", "Analyst", "Researcher", "Operations Manager", "Human Resources Specialist", "Financial Analyst", "Product Manager", "Business Development Manager"), key="type1")
                    with SMOL2:
                        JOB_APPLICATION_INDUSTRY = st.selectbox("Industry", options=("Technology", "Finance", "Healthcare", "Education", "Marketing", "Sales", "Customer Service", "Law", "Design", "Research", "Management", "Human Resources", "Operations", "Product Development", "Business Development", "Nonprofit", "Government", "Arts & Culture", "Media", "Retail"), key="industry1")
                    with SMOL3:
                        JOB_APPLICATION_EXPERIENCE = st.selectbox("Experience Level", options=("Entry-level", "Mid-level", "Senior-level"), key="experience1")
                    SMOL4, SMOL5 = st.columns(2)
                    with SMOL4:
                        JOB_APPLICATION_TARGET = st.text_area("Target Company", key="target1")
                    with SMOL5:
                        JOB_APPLICATION_REQUIREMENTS = st.text_area("Specific Job Requirements", key="requirements1")
                    SMOL6, SMOL7 = st.columns(2)
                    with SMOL6:                
                        JOB_APPLICATION_WORK = st.checkbox("Relevant Work Experience", key="work1")
                        if JOB_APPLICATION_WORK:
                            JOB_APPLICATION_WORK_TEXT = st.text_area("Relevant Work Experience", key="work_text1")
                        else:
                            JOB_APPLICATION_WORK_TEXT = "No relevant work experience."
                        JOB_APPLICATION_PERSONAL = st.checkbox("Personal Interests", key="personal1")
                        if JOB_APPLICATION_PERSONAL:
                            JOB_APPLICATION_PERSONAL_TEXT = st.text_area("Personal Interests", key="personal_text1")
                        else:
                            JOB_APPLICATION_PERSONAL_TEXT = "No relevant personal interests."
                    with SMOL7:
                        JOB_APPLICATION_SKILLS = st.checkbox("Skills & Expertise", key="skills1")
                        if JOB_APPLICATION_SKILLS:
                            JOB_APPLICATION_SKILLS_TEXT = st.text_area("Skills & Expertise", key="skills_text1")
                        else:
                            JOB_APPLICATION_SKILLS_TEXT = "No relevant skills or expertise."
                        JOB_APPLICATION_EDUCATION = st.checkbox("Education", key="education1")
                        if JOB_APPLICATION_EDUCATION:
                            JOB_APPLICATION_EDUCATION_TEXT = st.text_area("Education", key="education_text1")
                        else:
                            JOB_APPLICATION_EDUCATION_TEXT = "No relevant education."

                    if JOB_APPLICATION_JOB and JOB_APPLICATION_INDUSTRY and JOB_APPLICATION_EXPERIENCE and JOB_APPLICATION_TARGET and JOB_APPLICATION_REQUIREMENTS and JOB_APPLICATION_WORK_TEXT and JOB_APPLICATION_PERSONAL_TEXT and JOB_APPLICATION_SKILLS_TEXT and JOB_APPLICATION_EDUCATION_TEXT:
                        VALID = True

                # # # # # M O D E 2 # # # # #

                if SELECTION == "**Interview question generator**":
                    SMOL1, SMOL2 = st.columns(2)
                    with SMOL1:
                        INTERVIEW_JOB = st.text_input("Job Title")
                    with SMOL2:
                        INTERVIEW_STAGE = st.selectbox("Interview Stage", options=("Phone Screen (Initial screening questions)", "First Round Interview (More in-depth questions)", "Second/Subsequent Round Interview (Focus on skills, experience and fit)", "Final Round Interview"))
                    SMOL3, SMOL4 = st.columns(2)
                    with SMOL3:
                        with st.popover("Question Category"):
                            if st.checkbox("Only a Specific Category"):
                                INTERVIEW_CATEGORY = st.radio(
                                    "Question Category",
                                    ["Behavioral", "Technical", "Situational", "Culture Fit"],
                                    captions=[
                                        "eg., 'Tell me about a time you...'",
                                        "Specific to a job's skills, software, etc.",
                                        "eg., 'How would you handle...'",
                                        "eg., 'Describe your ideal work environment...'",
                                    ],
                                )
                            else:
                                INTERVIEW_CATEGORY = "All"
                    with SMOL4:
                        INTERVIEW_NUMBER = st.slider("Number of Questions", 0, 15, 5)
                    INTERVIEW_DESCRIPTION = st.text_area("Job Description")  

                    if INTERVIEW_JOB and INTERVIEW_STAGE and INTERVIEW_NUMBER and INTERVIEW_DESCRIPTION:
                        VALID = True

                # # # # # M O D E 3 # # # # #

                if SELECTION == "**Job description generator**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        JOB_DESCRIPTION_JOB = st.text_input("Title for Job Description")
                    with SMOL2:
                        JOB_DESCRIPTION_COMPANY = st.text_input("Company Name for Description")
                    with SMOL3:
                        JOB_DESCRIPTION_INDUSTRY = st.text_input("Industry / Domain")
                    SMOL4, SMOL5 = st.columns([2,1])
                    with SMOL4:
                        JOB_DESCRIPTION_RESPONSIBILITIES = st.text_area("Key Responsibilities")
                    with SMOL5:
                        JOB_DESCRIPTION_EXPERIENCE = st.slider("Required Years of Experience", 0, 15, 5)
                    
                    if JOB_DESCRIPTION_JOB and JOB_DESCRIPTION_COMPANY and JOB_DESCRIPTION_INDUSTRY and JOB_DESCRIPTION_EXPERIENCE and JOB_DESCRIPTION_RESPONSIBILITIES:
                        VALID = True

                # # # # # M O D E 4 # # # # #

                if SELECTION == "**Professional email writer**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        PRO_EMAIL_TYPE = st.selectbox("Email Type", options=("Introduction", "Follow-up", "Thank you", "Invitation", "Request", "Apology", "Complaint"), key="type4")
                    with SMOL2:
                        PRO_EMAIL_PURPOSE = st.selectbox("Purpose of Email", options=("Introduce yourself", "Follow up on a meeting", "Thank someone for their time", "Invite someone to an event", "Request information or assistance", "Apologize for an error", "Express a complaint"), key="purpose4")      
                    with SMOL3:
                        PRO_EMAIL_RECIPIENT = st.text_area("Recipient", key="recipient4")
                    SMOL4, SMOL5 = st.columns([1,2])
                    with SMOL4:
                        PRO_EMAIL_INFO = st.checkbox("Additional Information", key="info4")
                    with SMOL5:
                        if PRO_EMAIL_INFO:
                            PRO_EMAIL_INFO_TEXT = st.text_area("Additional Information", key="info_text4")
                        else:
                            PRO_EMAIL_INFO_TEXT = "No additional information."
                    
                    if PRO_EMAIL_TYPE and PRO_EMAIL_RECIPIENT and PRO_EMAIL_PURPOSE and PRO_EMAIL_INFO_TEXT:
                        VALID = True

                # # # # # M O D E 5 # # # # #

                if SELECTION == "**Document summarizer**":
                    SMOL1, SMOL2 = st.columns(2)
                    with SMOL1:
                        DOC_SUMMARY_FILE = st.file_uploader(":blue[Document File]", type="pdf")
                    with SMOL2:
                        DOC_SUMMARY_LENGTH = st.selectbox("Summary Length", options=("Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (6+ paragraphs)"), key="length5")
                    SMOL3, SMOL4 = st.columns([1,2])
                    with SMOL3:
                        DOC_SUMMARY_POINTS = st.checkbox("Include Key Points", key="points5")
                    with SMOL4:
                        if DOC_SUMMARY_POINTS:
                            DOC_SUMMARY_POINTS_TEXT = st.text_area("Key Points", key="points_text5")
                        else:
                            DOC_SUMMARY_POINTS_TEXT = "No additional information."

                    if DOC_SUMMARY_FILE and DOC_SUMMARY_LENGTH and DOC_SUMMARY_POINTS_TEXT:
                        VALID = True

                # # # # # M O D E 6 # # # # #

                if SELECTION == "**Meeting notes summarizer**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        MEETING_SUMMARY_FILE = st.text_input("File", key="file6")
                    with SMOL2:
                        MEETING_SUMMARY_LENGTH = st.selectbox("Summary Length", options=("Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (6+ paragraphs)"), key="length6")
                    with SMOL3:
                        MEETING_SUMMARY_TOPIC = st.text_area("Meeting Topic", key="topic6")

                    if MEETING_SUMMARY_FILE and MEETING_SUMMARY_LENGTH and MEETING_SUMMARY_TOPIC:
                        VALID = True

                # # # # # M O D E 7 # # # # #

                if SELECTION == "**Cover letter generator**":
                    SMOL1, SMOL2 = st.columns(2)
                    with SMOL1:
                        COVER_LETTER_JOB = st.text_input("Job Title", key="job7")
                    with SMOL2:
                        COVER_LETTER_COMPANY = st.text_input("Company", key="company7")
                    SMOL3, SMOL4 = st.columns(2)
                    with SMOL3:
                        COVER_LETTER_SKILLS = st.text_area("Skills & Qualifications", key="skills7")
                    with SMOL4:
                        COVER_LETTER_EXPERIENCE = st.text_area("Experience", key="experience7")

                    if COVER_LETTER_JOB and COVER_LETTER_COMPANY and COVER_LETTER_SKILLS and COVER_LETTER_EXPERIENCE:
                        VALID = True

                # # # # # M O D E 8 # # # # #

                if SELECTION == "**Business pitch generator**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        PITCH_BUSINESS = st.text_input("Business Idea Name")
                    with SMOL2:
                        PITCH_PROBLEM = st.text_input("Problem")
                    with SMOL3:
                        PITCH_SOLUTION = st.text_input("Solution")
                    SMOL4, SMOL5, SMOL6 = st.columns(2)
                    with SMOL4:
                        PITCH_TARGET = st.selectbox("Select the model", options=("Angel Investors", "Venture Capitalists", "Crowdfunding Platform", "Others (Specify)"))
                    with SMOL5:
                        PITCH_FORMAT = st.selectbox("Pitch Format", options=("Elevator Pitch", "One-Paragraph Summary", "Short Pitch Deck Outline"))
                    with SMOL6:
                        if PITCH_TARGET == "Others (Specify)":
                            PITCH_TARGET = st.text_input("Specify")

                    if PITCH_BUSINESS and PITCH_PROBLEM and PITCH_SOLUTION and PITCH_TARGET and PITCH_FORMAT:
                        VALID = True


                # # # # # M O D E 9 # # # # #

                if SELECTION == "**Meeting agenda generator**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        MEETING_AGENDA_TOPIC = st.text_area("Meeting Topic", key="topic9")
                    with SMOL2:
                        MEETING_AGENDA_PURPOSE = st.text_area("Meeting Purpose", key="purpose9")
                    with SMOL3:
                        MEETING_AGENDA_ATTENDEES = st.text_area("Attendees", key="attendees9")
                    SMOL4, SMOL5, SMOL6 = st.columns(3)
                    with SMOL4:
                        MEETING_AGENDA_POINTS = st.text_area("Discussion Points", key="points9")
                    with SMOL5:
                        MEETING_AGENDA_TIME = st.text_area("Time Allocation", key="time9")
                    with SMOL6:
                        MEETING_AGENDA_ACTION = st.text_area("Action Items", key="actions9")

                    if MEETING_AGENDA_TOPIC and MEETING_AGENDA_PURPOSE and MEETING_AGENDA_ATTENDEES and MEETING_AGENDA_POINTS and MEETING_AGENDA_TIME and MEETING_AGENDA_ACTION:
                        VALID = True


            GENERATE = st.button("Generate", use_container_width=True, type="primary", key="button1")


        with DASH_COL2:
            container = st.container(border=True, height=500)
            if not GENERATE:
                container.write("**Generated content will be displayed here**")
            if GENERATE:
                if SELECTION == "**Job application writer (resume & cover letter)**":
                    container.write(JOB_APPLICATION_WRITER(VARIANT, TONE, JOB_APPLICATION_JOB, JOB_APPLICATION_INDUSTRY, JOB_APPLICATION_EXPERIENCE, JOB_APPLICATION_TARGET, JOB_APPLICATION_REQUIREMENTS, JOB_APPLICATION_WORK_TEXT, JOB_APPLICATION_PERSONAL_TEXT, JOB_APPLICATION_SKILLS_TEXT, JOB_APPLICATION_EDUCATION_TEXT))
                if SELECTION == "**Interview question generator**":
                    container.write(INTERVIEW_QUESTION_GENERATOR(VARIANT, TONE, INTERVIEW_NUMBER, INTERVIEW_JOB, INTERVIEW_DESCRIPTION, INTERVIEW_STAGE, INTERVIEW_CATEGORY))
                if SELECTION == "**Job description generator**":
                    container.write(JOB_DESCRIPTION_GENERATOR(VARIANT, TONE, JOB_DESCRIPTION_JOB, JOB_DESCRIPTION_COMPANY, JOB_DESCRIPTION_INDUSTRY, JOB_DESCRIPTION_EXPERIENCE, JOB_DESCRIPTION_RESPONSIBILITIES))
                if SELECTION == "**Professional email writer**":
                    container.write(PROFESSIONAL_EMAIL_WRITER(VARIANT, TONE, PRO_EMAIL_TYPE, PRO_EMAIL_RECIPIENT, PRO_EMAIL_PURPOSE, PRO_EMAIL_INFO_TEXT))
                if SELECTION == "**Document summarizer**":
                    reader = PdfReader(DOC_SUMMARY_FILE)
                    BOOK = """"""
                    PAGE = ""
                    number_of_pages = len(reader.pages)
                    for i in range(number_of_pages):
                        PAGE = f"\n\n\n- - - - - - Page Number {i+1} - - - - - -\n\n"
                        BOOK = BOOK + PAGE
                        page = reader.pages[i]
                        text = page.extract_text()
                        BOOK = BOOK + text
                    container.write(DOCUMENT_SUMMARIZER(VARIANT, TONE, BOOK, DOC_SUMMARY_LENGTH, DOC_SUMMARY_POINTS_TEXT))
                if SELECTION == "**Meeting notes summarizer**":
                    container.write(MEETING_NOTES_SUMMARIZER(VARIANT, TONE, MEETING_SUMMARY_FILE, MEETING_SUMMARY_LENGTH, MEETING_SUMMARY_TOPIC))
                if SELECTION == "**Cover letter generator**":
                    container.write(COVER_LETTER_GENERATOR(VARIANT, TONE, COVER_LETTER_JOB, COVER_LETTER_COMPANY, COVER_LETTER_SKILLS, COVER_LETTER_EXPERIENCE))
                if SELECTION == "**Business pitch generator**":
                    container.write(BUSINESS_PITCH_GENERATOR(VARIANT, TONE, PITCH_FORMAT, PITCH_BUSINESS, PITCH_PROBLEM, PITCH_SOLUTION, PITCH_TARGET))
                if SELECTION == "**Meeting agenda generator**":
                    container.write(MEETING_AGENDA_GENERATOR(VARIANT, TONE, MEETING_AGENDA_TOPIC, MEETING_AGENDA_PURPOSE, MEETING_AGENDA_ATTENDEES, MEETING_AGENDA_POINTS, MEETING_AGENDA_TIME, MEETING_AGENDA_ACTION))



    if MODE_SELECTION == "**SEO Professionals**":
        DASH_COL1, DASH_COL2 = st.columns(2, gap="medium")

        with DASH_COL1:

            # # # # # V A R I E N T S / T O N E S # # # # #

            HEAD_COL1, HEAD_COL2 = st.columns(2)
            with HEAD_COL1:
                VARIANT = st.selectbox("Variants", options=("1 varient", "2 varients", "3 varients"), key="varient1")
            with HEAD_COL2:
                TONE = st.selectbox("Select Tone / Voice", options=TONES_TIER1, key="tone1")

            # # # # # S E L E C T I O N # # # # #

            with st.container(border=False, height=350):

                # # # # # M O D E 1 # # # # #

                if SELECTION == "**SEO content writer**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        SEO_CONTENT_TYPES = st.selectbox("Content Type", options=("Blog post", "Article", "Product page", "Landing page", "Website copy", "FAQ page", "Guide", "Case study", "White paper", "Report"), key="type1")
                    with SMOL2:
                        SEO_CONTENT_LENGTH = st.selectbox("Content Length", options=("Short (250-500 words)", "Medium (500-1000 words)", "Long (1000+ words)"), key="length1")
                    with SMOL3:
                        SEO_CONTENT_TARGET = st.text_input("Target Audience", key="target1")
                    SEO_CONTENT_KEYWORDS = st.text_input("Target Keyword", key="keyword1")

                    if SEO_CONTENT_TYPES and SEO_CONTENT_LENGTH and SEO_CONTENT_TARGET and SEO_CONTENT_KEYWORDS:
                        VALID = True

                # # # # # M O D E 2 # # # # #

                if SELECTION == "**Keyword extractor**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        KEYWORD_EXTRACT_CONTENT = st.text_area("Source Content", key="content2")
                    with SMOL2:
                        KEYWORD_EXTRACT_COUNT = st.selectbox("Number of Keywords", options=("Top 5", "Top 10", "Top 20", "All Keywords"), key="keywords2")
                    with SMOL3:
                        KEYWORD_EXTRACT_TYPE = st.selectbox("Keyword Type", options=("Short-tail (e.g., 'digital marketing')", "Long-tail (e.g., 'best digital marketing tools for small businesses')", "Head terms (e.g., 'marketing')"), key="type2")

                    if KEYWORD_EXTRACT_CONTENT and KEYWORD_EXTRACT_COUNT and KEYWORD_EXTRACT_TYPE:
                        VALID = True

                # # # # # M O D E 3 # # # # #

                if SELECTION == "**AI keyword generator**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        KEYWORD_GENERATOR_TARGET = st.text_input("Target Audience", key="target2")
                    with SMOL2:
                        KEYWORD_GENERATOR_COUNT = st.selectbox("Number of Keywords", options=("5", "10", "15", "20"), key="keywords3")
                    with SMOL3:
                        KEYWORD_GENERATOR_TYPE = st.selectbox("Keyword Type", options=("Short-tail (e.g., 'digital marketing')", "Long-tail (e.g., 'best digital marketing tools for small businesses')", "Head terms (e.g., 'marketing')"), key="type2")
                    KEYWORD_GENERATOR_SEED = st.text_input("Seed Keyword", key="seed3")

                    if KEYWORD_GENERATOR_TARGET and KEYWORD_GENERATOR_COUNT and KEYWORD_GENERATOR_TYPE and KEYWORD_GENERATOR_SEED:
                        VALID = True

                # # # # # M O D E 4 # # # # #

                if SELECTION == "**Meta title generator**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        META_TITLE_PAGE = st.text_input("Page Title", key="page4")
                    with SMOL2:
                        META_TITLE_KEYWORDS = st.text_input("Target Keyword", key="keywords4")
                    with SMOL3:
                        META_TITLE_LIMIT = st.text_input("Character Limit", key="limit4")
                    
                    if META_TITLE_PAGE and META_TITLE_KEYWORDS and META_TITLE_LIMIT:
                        VALID = True

                # # # # # M O D E 5 # # # # #

                if SELECTION == "**Meta description generator**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        META_DESCRIPTION_PAGE = st.text_input("Page Title", key="page5")
                    with SMOL2:
                        META_DESCRIPTION_KEYWORDS = st.text_input("Target Keyword", key="keywords5")
                    with SMOL3:
                        META_DESCRIPTION_LIMIT = st.text_input("Character Limit", key="limit5")
                    META_DESCRIPTION_CONTENT = st.text_area("Page Content", key="content5")

                    if META_DESCRIPTION_PAGE and META_DESCRIPTION_KEYWORDS and META_DESCRIPTION_LIMIT and META_DESCRIPTION_CONTENT:
                        VALID = True

                # # # # # M O D E 6 # # # # #

                if SELECTION == "**Website copywriter**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        WEBSITE_COPY_TYPE = st.selectbox("Page Type", options=("Home page", "About us page", "Services page", "Products page", "Contact page", "Blog page", "Landing page"), key="page6")
                    with SMOL2:
                        WEBSITE_COPY_TARGET = st.text_input("Target Audience", key="target6")
                    with SMOL3:
                        WEBSITE_COPY_TYPE = st.selectbox("Page Type", options=("Sign up", "Purchase", "Contact us"), key="cta6")
                    WEBSITE_COPY_CONTENT = st.text_area("Page Highlights", key="content6")

                    if WEBSITE_COPY_TYPE and WEBSITE_COPY_TARGET and WEBSITE_COPY_CONTENT:
                        VALID = True

                # # # # # M O D E 7 # # # # #

                if SELECTION == "**Product description generator**":
                    SMOL1, SMOL2 = st.columns(2)
                    with SMOL1:
                        PRODUCT_DESCRIPTION_TARGET = st.text_input("Target Audience")
                    with SMOL2:
                        PRODUCT_DESCRIPTION_CATEGORY = st.selectbox("Product Category", options=("Clothing", "Electronics", "Home & Kitchen", "Beauty", "Sports & Outdoors"))
                    SMOL3, SMOL4 = st.columns(2)
                    with SMOL3:
                        PRODUCT_DESCRIPTION_NAME = st.text_input("Product Name")
                    with SMOL4:
                        PRODUCT_DESCRIPTION_FEATURES = st.text_area("Key Features & Benefits")

                    if PRODUCT_DESCRIPTION_NAME and PRODUCT_DESCRIPTION_TARGET and PRODUCT_DESCRIPTION_CATEGORY and PRODUCT_DESCRIPTION_FEATURES:
                        VALID = True


            GENERATE = st.button("Generate", use_container_width=True, type="primary", key="button1")


        with DASH_COL2:
            container = st.container(border=True, height=500)
            if not GENERATE:
                container.write("**Generated content will be displayed here**")
            if GENERATE:
                if SELECTION == "**SEO content writer**":
                    container.write(SEO_CONTENT_WRITER(VARIANT, TONE, SEO_CONTENT_TYPES, SEO_CONTENT_LENGTH, SEO_CONTENT_TARGET, SEO_CONTENT_KEYWORDS))
                if SELECTION == "**Keyword extractor**":
                    container.write(KEYWORD_EXTRACTOR(VARIANT, TONE, KEYWORD_EXTRACT_CONTENT, KEYWORD_EXTRACT_COUNT, KEYWORD_EXTRACT_TYPE))
                if SELECTION == "**AI keyword generator**":
                    container.write(KEYWORD_GENERATOR(VARIANT, TONE, KEYWORD_GENERATOR_TARGET, KEYWORD_GENERATOR_COUNT, KEYWORD_GENERATOR_TYPE, KEYWORD_GENERATOR_SEED))
                if SELECTION == "**Meta title generator**":
                    container.write(META_TITLE_GENERATOR(VARIANT, TONE, META_TITLE_PAGE, META_TITLE_KEYWORDS, META_TITLE_LIMIT))
                if SELECTION == "**Meta description generator**":
                    container.write(META_DESCRIPTION_GENERATOR(VARIANT, TONE, META_DESCRIPTION_PAGE, META_DESCRIPTION_KEYWORDS, META_DESCRIPTION_LIMIT, META_DESCRIPTION_CONTENT))
                if SELECTION == "**Website copywriter**":
                    container.write(WEBSITE_COPYWRITER(VARIANT, TONE, WEBSITE_COPY_TYPE, WEBSITE_COPY_TARGET, WEBSITE_COPY_CONTENT))
                if SELECTION == "**Product description generator**":
                    container.write(PRODUCT_DESCRIPTION_GENERATOR(VARIANT, TONE, PRODUCT_DESCRIPTION_NAME, PRODUCT_DESCRIPTION_CATEGORY, PRODUCT_DESCRIPTION_FEATURES, PRODUCT_DESCRIPTION_TARGET, TONE))



    if MODE_SELECTION == "**Students & Educators**":
        DASH_COL1, DASH_COL2 = st.columns(2, gap="medium")

        with DASH_COL1:

            # # # # # V A R I E N T S / T O N E S # # # # #

            HEAD_COL1, HEAD_COL2 = st.columns(2)
            with HEAD_COL1:
                VARIANT = st.selectbox(":blue[Variants]", options=("1 varient", "2 varients", "3 varients"), key="varient1", disabled=True)
            with HEAD_COL2:
                TONE = st.selectbox(":blue[Select Tone / Voice]", options=TONES_TIER1, key="tone1", disabled=True)

            # # # # # S E L E C T I O N # # # # #

            with st.container(border=False, height=350):

                # # # # # M O D E 1 # # # # #

                if SELECTION == "**Research Paper Summarizer**":
                    SMOL1, SMOL2 = st.columns(2)
                    with SMOL1:
                        RESEARCH_SUMMARY_FOCUS = st.selectbox(":blue[Summary Focus]", options=("General Overview", "Key Findings", "Methodology", "Limitations"), key="type1")
                    with SMOL2:
                        RESEARCH_SUMMARY_LENGTH = st.selectbox(":blue[Summary Length]", options=("Short Summary (Bullet points)", "Medium Summary (Paragraph)", "Long Summary (Multiple paragraphs)"), key="length1")
                    SMOL3, SMOL4 = st.columns([1,2])
                    with SMOL3:
                        RESEARCH_SUMMARY_BOOL = st.checkbox(":blue[Upload PDF Document]", key="bool1")
                    with SMOL4:
                        if RESEARCH_SUMMARY_BOOL:
                            RESEARCH_SUMMARY_FILE = st.file_uploader(":blue[Research Document]", type="pdf")
                            RESEARCH_SUMMARY_BOOL_TEXT = "File uploaded"
                        else:
                            RESEARCH_SUMMARY_TEXT = st.text_area(":blue[Research Content]", key="content1")
                            RESEARCH_SUMMARY_BOOL_TEXT = "Content entered"

                    if (RESEARCH_SUMMARY_FOCUS and RESEARCH_SUMMARY_LENGTH and RESEARCH_SUMMARY_BOOL_TEXT == "File uploaded") or (RESEARCH_SUMMARY_FOCUS and RESEARCH_SUMMARY_LENGTH and RESEARCH_SUMMARY_BOOL_TEXT == "Content entered"):
                        VALID = True

                # # # # # M O D E 2 # # # # #

                if SELECTION == "**Lesson Explainer**":
                    CHAPTER_EXPLAINER_TARGET = st.text_input(":blue[Student Grade]", key="grade2")
                    CHAPTER_EXPLAINER_BOOK = st.file_uploader(":blue[Chapter PDF to Explain]", type="pdf")

                    if CHAPTER_EXPLAINER_TARGET and CHAPTER_EXPLAINER_BOOK:
                        VALID = True

                # # # # # M O D E 3 # # # # #

                if SELECTION == "**Question Paper Generator**":
                    SMOL1, SMOL2 = st.columns(2)
                    with SMOL1:
                        QUESTION_PAPER_SUBJECT = st.text_input(":blue[Subject]")
                    with SMOL2:
                        QUESTION_PAPER_LEVEL = st.text_input(":blue[Level / Grade]")
                    QUESTION_PAPER_TYPES = st.multiselect(
                        ":blue[Types of Questions]",
                        ["Multiple Choice", "True/False", "Fill in the Blanks", "Very Short Answer (max 40 words)", "Short Answer (max 80 words)", "Essay/Long Answer (max 120 words)"],
                        ["Multiple Choice", "Very Short Answer (max 40 words)"],
                    )
                    SMOL3, SMOL4 = st.columns(2)
                    with SMOL3:
                        QUESTION_PAPER_NUMBERS = st.slider(":blue[Number of Questions]", 5, 20, 12)
                    with SMOL4:
                        QUESTION_PAPER_TIME = st.slider(":blue[Time to Complete Questions]", 5, 60, 20)
                    QUESTION_PAPER_BOOK = st.file_uploader(":blue[Upload Chapter PDF]", type="pdf")

                    if QUESTION_PAPER_SUBJECT and QUESTION_PAPER_LEVEL and QUESTION_PAPER_TYPES and QUESTION_PAPER_NUMBERS and QUESTION_PAPER_TIME and QUESTION_PAPER_BOOK:
                        VALID = True

                # # # # # M O D E 4 # # # # #

                if SELECTION == "**Study Guide Creator**":
                    STUDY_GUIDE_TYPE = st.multiselect(
                        ":blue[Study Guide Format]",
                        ["Key Terms & Definitions", "Important Concepts (Summaries)", 
                        "Practice Questions (Multiple choice, True/False, etc.)", 
                        "Timeline/Chronology", "Flashcards"], key="type4"
                    )
                    STUDY_GUIDE_BOOK = st.file_uploader(":blue[Upload Chapter PDF]", type="pdf")
                    
                    if STUDY_GUIDE_TYPE and STUDY_GUIDE_BOOK:
                        VALID = True      

            if VALID:
                GENERATE = st.button("Generate", use_container_width=True, type="primary", key="button1")
            else:
                GENERATE = st.button("Generate", use_container_width=True, type="primary", key="button1", disabled=True)


        with DASH_COL2:
            container = st.container(border=True, height=500)
            if not GENERATE:
                container.write("**Generated content will be displayed here**")
            if GENERATE:
                if SELECTION == "**Research Paper Summarizer**":
                    if RESEARCH_SUMMARY_FOCUS and RESEARCH_SUMMARY_LENGTH and RESEARCH_SUMMARY_BOOL_TEXT == "Content entered":
                        container.write(RESEARCH_PAPER_SUMMARIZER(RESEARCH_SUMMARY_FOCUS, RESEARCH_SUMMARY_LENGTH, RESEARCH_SUMMARY_TEXT))
                    if RESEARCH_SUMMARY_FOCUS and RESEARCH_SUMMARY_LENGTH and RESEARCH_SUMMARY_BOOL_TEXT == "File uploaded":
                        reader = PdfReader(RESEARCH_SUMMARY_FILE)
                        TEXT = """"""
                        PAGE = ""
                        number_of_pages = len(reader.pages)
                        for i in range(number_of_pages):
                            PAGE = f"\n\n\n- - - - - - Page Number {i+1} - - - - - -\n\n"
                            TEXT = TEXT + PAGE
                            page = reader.pages[i]
                            text = page.extract_text()
                            TEXT = TEXT + text
                        container.write(RESEARCH_PAPER_SUMMARIZER(RESEARCH_SUMMARY_FOCUS, RESEARCH_SUMMARY_LENGTH, TEXT))

                if SELECTION == "**Lesson Explainer**":
                    reader = PdfReader(CHAPTER_EXPLAINER_BOOK)
                    BOOK = """"""
                    PAGE = ""
                    number_of_pages = len(reader.pages)
                    for i in range(number_of_pages):
                        PAGE = f"\n\n\n- - - - - - Page Number {i+1} - - - - - -\n\n"
                        BOOK = BOOK + PAGE
                        page = reader.pages[i]
                        text = page.extract_text()
                        BOOK = BOOK + text
                    container.write(CHAPTER_EXPLAINER(BOOK, CHAPTER_EXPLAINER_TARGET))

                if SELECTION == "**Question Paper Generator**":
                    reader = PdfReader(QUESTION_PAPER_BOOK)
                    BOOK = """"""
                    PAGE = ""
                    number_of_pages = len(reader.pages)
                    for i in range(number_of_pages):
                        PAGE = f"\n\n\n- - - - - - Page Number {i+1} - - - - - -\n\n"
                        BOOK = BOOK + PAGE
                        page = reader.pages[i]
                        text = page.extract_text()
                        BOOK = BOOK + text
                    container.write(QUESTION_PAPER_GENERATION(QUESTION_PAPER_SUBJECT, QUESTION_PAPER_LEVEL, QUESTION_PAPER_TYPES, QUESTION_PAPER_NUMBERS, QUESTION_PAPER_TIME, BOOK))
                
                if SELECTION == "**Study Guide Creator**":
                    reader = PdfReader(STUDY_GUIDE_BOOK)
                    BOOK = """"""
                    PAGE = ""
                    number_of_pages = len(reader.pages)
                    for i in range(number_of_pages):
                        PAGE = f"\n\n\n- - - - - - Page Number {i+1} - - - - - -\n\n"
                        BOOK = BOOK + PAGE
                        page = reader.pages[i]
                        text = page.extract_text()
                        BOOK = BOOK + text
                    container.write(STUDY_GUIDE_CREATOR(STUDY_GUIDE_TYPE, BOOK))



    if MODE_SELECTION == "**Personal Use & Creativity**":
        DASH_COL1, DASH_COL2 = st.columns(2, gap="medium")

        with DASH_COL1:

            # # # # # V A R I E N T S / T O N E S # # # # #

            HEAD_COL1, HEAD_COL2 = st.columns(2)
            with HEAD_COL1:
                VARIANT = st.selectbox("Variants", options=("1 varient", "2 varients", "3 varients"), key="varient1")
            with HEAD_COL2:
                TONE = st.selectbox("Select Tone / Voice", options=TONES_TIER1, key="tone1")

            # # # # # S E L E C T I O N # # # # #

            with st.container(border=False, height=350):

                # # # # # M O D E 1 # # # # #

                if SELECTION == "**Song Lyrics Generator**":
                    SMOL1, SMOL2 = st.columns(2)
                    with SMOL1:
                        SONG_GENRE = st.selectbox("Genre", options=('Pop', 'Rock', 'Hip-Hop', 'Country', 'Jazz', 'Classical', 'Electronic'), key="genre1")
                    with SMOL2:
                        SONG_THEME = st.selectbox("Theme", options=('Love', 'Breakup', 'Happiness', 'Sadness', 'Anger', 'Hope', 'Nature', 'Travel', 'Dreams'), key="theme1")
                    SONG_KEYWORDS = st.text_input("Keywords", key="keyword1")

                    if SONG_GENRE and SONG_THEME and SONG_KEYWORDS:
                        VALID = True

                # # # # # M O D E 2 # # # # #

                if SELECTION == "**Poem Generator**":
                    SMOL1, SMOL2 = st.columns(2)
                    with SMOL1:
                        POEM_TYPE = st.selectbox("Type", options=('Free verse', 'Sonnet', 'Haiku', 'Limerick'), key="type2")
                    with SMOL2:
                        POEM_THEME = st.selectbox("Theme", options=('Love', 'Breakup', 'Happiness', 'Sadness', 'Anger', 'Hope', 'Nature', 'Travel', 'Dreams'), key="theme2")
                    POEM_KEYWORDS = st.text_input("Keywords", key="keyword2")

                    if POEM_TYPE and POEM_THEME and POEM_KEYWORDS:
                        VALID = True

                # # # # # M O D E 3 # # # # #

                if SELECTION == "**Story Generator**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        STORY_GENRE = st.selectbox("Genre", options=('Fantasy', 'Science fiction', 'Romance', 'Mystery', 'Thriller', 'Historical fiction'), key="genre3")
                    with SMOL2:
                        STORY_THEME = st.selectbox("Theme", options=('Love', 'Breakup', 'Happiness', 'Sadness', 'Anger', 'Hope', 'Nature', 'Travel', 'Dreams'), key="theme3")
                    with SMOL3:
                        STORY_SETTING = st.selectbox("Setting", options=('Medieval kingdom', 'Post-apocalyptic world', 'Space station', 'Haunted house', 'Modern city'), key="setting3")
                    SMOL4, SMOL5 = st.columns(2)
                    with SMOL4:
                        STORY_CHARACTERS = st.text_area("Story Characters", key="character3")
                    with SMOL5:
                        STORY_PLOT = st.text_area("Plot Points", key="plot3")

                    if STORY_GENRE and STORY_THEME and STORY_SETTING and STORY_CHARACTERS and STORY_PLOT:
                        VALID = True

                # # # # # M O D E 4 # # # # #

                if SELECTION == "**Personalized Recipe Generator**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        RECIPE_CUISINE = st.selectbox("Cuisine", options=('Any Cuisine', 'Italian', 'Mexican', 'Indian', 'Chinese', 'American'), key="cuisine4")
                    with SMOL2:
                        RECIPE_RESTRICTION = st.multiselect("Diet Restrictions", ['No Restrictions', 'Vegetarian', 'Vegan', 'Gluten-free', 'Dairy-free', 'Pork-free', 'Red Meat-free', 'Beef-free'], ['No Restrictions'], key="restriction4")
                    with SMOL3:
                        RECIPE_LEVEL = st.selectbox("Difficulty Level", options=('Easy', 'Medium', 'Hard'), key="level4")
                    RECIPE_INGREDIENTS = st.text_area("Ingredients", key="ingredient4")
                    
                    if RECIPE_CUISINE and RECIPE_RESTRICTION and RECIPE_LEVEL and RECIPE_INGREDIENTS:
                        VALID = True

                # # # # # M O D E 5 # # # # #

                if SELECTION == "**Recipe from Ingredients**":
                    SMOL1, SMOL2 = st.columns(2)
                    with SMOL1:
                        QUICK_RECIPE_CUISINE = st.selectbox("Cuisine", options=('Any Cuisine', 'Italian', 'Mexican', 'Indian', 'Chinese', 'American'), key="cuisine5")
                    with SMOL2:
                        QUICK_RECIPE_TYPE = st.selectbox("Dish Type", options=('Soup', 'Salad', 'Main course', 'Dessert'), key="type5")
                    QUICK_RECIPE_INGREDIENTS = st.text_area("Available Ingredients", key="ingredient5")

                    if QUICK_RECIPE_CUISINE and QUICK_RECIPE_TYPE and QUICK_RECIPE_INGREDIENTS:
                        VALID = True

                # # # # # M O D E 6 # # # # #

                if SELECTION == "**Personalized Email Writer**":
                    SMOL1, SMOL2, SMOL3 = st.columns(3)
                    with SMOL1:
                        PERSONALIZED_EMAIL_TYPE = st.selectbox("Page Type", options=("Home page", "About us page", "Services page", "Products page", "Contact page", "Blog page", "Landing page"), key="page6")
                    with SMOL2:
                        PERSONALIZED_EMAIL_RECIPIENT = st.text_input("Target Audience", key="target6")
                    PERSONALIZED_EMAIL_CONTENT = st.text_area("Email Content", key="content6")
                    SMOL3, SMOL4 = st.columns([1,2])
                    with SMOL3:
                        PERSONALIZED_EMAIL_EXTRA = st.checkbox("Include Additional Information", key="extra6")
                    with SMOL4:
                        if PERSONALIZED_EMAIL_EXTRA:
                            PERSONALIZED_EMAIL_EXTRA_CONTENT = st.text_area("Additional Information", key="extra_text6")
                        else:
                            PERSONALIZED_EMAIL_EXTRA_CONTENT = "No additional information required."

                    if PERSONALIZED_EMAIL_CONTENT and PERSONALIZED_EMAIL_TYPE and PERSONALIZED_EMAIL_RECIPIENT and PERSONALIZED_EMAIL_EXTRA_CONTENT:
                        VALID = True


            GENERATE = st.button("Generate", use_container_width=True, type="primary", key="button1")


        with DASH_COL2:
            container = st.container(border=True, height=500)
            if not GENERATE:
                container.write("**Generated content will be displayed here**")
            if GENERATE:
                if SELECTION == "**Song Lyrics Generator**":
                    container.write(SONG_LYRICS_GENERATOR(VARIANT, TONE, SONG_GENRE, SONG_THEME, SONG_KEYWORDS))
                if SELECTION == "**Poem Generator**":
                    container.write(POEM_GENERATOR(VARIANT, TONE, POEM_TYPE, POEM_THEME, POEM_KEYWORDS))
                if SELECTION == "**Story Generator**":
                    container.write(STORY_GENERATOR(VARIANT, TONE, STORY_GENRE, STORY_THEME, STORY_SETTING, STORY_CHARACTERS, STORY_PLOT))
                if SELECTION == "**Personalized Recipe Generator**":
                    container.write(PERSONALIZED_RECIPE_GENERATOR(VARIANT, TONE, RECIPE_CUISINE, RECIPE_RESTRICTION, RECIPE_LEVEL, RECIPE_INGREDIENTS))
                if SELECTION == "**Recipe from Ingredients**":
                    container.write(RECIPE_GENERATOR(VARIANT, TONE, QUICK_RECIPE_CUISINE, QUICK_RECIPE_TYPE, QUICK_RECIPE_INGREDIENTS))
                if SELECTION == "**Personalized Email Writer**":
                    container.write(PERSONALIZED_EMAIL_GENERATOR(VARIANT, TONE, PERSONALIZED_EMAIL_CONTENT, PERSONALIZED_EMAIL_TYPE, PERSONALIZED_EMAIL_RECIPIENT, PERSONALIZED_EMAIL_EXTRA_CONTENT))



    if MODE_SELECTION == "**Coding & Technical Tools**":
        DASH_COL1, DASH_COL2 = st.columns(2, gap="medium")

        with DASH_COL1:

            # # # # # V A R I E N T S / T O N E S # # # # #

            HEAD_COL1, HEAD_COL2 = st.columns(2)
            with HEAD_COL1:
                VARIANT = st.selectbox(":blue[Variants]", options=("1 varient", "2 varients", "3 varients"), key="varient1", disabled=True)
            with HEAD_COL2:
                TONE = st.selectbox(":blue[Select Tone / Voice]", options=TONES_TIER1, key="tone1", disabled=True)

            # # # # # S E L E C T I O N # # # # #

            with st.container(border=False, height=350):

                # # # # # M O D E 1 # # # # #

                if SELECTION == "**Code Generator**":
                    SMOL1, SMOL2 = st.columns(2)
                    with SMOL1:
                        CODE_INSTRUCTION = st.text_area("Code Task / Instruction", key="content1")
                    with SMOL2:
                        CODE_LANGUAGE = st.selectbox("Programming Language", options=LANGUAGES_FOR_CODE, key="length1")
                    SMOL3, SMOL4 = st.columns(2)
                    with SMOL3:
                        CODE_EXAMPLE = st.checkbox("Include Code Example")
                    with SMOL4:
                        if CODE_EXAMPLE:
                            CODE_EXAMPLE_TEXT = st.text_area("Code Example", key="example1")
                        else:
                            CODE_EXAMPLE_TEXT = st.write("Code Example Not Required")

                    if CODE_INSTRUCTION and CODE_LANGUAGE and CODE_EXAMPLE_TEXT:
                        VALID = True

                # # # # # M O D E 2 # # # # #

                if SELECTION == "**Technical Documentation Writer**":
                    SMOL1, SMOL2 = st.columns(2)
                    with SMOL1:
                        DOCUMENTATION_TYPE = st.selectbox("Document Type", options=("API documentation", "User manual", "Software guide", "Tutorials", "White paper", "Technical specification"), key="type2")
                    with SMOL2:
                        DOCUMENTATION_LEVEL = st.selectbox("Level of Detail Required", options=("Beginner", "Intermediate", "Advanced"), key="level2")
                    DOCUMENTATION_CONTENT = st.text_area("Code Snippets", key="content2")

                    if DOCUMENTATION_TYPE and DOCUMENTATION_LEVEL and DOCUMENTATION_CONTENT:
                        VALID = True


            GENERATE = st.button("Generate", use_container_width=True, type="primary", key="button1")


        with DASH_COL2:
            container = st.container(border=True, height=500)
            if not GENERATE:
                container.write("**Generated content will be displayed here**")
            if GENERATE:
                if SELECTION == "**Code Generator**":
                    container.write(CODE_GENERATOR(VARIANT, TONE, CODE_INSTRUCTION, CODE_LANGUAGE, CODE_EXAMPLE_TEXT))
                if SELECTION == "**Technical Documentation Writer**":
                    container.write(TECHNICAL_DOCUMENTATION_WRITER(VARIANT, TONE, DOCUMENTATION_TYPE, DOCUMENTATION_LEVEL, DOCUMENTATION_CONTENT))



    if MODE_SELECTION == "**Additional Tools**":
        DASH_COL1, DASH_COL2 = st.columns(2, gap="medium")

        with DASH_COL1:

            # # # # # V A R I E N T S / T O N E S # # # # #

            HEAD_COL1, HEAD_COL2 = st.columns(2)
            with HEAD_COL1:
                VARIANT = st.selectbox("Variants", options=("1 varient", "2 varients", "3 varients"), key="varient1")
            with HEAD_COL2:
                TONE = st.selectbox("Select Tone / Voice", options=TONES_TIER1, key="tone1")

            # # # # # S E L E C T I O N # # # # #

            with st.container(border=False, height=350):

                # # # # # M O D E 1 # # # # #

                if SELECTION == "**Grammar Checker & Improver**":
                    SMOL1, SMOL2 = st.columns(2)
                    with SMOL1:
                        GRAMMAR_CONTENT = st.text_area("Content to Check", key="content1")
                    with SMOL2:
                        GRAMMAR_LEVEL = st.selectbox("Content Length", options=("Basic (highlighting major errors)", "Advanced (providing detailed explanations and suggestions)"), key="level1")

                    if GRAMMAR_CONTENT and GRAMMAR_LEVEL:
                        VALID = True

                # # # # # M O D E 2 # # # # #

                if SELECTION == "**Sentence Reworder**":
                    REWORD_CONTENT = st.text_area("Content to Reword", key="content2")

                    if REWORD_CONTENT:
                        VALID = True

                # # # # # M O D E 3 # # # # #

                if SELECTION == "**Text Inflator**":
                    SMOL1, SMOL2 = st.columns(3)
                    with SMOL1:
                        INFLATOR_CONTENT = st.text_area("Content to Inflate", key="content3")
                    with SMOL2:
                        INFLATOR_LEVEL = st.selectbox("Inflation Level", options=("Slight (add a few extra words and phrases)", "Moderate (expand on existing ideas and add details)", "Extensive (significantly increase the length by adding more information and examples)"), key="level3")

                    if INFLATOR_CONTENT and INFLATOR_LEVEL:
                        VALID = True

                # # # # # M O D E 4 # # # # #

                if SELECTION == "**Sentence Shortener**":
                    SMOL1, SMOL2 = st.columns(2)
                    with SMOL1:
                        SHORTENER_CONTENT = st.text_area("Content to Shorten", key="content4")
                    with SMOL2:
                        SHORTENER_LEVEL = st.selectbox("Shortening Style", options=("Remove unnecessary words", "Simplify complex phrasing", "Combine sentences"), key="level4")
                    
                    if SHORTENER_CONTENT and SHORTENER_LEVEL:
                        VALID = True

                # # # # # M O D E 5 # # # # #

                if SELECTION == "**Summarizer**":
                    SMOL1, SMOL2 = st.columns(2)
                    with SMOL1:
                        SUMMARY_CONTENT = st.text_area("Content to Summarize", key="content5")
                    with SMOL2:
                        SUMMARY_LENGTH = st.selectbox("Summary Length", options=("Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (6+ paragraphs)"), key="length5")

                    if SUMMARY_CONTENT and SUMMARY_LENGTH:
                        VALID = True

                # # # # # M O D E 6 # # # # #

                if SELECTION == "**Translator**":
                    SMOL1, SMOL2 = st.columns(2)
                    with SMOL1:
                        TRANSLATOR_CONTENT = st.text_area("Content to Translate", key="content6")
                    with SMOL2:
                        TRANSLATOR_LANGUAGE = st.selectbox("Language", options=LANGUAGES_FOR_TRANSLATION, key="translate6")
                    
                    if TRANSLATOR_CONTENT and TRANSLATOR_LANGUAGE:
                        VALID = True
                        

            GENERATE = st.button("Generate", use_container_width=True, type="primary", key="button1")


        with DASH_COL2:
            container = st.container(border=True, height=500)
            if not GENERATE:
                container.write("**Generated content will be displayed here**")
            if GENERATE:
                if SELECTION == "**Grammar Checker & Improver**":
                    container.write(GRAMMAR_CHECKER(VARIANT, TONE, GRAMMAR_CONTENT, GRAMMAR_LEVEL))
                if SELECTION == "**Sentence Reworder**":
                    container.write(SENTENCE_REWORDER(VARIANT, TONE, REWORD_CONTENT))
                if SELECTION == "**Text Inflator**":
                    container.write(TEXT_INFLATOR(VARIANT, TONE, INFLATOR_CONTENT, INFLATOR_LEVEL))
                if SELECTION == "**Sentence Shortener**":
                    container.write(SENTENCE_SHORTENER(VARIANT, TONE, SHORTENER_CONTENT, SHORTENER_LEVEL))
                if SELECTION == "**Summarizer**":
                    container.write(SUMMARIZER(VARIANT, TONE, SUMMARY_CONTENT, SUMMARY_LENGTH))
                if SELECTION == "**Translator**":
                    container.write(TRANSLATOR(VARIANT, TONE, TRANSLATOR_CONTENT, TRANSLATOR_LANGUAGE))



