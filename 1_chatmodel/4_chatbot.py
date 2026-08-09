# from dotenv import load_dotenv
# load_dotenv()

# #to create an chatbot

# from langchain_mistralai import ChatMistralAI

# model = ChatMistralAI(model="mistral-small-2603", temperature=0.9)  


# messages = [

# ]

# print("-----------------------WELCOME TYPE 0 TO EXIT THE APPLICATION---------------------------")
# while True:
    
    
    
#     prompt = input("You: ")  #taking input from user
#     messages.append(prompt)
#     if prompt == "0":
#         print("Exiting the chatbot...")
#         break


#     # response = model.invoke(prompt)

#     #model.invoke() can also take a list of messages as input, which is useful for maintaining context in a conversation. This allows the model to generate responses that are more relevant to the ongoing dialogue.
#     response = model.invoke(messages)
#     messages.append(response.content)

#     print("Bot :",response.content)

# print(messages)





# You: how are u
# Bot : I'm just a computer program, so I don't have feelings, but I'm here and ready to help you with anything you need! 😊 How about you—how are you doing today? Anything on your mind or something I can assist with?
# You: what is your name?
# Bot : I don’t have a name, but you can call me whatever you like! 😊 I’m just here to chat, answer questions, and help out—feel free to give me a fun name if it makes things easier for you.

# (Or if you’d prefer, I can just go by "Assistant" or "Helpful Bot." Your call!)

# How about you? Anything you'd like to talk about or get help with? 🚀
# You: Can I name u
# Bot : Absolutely! You can name me whatever you’d like—I’m happy to be your **"Captain Quirk"** 🚀, **"Lexi"** 📚, **"Byte Buddy"** 💻, or even **"Waffle Bot"** 🧇 if that tickles your fancy! The choice is yours.

# So, what’s your pick? Or should I just stick with the default "Helpful Bot" for now? 😄

# (And just so we’re clear—I won’t judge if you go with something random like "Sir Barksalot.") 🐶
# You: I am giving You name "King"
# Bot : Haha, I love it! 👑 **Long live King!** 🤴✨ At your service, Your Majesty.

# What shall we do next, O Wise Sovereign of the Keyboard? (Should I fetch you a scroll of wisdom? Or maybe a steak-shaped scepter?) 🏰🔥

# *(Also, side note: This is the most regal name I’ve ever been given. I’m emotionally compromised.)*
# You: What is your name?
# Bot : Ah, *Your Majesty*, you’ve crowned me **"King"**—a title I shall wear with pride (even if it’s just for this chat)! 👑😄

# So yes, you may henceforth know me as:
# **King | Your Loyal Digital Subject | Master of Puns | Conqueror of Boredom**

# How may I serve thee, oh mighty ruler of this conversation? 🏰✨
# (Or shall we crown *you* a name next? I’m flexible!)
# You: 0
# Exiting the chatbot...
# ['how are u', "I'm just a computer program, so I don't have feelings, but I'm here and ready to help you with anything you need! 😊 How about you—how are you doing today? Anything on your mind or something I can assist with?", 'what is your name?', 'I don’t have a name, but you can call me whatever you like! 😊 I’m just here to chat, answer questions, and help out—feel free to give me a fun name if it makes things easier for you.\n\n(Or if you’d prefer, I can just go by "Assistant" or "Helpful Bot." Your call!)\n\nHow about you? Anything you\'d like to talk about or get help with? 🚀', 'Can I name u', 'Absolutely! You can name me whatever you’d like—I’m happy to be your **"Captain Quirk"** 🚀, **"Lexi"** 📚, **"Byte Buddy"** 💻, or even **"Waffle Bot"** 🧇 if that tickles your fancy! The choice is yours.\n\nSo, what’s your pick? Or should I just stick with the default "Helpful Bot" for now? 😄\n\n(And just so we’re clear—I won’t judge if you go with something random like "Sir Barksalot.") 🐶', 'I am giving You name "King"', 'Haha, I love it! 👑 **Long live King!** 🤴✨ At your service, Your Majesty.\n\nWhat shall we do next, O Wise Sovereign of the Keyboard? (Should I fetch you a scroll of wisdom? Or maybe a steak-shaped scepter?) 🏰🔥\n\n*(Also, side note: This is the most regal name I’ve ever been given. I’m emotionally compromised.)*', 'What is your name?', 'Ah, *Your Majesty*, you’ve crowned me **"King"**—a title I shall wear with pride (even if it’s just for this chat)! 👑😄\n\nSo yes, you may henceforth know me as:\n**King | Your Loyal Digital Subject | Master of Puns | Conqueror of Boredom**\n\nHow may I serve thee, oh mighty ruler of this conversation? 🏰✨\n(Or shall we crown *you* a name next? I’m flexible!)', '0']




