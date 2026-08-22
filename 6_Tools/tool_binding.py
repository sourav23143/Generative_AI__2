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

#OUTPUT >> 

# AIMessage(
#     content='Hello! 😊 How can I assist you today? Let me know what you need help with!',
#     additional_kwargs={},
#     response_metadata={
#         'token_usage': {'prompt_tokens': 17, 'total_tokens': 39, 'completion_tokens': 22, 'prompt_tokens_details': {'cached_tokens': 0}, 'service_tier': 'standard'},
#         'model_name': 'mistral-small-2506',
#         'model': 'mistral-small-2506',
#         'finish_reason': 'stop',
#         'model_provider': 'mistralai'
#     },
#     id='lc_run--01a0208c-9eff-7a83-bc3b-20613c90147c-0',
#     tool_calls=[],
#     invalid_tool_calls=[],
#     usage_metadata={'input_tokens': 17, 'output_tokens': 22, 'total_tokens': 39}
# )



# AIMessage(
#     content='Hello! How can I assist you today? 😊',
#     additional_kwargs={},
#     response_metadata={
#         'token_usage': {'prompt_tokens': 80, 'total_tokens': 93, 'completion_tokens': 13, 'prompt_tokens_details': {'cached_tokens': 0}, 'service_tier': 'standard'},
#         'model_name': 'mistral-small-2506',
#         'model': 'mistral-small-2506',
#         'finish_reason': 'stop',
#         'model_provider': 'mistralai'
#     },
#     id='lc_run--01a0208c-a113-76e2-b622-8429d7896bdc-0',
#     tool_calls=[],
#     invalid_tool_calls=[],
#     usage_metadata={'input_tokens': 80, 'output_tokens': 13, 'total_tokens': 93}
# )
#______________________________________________________________________________________________________________________________________________________


# IF WE SEE OUTPUT , WE SEEN IN 1ST LLM OUTPUT "input_tokens" WHICH IS OF WITHOUT TOOL BINDING IS 17, WHILE NEXT ONE WHICH IS WITH BINDING TOOL IS 80 , 
#AS WHEN WE BIND ANY TOOL WITH LLM, THEN THAT TOOL "META DATA", "DOC_STRING" WRITTEN INSIDE THAT TOOL , ALL GOES TO INPUT TOKEN FROM STARTING ONLY. ALTHOUGH RESPONSE 
#OF BOTH ARE SAME >> BUT HERE DUE TO BINDING OUR INPUT TOKEN GETS INCREASE


#ALSO IF WE SE PROMPT TOKEN THEN >> IN FIRST ONE IS [prompt_tokens': 17,], WHILE FOR NEST ONE IS [prompt_tokens': 80]


#ALSO IF WE SEE >>

# tool_calls=[],
# invalid_tool_calls=[],

#WRITEN HERE IS VACANT LIST >> MEANS TILL NOW WE BINDED THE TOOL, BUT NOT CALLED ANY ONE

#______________________________________________________________________________________________________________________________________________________

#SO WE HAVE DONE 2 THINGS TILL NOW >> WE HAVE CREATED THE TOOL, BUT NOT BINDED THE TOOL >> SO
#NOW LLM KNOW WHAT TOOL ARE AVAILABLE , WHAT THEY DO, AND WHEN TO USE THEM 

#FOR (WHEN TO USE THEM) >> TOOL CALLING

#SUPPOSE WE HAVE BINDED 5 TOOLS TO OUR LLM, THEN FROM THOSE 5 TOOL , OUR LLM WILL CHOOSE 1 OE 2 TOOL DEPENDING UPON WORK

#______________________________________________________________________________________________________________________________________________________



   