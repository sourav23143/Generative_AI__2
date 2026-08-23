from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
# from langchain_core.messages import HummanMessage
from rich import print


#1. creating a tool 

@tool
def get_text_length(text: str) -> int:
    """Returns the number of character in a given text"""
    return len(text)




llm = ChatMistralAI(model = "mistral-small-2506")

llm_with_tool = llm.bind_tools([get_text_length])


result = llm.invoke("Returns the number of character in a given text: 'hello how are you' ")
result2 = llm_with_tool.invoke("Returns the number of character in a given text: 'hello how are you' ")

#NOW WE HAVE GIVEN BOTH LLM SAME INPUT >> 


# print(result)
# print()
# print()
# print()
# print(result2)



#OUTPUT >> 

# AIMessage(
#     content="To find the number of characters in the given text `'hello how are you'`, you can count each character, including the spaces between the words.\n\nHere's the breakdown:\n\n-
# 'h', 'e', 'l', 'l', 'o', ' ', 'h', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u'\n\nTotal characters: **17**\n\nSo, the number of characters in the text `'hello how are you'` is 
# **17**.",
#     additional_kwargs={},
#     response_metadata={
#         'token_usage': {'prompt_tokens': 32, 'total_tokens': 144, 'completion_tokens': 112, 'prompt_tokens_details': {'cached_tokens': 0}, 'service_tier': 'standard'},
#         'model_name': 'mistral-small-2506',
#         'model': 'mistral-small-2506',
#         'finish_reason': 'stop',
#         'model_provider': 'mistralai'
#     },
#     id='lc_run--01a02ad0-b1b5-70c3-9506-6713e91a3c7f-0',
#     tool_calls=[],
#     invalid_tool_calls=[],
#     usage_metadata={'input_tokens': 32, 'output_tokens': 112, 'total_tokens': 144}
# )



# AIMessage(
#     content='',
#     additional_kwargs={'tool_calls': [{'id': '1VVoolcLJ', 'type': 'function', 'function': {'name': 'get_text_length', 'arguments': '{"text": "hello how are you"}'}, 'index': 0}]},
#     response_metadata={
#         'token_usage': {'prompt_tokens': 95, 'total_tokens': 110, 'completion_tokens': 15, 'prompt_tokens_details': {'cached_tokens': 0}, 'service_tier': 'standard'},
#         'model_name': 'mistral-small-2506',
#         'model': 'mistral-small-2506',
#         'finish_reason': 'tool_calls',
#         'model_provider': 'mistralai'
#     },
#     id='lc_run--01a02ad0-b7bf-7d43-9428-87c05d393979-0',
#     tool_calls=[{'name': 'get_text_length', 'args': {'text': 'hello how are you'}, 'id': '1VVoolcLJ', 'type': 'tool_call'}],
#     invalid_tool_calls=[],
#     usage_metadata={'input_tokens': 95, 'output_tokens': 15, 'total_tokens': 110}
# )


#______________________________________________________________________________________________________________________________________________________


#NOW IF WE SEE OUTPUT OF 2ND LLM i.e (llm_with_tool), its content ='' is empty,>> THIS IS SINCE THIS LLM IS SUGGESTING US TO DO THIS TASK BY TOOL_CALLING, WE CAN SEE THAT IN "additional_kwargs">> 

#additional_kwargs={'tool_calls': [{'id': '1VVoolcLJ', 'type': 'function', 'function': {'name': 'get_text_length', 'arguments': '{"text": "hello how are you"}'}, 'index': 0}]},

#it is suggesting to call tool name "get_text_length" function with argument : '{"text": "hello how are you"}

#----------------------------------------------------------------------
#IMP: TILL NOW OUR AI HAVE NOT CALLED TOOL ITS ONLY GIVING US SUGGESTION, AND FOR THAT WE HAVE TO CALL TOOL 
#----------------------------------------------------------------------


#IF WE SEE output_token OF 1ST = 122 BUT FOR 2ND ONE = 15(THIS 15 COMMING AFTER ALSO IT HAVE NOTHING IN CONTENT AS  IT IS COMMING DUE TO "additional_kwargs" )  


#IN TOOL CALLING LLM CHOOSES THE  TOOL TO USE THEN
#CHOOSE SINCE >> "LLM AFTER COMPAREING "DOC_STRING" OUT OF ALL TOOLS WITH OUR "PROMPT" AND GIVE SUGGESTION THAT U CAN USE THIS TOOL


#FOR EXECUTION WE HAVE TO EXECUTE TOOL ("TOOL EXECUTION")
#______________________________________________________________________________________________________________________________________________________



#print(result2.tool_calls)  #to see tool calls

#OUTPUT >>

#[{'name': 'get_text_length', 'args': {'text': 'hello how are you'}, 'id': 'F3Bn1SZ0v', 'type': 'tool_call'}]

#print(result2.tool_calls[0]) #to see 0th tool call if multiple elements are present

#OUTPUT >>
#{'name': 'get_text_length', 'args': {'text': 'hello how are you'}, 'id': 'F3Bn1SZ0v', 'type': 'tool_call'}


#______________________________________________________________________________________________________________________________________________________

#insted of printing we can do >>

if result2.tool_calls:  #means if tool_calls = True
    tool_call = result2.tool_calls[0] #capturing tool call


#----------------------------------------------------------------------
#after capturing >> we have to extract "tool_name", "arguments"
#----------------------------------------------------------------------

tool_name = tool_call['name']
tool_args = tool_call['args']


print(tool_name)
print(tool_args)

#output >> 

# get_text_length
# {'text': 'hello how are you'}