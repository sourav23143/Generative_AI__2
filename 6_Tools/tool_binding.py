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
result2 = llm_with_tool.invoke("hello ")

#print(result.content)

#OUTPUT >> 


#Hello! 😊 How can I assist you today?
 
#______________________________________________________________________________________________________________________________________________________
#removing .content >> 

print(result)
print()
print()
print()
print(result2)

#we are able to print like this as are using > "from rich import print"

# AIMessage(
#     content='Hello! 😊 How can I assist you today?',
#     additional_kwargs={},
#     response_metadata={
#         'token_usage': {
#             'prompt_tokens': 17,
#             'total_tokens': 30,
#             'completion_tokens': 13,
#             'prompt_tokens_details': {'cached_tokens': 0},
#             'service_tier': 'standard'
#         },
#         'model_name': 'mistral-small-2506',
#         'model': 'mistral-small-2506',
#         'finish_reason': 'stop',
#         'model_provider': 'mistralai'
#     },
#     id='lc_run--01a02066-b7b6-7a90-bb0f-2ff9909c2ff5-0',
#     tool_calls=[],
#     invalid_tool_calls=[],
#     usage_metadata={'input_tokens': 17, 'output_tokens': 13, 'total_tokens': 30}
# )


#______________________________________________________________________________________________________________________________________________________