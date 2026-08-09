# AIM >> 1. TAKES A RAW PARAGRAPH ABOUT THE A MOVIE
#         2. EXTRACT IMPORTANT STRUCTURED INFORMATION
#         3. GENEARATES A CLEAN SUMMARY OF THE MOVIE
#         4. STORES IT IN THEIR DATABASES

#-----------------------------------------------------------------------------------------------------------------------------------------

#ONE WAY > 


# from dotenv import load_dotenv
# load_dotenv()


# from langchain_mistralai import ChatMistralAI

# model = ChatMistralAI(model="mistral-small-2603")

# response = model.invoke(""" Inception is a mind-bending science fiction thriller directed by Christopher Nolan. Released in 2010, the film stars Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, 
#                         Tom Hardy, and Ken Watanabe. The story follows Dom Cobb, a skilled thief who specializes in stealing valuable information by entering people's dreams. He is given a challenging
#                           mission to plant an idea into someone's mind through a process known as inception. The movie was widely praised for its unique concept, stunning visual effects, complex storytelling, '
#                           'and Hans Zimmer's memorable soundtrack. It is considered one of the most innovative science fiction films of modern cinema.
# CAN YOU PLEASE EXTRACT THE SUMMARY AND THE INFORMATION OF THE MOVIE """)

# print(response.content)  



#output >>

# Here’s the extracted summary and key information about the movie **Inception (2010)**:

# ---

# ### **Summary:**
# *Inception* is a mind-bending science fiction thriller directed by **Christopher Nolan**. The story follows **Dom Cobb** (Leonardo DiCaprio), a skilled "extractor" who steals valuable secrets by infiltrating people’s dreams. Cobb is offered a high-stakes mission called **"inception"**—planting an idea deep within someone’s subconscious rather than stealing it. Alongside a team of experts (including **Ariadne** played by Ellen Page, **Arthur** by Joseph Gordon-Levitt, and **Eames** by Tom Hardy), Cobb must navigate layered dreams, time dilation, and his own psychological demons to pull off the impossible. The film explores themes of reality vs. illusion, guilt, and the power of the mind.

# ---

# ### **Key Information:**
# - **Director:** Christopher Nolan
# - **Release Year:** 2010
# - **Genre:** Science Fiction / Thriller / Action
# - **Main Cast:**
#   - **Leonardo DiCaprio** as Dom Cobb
#   - **Joseph Gordon-Levitt** as Arthur
#   - **Ellen Page** as Ariadne
#   - **Tom Hardy** as Eames
#   - **Ken Watanabe** as Saito
# - **Music:** Hans Zimmer (iconic soundtrack)
# - **Visual Effects:** Praised for innovative dream sequences and practical effects.
# - **Awards:** Won 4 Oscars (Cinematography, Sound Mixing, Sound Editing, Visual Effects) and nominated for 4 more.
# - **Legacy:** Considered a modern classic for its complex narrative, originality, and technical craftsmanship.




#-----------------------------------------------------------------------------------------------------------------------------------------

#BUT THE MAJOR PROBELM IS THAT I HAVE TO WRITE PARAGRAPH INSIDE MODEL.INVOKE() FUNCTION AND
# ALSO I HAVE TO WRITE A  PROMPT INSIDE IT FOR WORK DONE

# IT IS GOOD FOR 1-2 TIMES , BUT IF WE HAVE TO DO THIS 1 TIMES THAN IT WILL NOT BE GOOD AND ALSO NOT FESIBLE FOR THE USER


#SO BEST WAY TO DO IT BY USING CHAT PROMPT TEMPLATE >> 1. WE CAN CREATE A CHAT PROMPT TEMPLATE
#                                           2. WE CAN PASS THE RAW PARAGRAPH AND PROMPT TO IT   


#TEMPLETAE EX >
#PLEASE YOU ARE A GOOD AI  AND YOU HAVE TO SUMMARIZE THIS {PARAGRAPH} AND ALSO EXTRACT THE INFORMATION OF
#  IT AND GIVE ME A CLEAN SUMMARY AND INFORMATION OF IT


#SO THIS IS REUSABLE > template is a kind of structured prompt which we can reuse again and agian and usually we use it when we have to create 
#any usecase application

