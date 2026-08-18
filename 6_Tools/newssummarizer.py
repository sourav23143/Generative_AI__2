#we will create an ageent that will search AI news and summarize those


from dotenv import load_dotenv()
load_dotenv()

from langchain_community.tools.tavily_search import TavilySearchResults

#for summarization we need LLM Model also >
from langchain_mistralai import ChatMistralAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


#when are we are going to use tools, they are also Runnable , means we can invoke those also  

search_tools = TavilySearchResults(max_result = 5)

llm = ChatMistralAI("mistral-small-2506")


prompt = ChatPromptTemplate.from_template(  #we are using .from_template(), instead of .from_messages(), as we not wnat to define much roles here

)
