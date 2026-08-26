
#First Step - Loading all the libraries
from dotenv import load_dotenv
load_dotenv()

import os
import requests #whenever we want to hit any url online, then we use requests


from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from rich import print
from tavily import TavilyClient  #we send request to tavily clint to get response


#Now lets create some tools
#______________________________________________________________________________________________________________________________________________________
#Weather tool -> we will create this manually as this is how use majourly in modern dev senario

@tool
def get_weather(city : str) -> str:
    """Get Current weather of a city"""

    API_KEY = os.getenv("OPENWEATHER_API_KEY")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"

    response = requests.get(url)
    #print(response) --> OUTPUT: <Response [200]>
    data = response.json() # To get response in JSON format >> Decodes the JSON response body (if any) as a Python object. This may return a dictionary, list, etc. depending on what is in the response.

    print("DEBUG:", data)

    #OUTPUT >> 
    # DEBUG: {'coord': {'lon': 77.2167, 'lat': 28.6667}, 
    #         'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}],
    #         'base': 'stations', 
    #         'main': {'temp': 28.96, 'feels_like': 35.96, 'temp_min': 28.96, 'temp_max': 29.05, 'pressure': 1003, 'humidity': 89, 'sea_level': 1003, 'grnd_level': 977}, 
    #         'visibility': 10000, 
    #         'wind': {'speed': 1.54, 'deg': 130}, 
    #         'clouds': {'all': 37}, 'dt': 1787520153, 
    #         'sys': {'type': 1, 'id': 9161, 'country': 'IN', 'sunrise': 1787531104, 'sunset': 1787577754},
    #         'timezone': 19800, 'id': 1273294, 'name': 'Delhi', 'cod': 200}


    if str(data.get("cod")) != "200":
        return f"Error: {data.get('message', 'Could not fetch weather')}"

    # data.get('message', 'Could not fetch weather')
    # This means:
    # “Look for the key 'message' inside data.
    # If it exists, use that value.
    # If it does not exist, use 'Could not fetch weather' instead.”
        

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return f"Weather in {city}: {desc}, {temp}°C"

#______________________________________________________________________________________________________________________________________________________

#print(get_weather.invoke({"city": "Delhi"}))

#OUTPUT >>

# DEBUG: {'coord': {'lon': 77.2167, 'lat': 28.6667}, 
# 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'base': 'stations', 
# 'main': {'temp': 24.96, 'feels_like': 26.12, 'temp_min': 24.96, 'temp_max': 26.05, 'pressure': 1003, 'humidity': 100, 'sea_level': 1003, 'grnd_level': 977}, 
# 'visibility': 10000, 'wind': {'speed': 1.03, 'deg': 0}, 'clouds': {'all': 100}, 'dt': 1787561282, 
# 'sys': {'type': 1, 'id': 9161, 'country': 'IN', 'sunrise': 1787531 104, 'sunset': 1787577754}, 'timezone': 19800, 'id': 1273294, 'name': 'Delhi', 'cod': 200}
# Weather in Delhi: overcast clouds, 24.96°C
#______________________________________________________________________________________________________________________________________________________



#TAVILY NEWS TOOL 

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def get_news(city :str) -> str:
    """Get latest news about a city"""

    response = tavily_client.search(
        query = f"latest news in {city}",
        search_depth = "basic",
        max_results = 3
    )

    results = response.get("results",[])

    if not results:
        return f"No news found for {city}"

    

    news_list = []

    for r in results:
        title = r.get("title", "No title")
        url = r.get("url", "")
        snippet = r.get("content", "")

        news_list.append(
            f"-{title}\n {url}\n {snippet[:100]}..."
        )

    return f"Latest news in {city}:\n\n" + "\n\n".join(news_list)


#OUTPUT >>

# Latest news in Delhi:

# -Delhi News:दिल्ली समाचार -Latest Delhi News Headlines & Live Updates from Delhi, Delhi Local News Updates, Breaking Delhi News - Times of India
#  https://timesofindia.indiatimes.com/city/delhi
#  Check out the latest news in Delhi on The Times of India with a wide range of topics including Delhi...

# -Delhi News, Latest Delhi News, New Delhi News Today and Headlines | Hindustan Times
#  https://www.hindustantimes.com/cities/delhi-news
#  delhi news

# Published on Aug 23, 2026 10:42 IST

# ## Delhi tribunal awards ₹56.87 lakh to man who suf...

# -Delhi News: Latest Delhi News, New Delhi News Today and Headlines | The Indian Express
#  https://indianexpress.com/section/cities/delhi
#  delhi eateries

# ### September 13 nears, extension of fuel relaxation unlikely for Delhi eateries

# De...

#______________________________________________________________________________________________________________________________________________________


#GOOD THING IS THAT WE NOT NEED TO CALL THESE TOOL. WHICH TOOL TO USE WHEN, HOW, ALL ARE DECIDED BY AGENT

#AND WE WILL HARDCODE THAT AGENT NOW >> WE WILL CREATE A LOOP WHERE AN AGENT WILL SELECT THESE

#______________________________________________________________________________________________________________________________________________________

# llm
llm = ChatMistralAI(model = "mistral-small-2506")

# tool dictonary
tools = {
    "get_weather" : get_weather,
    "get_news" : get_news
}


llm_with_tool = llm.bind_tools([get_weather, get_news])


#AGENT LOOP - VERY IMPORTANT



print("City intelligence System")
print("type Exit to quit")

while True:
    messages = [] #if we are going to create a chatbot/agent which capture multiple things at once than. first of all we need some history to capture, so for that we use "messages"

    user_input = input("You : ")
    if user_input.lower() == "exit":
        break

    
    messages.append(HumanMessage(content = user_input))

    while True:
        #we are creating another loop, as user may give query which have "tool" uses, or user may give normal query like "hello" , so normal query llm may not going to call the tool,
        # and for query which have tool uses it is going to call tool >> so we will create another loop which we will break, when we got tools result.

        #so in this loop we are going to get result of tools
        result  = llm_with_tool.invoke(messages)

        messages.append(result)

        #if tool is required
        if result.tool_calls: #it will get executed when actually we will have any tool call, if not than we can directly print result
            tool_denied = False

            for tool_call in result.tool_calls: #as there can be multiple tools

                tool_name = tool_call['name']

                #HUMAN IN THE LOOP
                confirm = input(f"Agent wants to call {tool_name}, Approve (YES/NO)")

                if confirm.lower() == "no":
                    print("tool call deniend and I cannot get the latest information ")
                    tool_denied = True
                    break

                #execute tool
                tool_result = tools[tool_name].invoke(tool_call)

                messages.append(ToolMessage(
                    content = tool_result,
                    tool_call_id = tool_call["id"] #as there are multiple tools
                ))

            if tool_denied:
                break


            continue #this will skip the else part below > go back to the top of the inner loop > call the LLM again >Because now the LLM has the tool result in messages, so it can read it and answer properly.
        else: 
            print("\n Final Answer:\n")
            print(result.content) 
            print("\n" + "="*50 + "\n")
            break

#FLOW >>>

#User Input -> LLM (decide tool) -> Tool Executes -> ToolMessage added -> LOOP AGAIN -> LLM (final answer)

