#write now our app prints nice text 
#But the companies don't want text
#They want data they can store, search, filter
#recommend, analyze, send to APIs.
#That is called Structured Output.

#or we want data we can use later> like creating excel file from the data, or created api, or we analyze data and create a spreadsheet


#STRUCTURED OUTPUTS MEANS:
#THE AI RESPONSE FOLLOWS A FIXED MACHINE-READABLE FORMAT INSTED OF NATURAL LANGUAGE.


# eg:-

# Human Friendly – The movie Interstellar was released in 2014 and directed by Christopher Nolan.

# Machine Friendly:-

# {
#   "title": "Interstellar",
#   "year": 2014,
#   "director": "Christopher Nolan"
# }



#USECASES >> 


# LLMs are not used to “answer questions”.
# They are used inside systems.
# Think like a company (MovieSage 🎬):

# You can store the result directly in MongoDB / SQL

# Title	year	director
# Interstellar	2014	Christopher Nolan

# Impossible with raw paragraph text.




#FLOW>>


# AI → JSON → Backend → API → Frontend

# Without structured output:
# AI breaks the system every time.


#NOW THE POINT IS HOW WE ARE GOING TO GENERATE A STRUCTURED OUTPUT OR WE CAN SAY A PROPER OBJECT

#FOR THAT WE ARE GOING TO USE "Pydantic"

#Pydantic >> is used for creating JSON object



#-----------------------------------------------------------------------------------------------------------------------------------------

# Steps :-

# 1st we have to create a schema –

# A schema is like a school form you have to fill.
# The form already tells you what to write name, age, class, and section.
# You cannot write your favourite cartoon in the age box, and you cannot leave the name empty.
# So the form makes sure everyone gives information in the same way.

# Lets create the Schema




#FOR CREATING SCHEMA WE NEED BASE MODEL CLASS

from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
#IF WE ARE USING BASIC LLM THEN WE CAN WRITE PromptTemplate , BUT IF WE ARE USING THAT ISTSELF IS CHAT MODEL THAN BEFORE PROMPT WE CAN
#WRITE ChatPromptTemplate
import sys
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel

#while creating schema we also make sure that we must have some optional things also like "email" for example form above
from typing import List, Optional


load_dotenv()


#schema for ai >
class Movie(BaseModel):
    title: str
    release_year : Optional[int]
    genre: List[str]
    director : Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str



# Then we have to create a parser –

# The student fills the form, but sometimes students make mistakes.
# Someone may write “ten years old” instead of 10, or write their nickname instead of full name.

# The teacher reads the form and checks:

# Is the name written?
# Is the age a number?
# Did the student write in the correct boxes?


#so we have to create a teacher who will check these
#For checking we have Pydantic Parser(PydanticOutputParser)

from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import PydanticOutputParser
#(that mean we can also use Pydantic inside langchain)

parser = PydanticOutputParser(pydantic_object=Movie)  #now this parser will check if all the info are in write way or not





from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-2603")


#NOW WE ARE NOT USING MESSGAGES LIKE HUMAN_MESSAGE, SYSTEM_MESSAGE, AI_MESSAGE. AS IN PROMPT TEMPELATE WE AUTOMATICALLY GIVES ROLES

# prompt = PromptTemplate.from_template("Say {foo}")
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', """
Extract movie information from the paragraph
         {format_instructions}
"""),
("human", "{paragraph}")
    ]
)



#to put info in {paragraph} > we need to call > ChatPromptTemplate.from_messages





para = int(input("Give your Paragraph :"))




#AFTER GETTING THIS "para" WE WILL GOING TO USE THIS INSIDE {paragraph}

final_prompt = prompt.invoke(
    {"paragraph" : para,
     'format_instructions': parser.get_format_instructions()}
)


response = model.invoke(final_prompt)
#since we are able to inkove this prompt thats way this thing is known as runnable(chains)

##SO response = model.invoke(final_prompt) WILL GIVE MODEL RAW OUTPUTS , BUT TO GET STRUCTURED OUTPUTWE HAVE MAKE RESONSE CONTENT MORE FINE

movie_data = parser.parse(response.content)  #Parse the output of an LLM call to a Pydantic object.


# print(response.content)
print(movie_data.model_dump_json(indent=2))  #print clean JSON output





#outputs >> 

# Give your Paragraph :
# Inception is a mind-bending science fiction thriller directed by Christopher Nolan. Released in 2010,
#  the film stars Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, Tom Hardy, and Ken Watanabe. The story follows Dom Cobb, 
# a skilled thief who specializes in stealing valuable information by entering people's dreams. He is given a challenging mission to 
# plant an idea into someone's mind through a process known as inception. The movie was widely praised for its unique concept, 
# stunning visual effects, complex storytelling, and Hans Zimmer's memorable soundtrack. It is considered one of the most 
# innovative science fiction films of modern cinema.
# ```json
# {
#   "title": "Inception",
#   "release_year": 2010,
#   "genre": ["science fiction", "thriller"],
#   "director": "Christopher Nolan",
#   "cast": [
#     "Leonardo DiCaprio",
#     "Joseph Gordon-Levitt",
#     "Ellen Page",
#     "Tom Hardy",
#     "Ken Watanabe"
#   ],
#   "rating": null,
#   "summary": "The story follows Dom Cobb, a skilled thief who specializes in stealing valuable information by entering people's dreams. He is given a challenging mission to plant an idea into someone's mind through a process known as inception. The movie was widely praised for its unique concept, stunning visual effects, complex storytelling, and Hans Zimmer's memorable soundtrack. It is considered one of the most innovative science fiction films of modern cinema."
# }
# ```


#SO response = model.invoke(final_prompt) WILL GIVE MODEL RAW OUTPUTS , BUT TO GET STRUCTURED OUTPUTWE HAVE MAKE RESONSE CONTENT MORE FINE





# Give your Paragraph :Inception is a mind-bending science fiction thriller directed by Christopher Nolan. Released in 2010, the film starsLeonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, Tom Hardy, and Ken Watanabe. The story follows Dom Cobb, a skilled thief who specializes in stealing valuable information by entering people's dreams. He is given a challenging mission to plant an idea into someone's mind through a process known as inception. The movie was widely praised for its unique concept, stunning visual effects, complex storytelling, and Hans Zimmer's memorable soundtrack. It is considered one of the most innovative science fiction films of modern cinema.
# ```json
# {
#   "title": "Inception",
#   "release_year": 2010,
#   "genre": ["science fiction", "thriller"],
#   "director": "Christopher Nolan",
#   "cast": [
#     "Leonardo DiCaprio",
#     "Joseph Gordon-Levitt",
#     "Ellen Page",
#     "Tom Hardy",
#     "Ken Watanabe"
#   ],
#   "rating": null,
#   "summary": "Dom Cobb, a skilled thief who specializes in stealing valuable information by entering people's dreams, is given a challenging mission to plant an idea into someone's mind through a process known as inception. The movie was widely praised for its unique concept, stunning visual effects, complex storytelling, and Hans Zimmer's memorable soundtrack. It is considered one of the most innovative science fiction films of modern cinema."
# }
# ```
