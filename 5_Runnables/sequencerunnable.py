# from dotenv import load_dotenv
# load_dotenv()


# from langchain_mistralai import ChatMistralAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# #1. Prompt Template
# prompt = ChatPromptTemplate.from_template(
#     "Explain {topic} in simple words"
# )


# #2. Model 
# model = ChatMistralAI(model = "mistral-small-2506")

# #3. Output Parser

# # whenever we invoke llm then we get output, that response may be not so good like (llm has written full text ast once) then to represent that in structured way we 
# #use StrOutputParser
# parser = StrOutputParser()


# #step by step manual 
# formatted_prompt = prompt.format_messages(topic = "Machine Learning")

# #call the model manually
# response = model.invoke(formatted_prompt)

# #parse the output manually
# final_output = parser.parse(response.content)

# print(final_output)



#OUTPUT >> 

# **Machine Learning (ML)** is like teaching a computer to learn from experience—just like how you learn from mistakes or practice.

# ### Simple Explanation:
# Imagine you teach a child to recognize cats by showing them many pictures of cats and dogs. After seeing enough examples, the child can tell the difference between a cat and a dog on their own. **Machine Learning does the same thing with computers**—it learns patterns from data so it can make predictions or decisions without being explicitly programmed.

# ### Key Ideas:
# 1. **Learn from Data** – Instead of writing rules (like "if ears are pointy, it's a cat"), the computer finds patterns in data.
# 2. **Improves Over Time** – The more data it sees, the better it gets (like practicing a skill).
# 3. **Types of ML**:
#    - **Supervised LeLearning** (Finding hidden patterns, e.g., grouping similar customers).
#    - **Reinforcementarning** (Teaching with labeled examples, e.g., "this is a cat").
#    - **Unsupervised  Learning** (Learning by trial and error, like a game AI).

# ### Real-World Examples:
# - **Spam Filters** – Learns which emails are spam based on past examples.
# - **Recommendations** – Netflix or Spotify suggest shows/music based on what you’ve liked before.
# - **Self-Driving Cars** – Learns to recognize pedestrians, traffic signs, etc.

# ### Why It’s Useful:
# ML automates tasks that would take humans too long, like analyzing big data, detecting fraud, or even diagnosing diseases from medical images.

# **In short:** Machine Learning is about teaching computers to learn from data and make smart decisions—just like how humans learn from experience!

# Would you like a deeper dive into any specific part? 😊




#WE ARE RUNNING ALL THESE THINGS MANUALLY, WE WOULD HAVE USED CAHINS HERE 

#earlier first we have to import 
#from langchain.chains import LLMChains

#and when we get this LLMchains function, then we have to call that 
# LLMChains(model, prompt, parser)


# we had multiple chains like LLMChains , these SequentialChain, ParllelChains, , there are multiple type of chains like this


#SO INSTEAD OF THESE CHAINS A NEW CONCEPT GOT INTRODUCE i.e RUNNABLES


from dotenv import load_dotenv
load_dotenv()


from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#1. Prompt Template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)


#2. Model 
model = ChatMistralAI(model = "mistral-small-2506")

#3. Output Parser

# whenever we invoke llm then we get output, that response may be not so good like (llm has written full text ast once) then to represent that in structured way we 
#use StrOutputParser
parser = StrOutputParser()


#NOW IN RUNNABLE CONCEPT ALL THESE promopt, model , parser all are Runnables
#TO CONNECT EACH AND EVERY RUNNABLE, WE WILL CREATE A VARIABLE AND NAME IT CHAIN

chain = prompt | model | parser

#SEQUENCE RUNNABLE MEANS IT GO BY SEQUENCE LIKE FIRST INNPUT GOES to "prompt", then "model", then "parser" , then output comes

result = chain.invoke("Machine Learning")
print(result)

#SEQUENCE RUNNABLE >> THIS IS VERY FIRST TYPE  SEQUENCE RUNNABLE, WHERE AFTER ONE ANOTHER SEQUENCE HAPPENS , SO WE ARE ABLE TO CONNECT MULTIPLE SEQUENCE DIRECTLY



# **Machine Learning (ML)** is like teaching a computer to learn from experience—just like how you learn from mistakes and practice.

# ### Simple Explanation:
# Instead of writing detailed instructions (like a traditional program), you give the computer **data** and let it **find patterns** on its own.

# ### Example:
# Imagine teaching a kid to recognize cats:
# - You show them **1000 cat pictures** (data).
# - Instead of explaining every feature (like pointy ears or whiskers), you let the kid **observe similarities** between the images.
# - Over time, the kid "learns" what a cat looks like and can identify new cat pictures correctly.

# ### How ML Works:
# 1. **Training**: Feed the computer lots of data (e.g., cat images, speech recordings, or sales numbers).
# 2. **Learning**: The computer finds patterns (e.g., "cats have whiskers" or "spam emails often contain certain words").
# 3. **Prediction**: When you show new data, the computer makes guesses (e.g., "This is a cat" or "This email is spam").

# ### Common Uses:
# - **Recommendations**: Netflix suggesting shows you might like.
# - **Spam Filters**: Gmail blocking spam emails.
# - **Voice Assistants**: Siri/Alexa understanding your voice.
# - **Self-Driving Cars**: Recognizing pedestrians and road signs.

# ### Key Idea:
# ML helps computers improve at tasks **without being explicitly programmed** for every step—just like humans learn from experience!

# Would you like an example with code or a real-world analogy? 😊