#-----------------------------------------------------------------------------------------------------------------------------------------







# PromptTemplate
# Prompt template for a language model.

# A prompt template consists of a string template. It accepts a set of parameters from the user that can be used to generate
#  a prompt for a language model.

# The template can be formatted using either f-strings (default), jinja2 (is a template engine use in danjgo), or mustache syntax.




#  BY PROMPT TEMPLATE > 

from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
#IF WE ARE USING BASIC LLM THEN WE CAN WRITE PromptTemplate , BUT IF WE ARE USING THAT ISTSELF IS CHAT MODEL THAN BEFORE PROMPT WE CAN
#WRITE ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-2603")


#NOW WE ARE NOT USING MESSGAGES LIKE HUMAN_MESSAGE, SYSTEM_MESSAGE, AI_MESSAGE. AS IN PROMPT TEMPELATE WE AUTOMATICALLY GIVES ROLES

# prompt = PromptTemplate.from_template("Say {foo}")
prompt = ChatPromptTemplate.from_messages([        #THIS IS KNOWN AS RUNNABLES
    (
        "system",
        """
You are a professional Movie Information Extraction Assistant.

Your task:
Carefully analyze the given movie paragraph and extract the most useful and relevant information from it.

Rules:
- Extract information only from the provided paragraph.
- Do NOT add explanations or extra commentary.
- Do NOT guess or invent unknown facts.
- If any information is not available, write "Not Mentioned".
- Keep the information clear, concise, and accurate.
- Keep the quick summary short (2-3 sentences maximum).
- Follow the exact output format given below.

Output Format:

Movie Title:
Release Year:
Genre:
Director:
Main Cast:
Plot:
IMDb Rating:
Music Composer:
Notable Features:
Recognition / Achievements:

Summary:
"""
    ),
    (
        "human",
        """
Extract the information from the following paragraph:

{paragraph}
"""
    )
])



#to put info in {paragraph} > we need to call > ChatPromptTemplate.from_messages


para = input("Give your Paragraph :")




#AFTER GETTING THIS "para" WE WILL GOING TO USE THIS INSIDE {paragraph}

final_prompt = prompt.invoke(
    {"paragraph" : para}
)


response = model.invoke(final_prompt)
#since we are able to inkove this prompt thats way this thing is known as runnable(chains)

print(response.content)  



#PROMPT TEMPALTE USES NOT ONLY LIMITED TO THIS, LET SAY WE ARE MAKING A PROMPT WHERE WE ARE TELLING 6-7 THINGS FOR EX> NMAE, AGE, ETC.. 
#ON THE BASIS OF THAT OUR AI IS WORKING
#SO WE CAN USE PROMPT TEMPLATE FOR THAT ALSO AGAIN AND AGAIN


#OUTPUT > 
# Give your Paragraph :Inception is a mind-bending science fiction thriller directed by Christopher Nolan. Released in 2010,
#  the film starsLeonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, Tom Hardy, and Ken Watanabe. The story follows Dom Cobb,
#  a skilled thief who specializes in stealing valuable information by entering people's dreams. He is given a challenging mission 
# to plant an idea into someone's mind through a process known as inception. The movie was widely praised for its unique concept, 
# stunning visual effects, complex storytelling, and Hans Zimmer's memorable soundtrack. It is considered one of the most 
# innovative science fiction films of modern cinema.


# Movie Title:
# Inception

# Release Year:
# 2010

# Genre:
# Science Fiction Thriller

# Director:
# Christopher Nolan

# Main Cast:
# Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, Tom Hardy, Ken Watanabe

# Plot:
# Dom Cobb, a skilled thief who steals valuable information by entering people's dreams, is tasked with planting an idea into someone's mind through a process called inception.

# IMDb Rating:
# Not Mentioned

# Music Composer:
# Hans Zimmer

# Notable Features:
# Unique concept, stunning visual effects, complex storytelling, memorable soundtrack

# Recognition / Achievements:
# Considered one of the most innovative science fiction films of modern cinema

# Summary:
# A mind-bending sci-fi thriller about a thief who extracts secrets from dreams and is challenged to plant an idea instead. Praised for itsinnovative storytelling and visuals.