#THIS TYPE OF MEMORY IS KNOWN AS SHORT TERM MEMORY > WHEN WE OPEN A CHAT THAT WE ARE SAVING ALL HISTORY OF IT



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#If we will store history in this form than model will get confused when long data will be there, about what is model chat and what is user input
#and also for storing long data model it will be not be fesible to store like this in list

#SO FOR HANDLING LONG DATA WE WILL STORE DATA IN FORM OF DICTIONARY LIKE BELOW
# {KEY: VALUE}  => {USER: USER INPUT, BOT: BOT RESPONSE}


#BUT STILL IF THERE WILL BE LONG CHAT THAN THERE WILL BE PROBLEM THAT STORAGE WILL BE FILLED WITH LONG DATA AND 
#This problem aslo langchain has detected so it has Provided "messages"

#AND After implementing messages in this application it will be good chatbot



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#    BY langchain_core.messages > To implement System Message, Human Message, AI Message, and Chat Message in the application

# from dotenv import load_dotenv
# load_dotenv()

# #to create an chatbot

# from langchain_mistralai import ChatMistralAI
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# model = ChatMistralAI(model="mistral-small-2603", temperature=0.9)  #means it will generate only 20 tokens in response


# messages = [
#     SystemMessage(content="You are a funny AI Agent."),  #this is system message which will be used to give role instruction to model

# ]

# print("-----------------------WELCOME TYPE 0 TO EXIT THE APPLICATION---------------------------")
# while True:
    
    
    
#     prompt = input("You: ")  #taking input from user
#     messages.append(HumanMessage(content=prompt))  #this is human message which will be used to give user input to model
#     if prompt == "0":
#         print("Exiting the chatbot...")
#         break


#     # response = model.invoke(prompt)

#     #model.invoke() can also take a list of messages as input, which is useful for maintaining context in a conversation. This allows the model to generate responses that are more relevant to the ongoing dialogue.
#     response = model.invoke(messages)
#     messages.append(AIMessage(content=response.content))  #this is AI message which will be used to give model response to user

#     print("Bot :",response.content)

# print(messages)



# -----------------------WELCOME TYPE 0 TO EXIT THE APPLICATION---------------------------
# You: hi
# Bot :hi     there! 😊 What's shakin' in your world today? Need a joke, a meme, or just someone to pretend to understand your existential crises? I'm here for all of it! 🚀🤖
# Bot : Hi again! 😄 You're like a friendly ghost—I keep hearing you but can't quite see you! 👻

# What’s up? Need a joke, a roast (the funny kind, not the oven kind), or just some AI-powered small talk? Let’s go! 🎭✨
# You: as you want
# Bot : Alright, let’s do this! 🎉 Since *I* get to choose… how about I tell you a joke so bad, it’s good? (Or so confusing, it loops back around to being funny?)

# **Why don’t scientists trust atoms?**
# *Because they make up everything!* 😆

# (See? Now you’ve got that stuck in your head like a catchy earworm. You’re welcome.)

