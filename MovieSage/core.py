# AIM >> 1. TAKES A RAW PARAGRAPH ABOUT THE A MOVIE
#         2. EXTRACT IMPORTANT STRUCTURED INFORMATION
#         3. GENEARATES A CLEAN SUMMARY OF THE MOVIE
#         4. STORES IT IN THEIR DATABASES


#ONE WAY > 


from dotenv import load_dotenv
load_dotenv()


from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-2603")

response = model.invoke(""" Inception is a mind-bending science fiction thriller directed by Christopher Nolan. Released in 2010, the film stars Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, 
                        Tom Hardy, and Ken Watanabe. The story follows Dom Cobb, a skilled thief who specializes in stealing valuable information by entering people's dreams. He is given a challenging
                          mission to plant an idea into someone's mind through a process known as inception. The movie was widely praised for its unique concept, stunning visual effects, complex storytelling, '
                          'and Hans Zimmer's memorable soundtrack. It is considered one of the most innovative science fiction films of modern cinema.
CAN YOU PLEASE EXTRACT THE SUMMARY AND THE INFORMATION OF THE MOVIE """)

print(response.content)  



