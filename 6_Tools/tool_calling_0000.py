from dotenv import load_dotenv
load_dotenv()

from rich import print
from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage  #we could have import the message directly but this is another way

#Tool
@tool
def get_text_length(text: str) -> int:
    """Returns the number of character in a given text"""
    return len(text)

#LLM
llm = ChatMistralAI(model = "mistral-small-2506")
llm_with_tool = llm.bind_tools([get_text_length])

# # Step 1: LLM decides tool
# result = llm_with_tool.invoke(
#     "Use the get_text_length tool to find the length of: hello how are you"
# )


# print(result.tool_calls[0])

# print(get_text_length.invoke({'text': 'hello how are you'}))
#______________________________________________________________________________________________________________________________________________________

#OUTPUT >>>
# {'name': 'get_text_length', 'args': {'text': 'hello how are you'}, 'id': 'sIVqlLKJ8', 'type': 'tool_call'}
# 17
#______________________________________________________________________________________________________________________________________________________


#But what if we insted of sending >> {'text': 'hello how are you'}, we send whole dictonary of result.tool_calls[0] >>

# print(get_text_length.invoke({'name': 'get_text_length', 'args': {'text': 'hello how are you'}, 'id': 'sIVqlLKJ8', 'type': 'tool_call'}))


#______________________________________________________________________________________________________________________________________________________
#----------------------------------------------------------------------
#OUTPUT >> if we see this output here we are getting ToolMessage()

#content='17' name='get_text_length' tool_call_id='sIVqlLKJ8'

#----------------------------------------------------------------------

# SO HERE WE ARE GOING TO MAINTAIN THE HISTORY >> BY THIS WE WILL TELL OUR AI THESE ARE MESSAGES >> SystemMessage, HumanMessage, AIMessage, ToolMessage 
#now by combining all these responses and answer, now are model will able to generate perfect answer
#______________________________________________________________________________________________________________________________________________________



#SO TILL NOW WE HAVE CREATED THE TOOL AND BINDED THE TOOL 
#NOW 

message = []
prompt = input("You: ")
query = HumanMessage(prompt) #now query will be return but will be in HumanMessage Object form now
message.append(query)
# print(message)

#OUTPUT >>
#[HumanMessage(content="Return the number of characters in the given text: 'Hello how are you' ", additional_kwargs={}, response_metadata={})]

#______________________________________________________________________________________________________________________________________________________


#Currently our chat history as only HumanMessage, Now we also have to generate AIMessage also and after that we have a tool and we would like to execute that tool
# 
# 
# Till now we have only given query 
# 

result = llm_with_tool.invoke(message)  #it wil be Our AIMessage

# print(result)

#OUTPUT >> 

# AIMessage(
#     content='',
#     additional_kwargs={'tool_calls': [{'id': 'UPdroQYGt', 'type': 'function', 'function': {'name': 'get_text_length', 'arguments': '{"text": "Hello how are you"}'}, 'index': 0}]},
#     response_metadata={
#         'token_usage': {'prompt_tokens': 95, 'total_tokens': 110, 'completion_tokens': 15, 'prompt_tokens_details': {'cached_tokens': 0}, 'service_tier': 'standard'},
#         'model_name': 'mistral-small-2506',
#         'model': 'mistral-small-2506',
#         'finish_reason': 'tool_calls',
#         'model_provider': 'mistralai'
#     },
#     id='lc_run--01a02bd1-4445-7152-aa70-5dd4c9384214-0',
#     tool_calls=[{'name': 'get_text_length', 'args': {'text': 'Hello how are you'}, 'id': 'UPdroQYGt', 'type': 'tool_call'}],
#     invalid_tool_calls=[],
#     usage_metadata={'input_tokens': 95, 'output_tokens': 15, 'total_tokens': 110}
# )

#______________________________________________________________________________________________________________________________________________________


#APPENDING THIS AIMessage also in message

message.append(result)

#print(message)

#NOW IT WILL LOOL LIKE THIS >> OUTPUT >> 

