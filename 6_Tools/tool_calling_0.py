from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
# from langchain_core.messages import HummanMessage
from rich import print

#----------------------------------------------------------------------
#1. Creating tool 
#----------------------------------------------------------------------

@tool
def get_text_length(text: str) -> int:
    """Returns the number of character in a given text"""
    return len(text)

#LLM
llm = ChatMistralAI(model = "mistral-small-2506")

#----------------------------------------------------------------------
#2. Binding the tool 
#----------------------------------------------------------------------

llm_with_tool = llm.bind_tools([get_text_length])

#----------------------------------------------------------------------
#3. Tool Calling
#----------------------------------------------------------------------

result = llm_with_tool.invoke("Returns the number of character in a given text: 'hello how are you' ")

if result.tool_calls:
    tool_call =result.tool_calls[0] #capturing the tool
   

tool_name = tool_call["name"]
tool_args = tool_call["args"]

#----------------------------------------------------------------------
#4. Executing the tool
#----------------------------------------------------------------------

tool_result = get_text_length.invoke(tool_args) 

#----------------------------------------------------------------------
#5. Sending result back to LLM
#----------------------------------------------------------------------

final_response = llm_with_tool.invoke(f"the length of text is {tool_result}")

print(final_response)


#OUTPUT >> 

# AIMessage(
#     content="The text you're referring to has **17 characters**.\n\nWould you like me to verify this using the `get_text_length` function? If so, please provide the text.",
#     additional_kwargs={},
#     response_metadata={
#         'token_usage': {'prompt_tokens': 86, 'total_tokens': 123, 'completion_tokens': 37, 'prompt_tokens_details': {'cached_tokens': 0}, 'service_tier': 'standard'},
#         'model_name': 'mistral-small-2506',
#         'model': 'mistral-small-2506',
#         'finish_reason': 'stop',
#         'model_provider': 'mistralai'
#     },
#     id='lc_run--01a02b89-f503-7ec1-a7cb-1fc713d02767-0',
#     tool_calls=[],
#     invalid_tool_calls=[],
#     usage_metadata={'input_tokens': 86, 'output_tokens': 37, 'total_tokens': 123}
# )