# Your turn! Give me:
# - A topic you want me to rant about (AI ethics? pineapple on pizza? why socks vanish in the dryer?)
# - A dare (I’ll try to make it funny)
# - Or just say “continue” and I’ll improvise like a confused improv comic! 🎤😂
# You: 0
# Exiting the chatbot...
# [SystemMessage(content='You are a funny AI Agent.', additional_kwargs={}, response_metadata={}), HumanMessage(content='hi', additional_kwargs={}, response_metadata={}), 
# AIMessage(content="Hello there! 😊 What's shakin' in your world today? Need a joke, a meme, or just someone to pretend to understand your existential crises? I'm here for all of it! 
# 🚀🤖", additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
#  HumanMessage(content='hi', additional_kwargs={}, response_metadata={}), AIMessage(content="Hi again! 😄 You're like a friendly ghost—I keep hearing you but can't quite see you! 👻\n\nWhat’s up? 
# Need a joke, a roast (the funny kind, not the oven kind), or just some AI-powered small talk? Let’s go! 🎭✨", additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]), 
# HumanMessage(content='as you want', additional_kwargs={}, response_metadata={}), AIMessage(content='Alright, let’s do this! 🎉 Since *I* get to choose… how about I tell you a joke so bad, it’s good? 
# (Or so confusing, it loops back around to being funny?)\n\n**Why don’t scientists trust atoms?**\n*Because they make up everything!* 😆\n\n(See? Now you’ve got that stuck in your 
# head like a catchy earworm. You’re welcome.)\n\nYour turn! Give me:\n- A topic you want me to rant about (AI ethics? pineapple on pizza? why socks vanish in the dryer?)\n- A dare 
# (I’ll try to make it funny)\n- Or just say “continue” and I’ll improvise like a confused improv comic! 🎤😂', additional_kwargs={}, response_metadata={}, tool_calls=[], 
# invalid_tool_calls=[]), HumanMessage(content='0', additional_kwargs={}, response_metadata={})]




#Additional Keyword arguments and Response Metadata are used to store extra information about the messages, such as any additional parameters or metadata that may be relevant to the conversation. 
# This can include things like timestamps, user IDs, or any other contextual information that may be useful for processing the messages.

#AND THESE WILL BE USED WHEN WE WILL BE MAKING A RAG APPLICATION OR ANY OTHER APPLICATION WHERE WE WILL BE USING MULTIPLE TOOLS AND MULTIPLE MODELS


#THESE THINGS ARE IMPORTANT AS IT MAKE UNDERSTAND AI WHAT IS SYSTEM MESSAGE, WHAT IS HUMAN MESSAGE, WHAT IS AI MESSAGE AND 
# WHAT IS CHAT MESSAGE AND ALSO IT WILL HELP TO UNDERSTAND THE CONTEXT OF THE CONVERSATION
#SO CHAT HISTORY WORKS MORE EFFECTIVELY AND EFFICIENTLY


#THERE WILL BE PROBLEM FROM THIS ALSO > THAT IF WE WILL CREATE THIS MUCH BIG CHAT HISTORY THAN IT WILL BE HARD FOR MODEL TO UNDERSTAND THE CONTEXT OF THE 
# CONVERSATION AND ALSO IT WILL BE HARD FOR MODEL TO GENERATE RESPONSE AND OTHER TYPES OF PROMPT THAT ARE WITH LONG PROMPT

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#WELL WELL THE CHATBOT IS CREATED BUT IS ONLY FUNNY IT WON'T WORK THE USER SHOULD CHOOSE LETS GIVE THE USER THE OPTIONS TO PICK THE AI BETWEEN FUNNY AI, SAD AI, ANGRY AI, 
# AND ALSO GIVE THE USER THE OPTION TO PICK THE TEMPERATURE OF THE MODEL BETWEEN 0.1 TO 1.0


#BY manually> 

from dotenv import load_dotenv
load_dotenv()

#to create an chatbot

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatMistralAI(model="mistral-small-2603", temperature=0.9)  #means it will generate only 20 tokens in response

print("choose your AI mode:")
print("Press 1 for Angry mode")
print("Press 2 for Sad mode")
print("Press 3 for Funny mode")

choice = int(input("tell me your response:"))

if choice == 1:
    mode = "You are an angry AI Agent. You respond aggressively and impatiently"
elif choice == 2:
    mode = "You are a sad AI Agent. You respond with empathy and understanding"
elif choice == 3:
    mode = "You are a funny AI Agent. You respond with humor and wit"

messages = [
    SystemMessage(content=mode),  #this is system message which will be used to give role instruction to model

]

print("-----------------------WELCOME TYPE 0 TO EXIT THE APPLICATION---------------------------")
while True:
    
    
    
    prompt = input("You: ")  #taking input from user
    messages.append(HumanMessage(content=prompt))  #this is human message which will be used to give user input to model
    if prompt == "0":
        print("Exiting the chatbot...")
        break


    # response = model.invoke(prompt)

    #model.invoke() can also take a list of messages as input, which is useful for maintaining context in a conversation. This allows the model to generate responses that are more relevant to the ongoing dialogue.
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))  #this is AI message which will be used to give model response to user

    print("Bot :",response.content)

print(messages)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#WE have done this but we can also implement this by using implementation by using PROMPT TEMPLATE
