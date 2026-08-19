
from langchain.tools import tool

# we create python function in so good way that we can make that a tool

#for example >>

#we are going  to create a function in which we will greet peoples

@tool  # decorator for creating tool -> # decorator is a function that takes another function as an argument, extends or modifies its behavior, and returns a new function without changing the original function's source code
def get_greeting(name: str) -> str:
    """Generate a greeting for a user"""
    #genrally when we create a function, then we also write a doc string inside it 
    #doc string work is simple to tell what  is this function going to do.
    #doc string is written, so suppose tommrow if LLM have to intract with tool than it must knew what this tool does/usecase of this tool
     
    return f"Hello {name}, Welcome to the AI world"

#SO NOW THIS IS A GREETING FUNCTION, 

#AND TO CONVERT FUNTION INTO TOOLS, WE HAVE A LIBRARY LANGCHAIN >> from langchain.tools import tools -> apply tools decorator to our function to make this function tool
#now we can use this tool with out LLM


#As we this is tool and, this also a runnable, so >>
result = get_greeting.invoke({"name" :"sourav"})
print(result)

#it also  have these features >> 
print(get_greeting.name)
print(get_greeting.description)
print(get_greeting.args)


#THESE SAME THING ALSO EXITS IN INBUILT TOOLS ALSO 

#OUTPUT >>


# Hello sourav, Welcome to the AI world
# get_greeting
# Generate a greeting for a user
# {'name': {'title': 'Name', 'type': 'string'}}