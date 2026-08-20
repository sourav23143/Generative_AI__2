from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool

from rich import print  #it have not much use case , but for better way , we are changing our print function , and importing it with rich

#______________________________________________________________________________________________________________________________________________________

#1. CREATING A TOOL 

@tool
def get_text_length(text: str) -> int:
    """Return the number of character in a given text"""
    return len(text)


llm = ChatMistralAI(model = "mistral-small-2506")

#______________________________________________________________________________________________________________________________________________________

#2. TOOL BINDING

#here we are3 going to tell our LLM that at tool exist which you can use when you want to find length

llm_with_tool = llm.bind_tools([get_text_length]) #here we wil provide all the available tool 
#so now we have 2 llm ,technically "llm" and "llm_with_tool" are same, but first llm not have tool and second have 

result = llm.invoke("hello ")

#print(result.content)

#Hello! 😊 How can I assist you today?
 

print(result)