# [              
#     HumanMessage(content="Return the number of characters in the given text: 'Hello how are you' ", additional_kwargs={}, response_metadata={}),
#     AIMessage(
#         content='',
#         additional_kwargs={'tool_calls': [{'id': 'op82aAN00', 'type': 'function', 'function': {'name': 'get_text_length', 'arguments': '{"text": "Hello how are you"}'}, 'index': 0}]},
#         response_metadata={
#             'token_usage': {'prompt_tokens': 95, 'total_tokens': 110, 'completion_tokens': 15, 'prompt_tokens_details': {'cached_tokens': 0}, 'service_tier': 'standard'},
#             'model_name': 'mistral-small-2506',
#             'model': 'mistral-small-2506',
#             'finish_reason': 'tool_calls',
#             'model_provider': 'mistralai'
#         },
#         id='lc_run--01a02bd4-45a2-7033-853f-4409f5a02ba5-0',
#         tool_calls=[{'name': 'get_text_length', 'args': {'text': 'Hello how are you'}, 'id': 'op82aAN00', 'type': 'tool_call'}],
#         invalid_tool_calls=[],
#         usage_metadata={'input_tokens': 95, 'output_tokens': 15, 'total_tokens': 110}
#     )
# ]

#______________________________________________________________________________________________________________________________________________________

#WE NOW ALSO HAVE TO WRITE ONE NEW MESSAGE i.e ToolMessage >>

#we could have multiple tools >> then we not knew that we have to call which tool, for that we have to extract name of the tool 

tools = {
    "get_text_length" : get_text_length
}

if result.tool_calls:
    #print(result.tool_calls[0])  # {'name': 'get_text_length', 'args': {'text': 'Hello how are you'}, 'id': '5SldAiiVY', 'type': 'tool_call'}
    tool_name = result.tool_calls[0]["name"]


    #if we would have send "{'name': 'get_text_length', 'args': {'text': 'Hello how are you'}, 'id': '5SldAiiVY', 'type': 'tool_call'}" this directly to .invoke() , then we would have 
    #got ToolMessage, but for us to get ToolMessage we have to call "get_text_length" function,
    #and if we extract name now then , we are getting string, and we are saving this in tool_name
    #so by calling this tool_name, nothing will happens as our tool i.e "get_text_length" is function, but our tool_name is a string

    #and if we have multiple tool like this then, what to do ?, So For that we will use variable tools = { } as above , so now we extract any tool_name, then after that we can also 
    #call them also, because we have now binding dictonary 
    
    #SO NOW WE CAN DIRECTLY DO>>
    tool_message = tools[tool_name].invoke(result.tool_calls[0]) #so by this we go inside "tool_name" from "tools" dict. and tool_name is "get_text_length", and get_text_length will call tool

    # print(tool_message)  >> #  ToolMessage(content='17', name='get_text_length', tool_call_id='iXIuBRg2T')

    message.append(tool_message)

   # print(message)


    #OUTPUT >> 

#     [
#     HumanMessage(content="Return the number of characters in the given text: 'Hello how are you' ", additional_kwargs={}, response_metadata={}),
#     AIMessage(
#         content='',
#         additional_kwargs={'tool_calls': [{'id': 'CnO4QFkc8', 'type': 'function', 'function': {'name': 'get_text_length', 'arguments': '{"text": "Hello how are you"}'}, 'index': 0}]},
#         response_metadata={
#             'token_usage': {'prompt_tokens': 95, 'total_tokens': 110, 'completion_tokens': 15, 'prompt_tokens_details': {'cached_tokens': 0}, 'service_tier': 'standard'},
#             'model_name': 'mistral-small-2506',
#             'model': 'mistral-small-2506',
#             'finish_reason': 'tool_calls',
#             'model_provider': 'mistralai'
#         },
#         id='lc_run--01a02bfe-eda4-7873-a322-e90b842ec0f6-0',
#         tool_calls=[{'name': 'get_text_length', 'args': {'text': 'Hello how are you'}, 'id': 'CnO4QFkc8', 'type': 'tool_call'}],
#         invalid_tool_calls=[],
#         usage_metadata={'input_tokens': 95, 'output_tokens': 15, 'total_tokens': 110}
#     ),
#     ToolMessage(content='17', name='get_text_length', tool_call_id='CnO4QFkc8')
# ]



#______________________________________________________________________________________________________________________________________________________

#NOW WE WILL SEND ALL THESE TO OUR LLM, NOW OUR LLM, HAVE ALL THE CONTEXT, WHICH ARE HummanMessage, AIMessage and ToolMessage , and 'content' and all other information of all 

#AND WHEN WE INVOKE OUR LLM FINALLY, THEN  >>

result = llm_with_tool.invoke(message)
print(result.content)

#______________________________________________________________________________________________________________________________________________________

# OUTPUT >>

# You: "Return the number of characters in the given text: 'Hello how are you' "
# The number of characters in the text **"Hello how are you"** is **17**.

#______________________________________________________________________________________________________________________________________________________


# BUT STILL THIS IS NOT AN AGENT, WE CAN SAY IT AS HUMAN_IN_THE LOOP, AGENT EXECUTE TOOL OWN BY ITS OWN