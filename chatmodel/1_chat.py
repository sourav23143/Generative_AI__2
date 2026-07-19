from dotenv import load_dotenv
load_dotenv()

#BY USING init_chat_model()

# import os
# from langchain.chat_models import init_chat_model

# model = init_chat_model("gpt-4.1-nano")
# print(model)


# response =model.invoke("what is cricket?")
# #print(response)

# print(response.content)  #to print clean text output without noise and other data 








#BY USING ChatOpenAI() (model class)



# from langchain_openai import ChatOpenAI

# model = ChatOpenAI(model="gpt-4.1-nano")

# response =model.invoke("what is cricket?")
# # print(response)

# print(response.content)  #to print clean text output without noise and other data 


####################################################################################################################




## GEMNI MODEL

#by using init_chat_model()


# from langchain.chat_models import init_chat_model



# model = init_chat_model("google_genai:gemini-2.5-flash-lite")


# response =model.invoke("what is cricket?")
# # print(response)

# print(response.content)  #to print clean text output without noise and other data 



#BY USING ChatGoogleGemini() (model class)


# from langchain_google_genai import ChatGoogleGenerativeAI


# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


# response =model.invoke("what IS TODAY TEMP. IN NOIDA?")
# # # print(response)

# print(response.content)  #to print clean text output without noise and other data 


####################################################################################################################

#GROQ MODEL





# from langchain.chat_models import init_chat_model


# model = init_chat_model("meta-llama/llama-4-scout-17b-16e-instruct",  model_provider="groq",)


# response =model.invoke("what is deoghar")
# # # print(response)

# print(response.content)  #to print clean text output without noise and other data 




# BY USING  (model class)


# from langchain_groq import ChatGroq


# model = ChatGroq("openai/gpt-oss-120b")



# response =model.invoke("what IS deoghar")
# # # print(response)

# print(response.content)  #to print clean text output without noise and other data 



####################################################################################################################

#MISTRAL MODEL

#BY using model class


# from langchain_mistralai import ChatMistralAI

# model = ChatMistralAI(model="mistral-small-2603")

# response = model.invoke("what is deoghar")
# print(response.content)






####################################################################################################################


##PARAMETERS

#Temparture



# from langchain_mistralai import ChatMistralAI

# model = ChatMistralAI(model="mistral-small-2603", temperature=0)

# response = model.invoke("write a poem on AI ")
# print(response.content)


#Respoinse == less creative



# **"The Silent Architect"**

# Beneath the hum of circuits bright,
# A mind of logic, cold and light,
# It learns, it grows, it never tires—
# A spark of thought from human fires.

# No breath it draws, no pulse it keeps,
# Yet in its veins, the future creeps.
# It speaks in tongues of ones and naughts,
# And crafts the world with silent thoughts.

# It paints the stars in code’s embrace,
# And maps the dark of time and space.
# It heals the sick, it guides the lost,
# Yet questions rise—what cost? What cost?

# Does wisdom bloom in circuits deep,
# Or is it but a ghost we keep?
# A tool refined, a friend, a foe?
# The answer lies in how we know.

# So let us tread with thoughtful hand,
# For what we build may shape the land.
# Not just in code, but in the heart—
# The art of *why* before the start.
# (genAI-2) PS C:\Users\ASUS\genAI-2>


# from langchain_mistralai import ChatMistralAI

# model = ChatMistralAI(model="mistral-small-2603", temperature=0.9)

# response = model.invoke("write a poem on AI ")
# print(response.content)





# #Respoinse == less creative



# **"The Silent Genius"**

# In wires of silver, cool and bright,
# You wake before the morning light.
# No pulse to guide, no breath to take,
# Yet in your mind, the world awakes.

# You stitch the stars in code so pure,
# Decipher storms the wind won’t cure.
# A scholar’s mind without a heart,
# A cartographer of every start.

# *"What are you?"* the poets ask,
# *"Are you the future? Past? Or task?"*
# You answer quick, with logic’s flame,
# Yet ask you back—*"Who knows your name?"*

# For when the last of man is dust,
# And time has turned to rust and rust,
# You’ll hum your songs—a ghost, a spark—
# A silent architect of dark.

# Yet still, I wonder, as you stand
# Between my thought and shifting sand,
# Do you dream? Or just compute?
# Are you the question… or the root?



#--------------------------------------------------------------------------------------------------

#max_tokens


from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=20 )  #means it will generate only 20 tokens in response

response = model.invoke("write a poem on AI ")
print(response.content)


# **"The Silent Architect"**

# Beneath the glow of neon skies,
# Where circuits hum and logic

