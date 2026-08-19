#we will create an ageent that will search AI news and summarize those

#HERE WE WILL USE BUILT IN TOOL >>


from dotenv import load_dotenv
load_dotenv()

from langchain_community.tools.tavily_search import TavilySearchResults

#for summarization we need LLM Model also >
from langchain_mistralai import ChatMistralAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


#when are we are going to use tools, they are also Runnable , means we can invoke those also  

search_tool = TavilySearchResults(max_results = 5) #max_results=5 = “give me the top 5 results”

llm = ChatMistralAI(model = "mistral-small-2506")


prompt = ChatPromptTemplate.from_template(  #we are using .from_template(), instead of .from_messages(), as we not wnat to define much roles here
    """
You are a helpul assistant
summarize the following news into clear bullet points
{news}
"""

)


#Now to create our Chains Varible and in that we will connect Runnables

chain = prompt | llm | StrOutputParser()


#after this we have to get News , and for that we have to create a Query(what we want to send to TavilySearch)
#so 1st we will feed Query to search_tools

news_result = search_tool.run("Latest AI news of 2026") #Run the tool.

#this news_result is also a runnable so we can integrate it at front of chain,then also it will work 

#but we will do like >>
result = chain.invoke({"news" : news_result}) 

print(result)


#OUTPUT >> 



# ### **AI News Summary (2026) – Key Highlights**

# #### **Google’s AI Advancements (May 2026)**
# - **Gemini Era Launch**:
#   - Introduced **Gemini 3.5** (agentic AI for coding & reasoning) and **Gemini Omni** (combining reasoning + creativity).
#   - Launched **Android Halo**—a dashboard to track AI agents’ progress on mobile devices.
# - **New Tools & Integrations**:
#   - **Google Health app** & **Fitbit Air** for wellness.
#   - **Universal Cart**—a unified shopping hub across Google services (Search, YouTube, Gmail, etc.).
#   - **Gemini for Science**—AI tools for scientific research (e.g., AlphaEvolve for logistics, chip design, and climate challenges).
#   - **Quantum AI Initiative**—applying AI + quantum computing to life sciences.

# #### **Major AI Funding & Valuations (2026)**
# - **OpenAI**: Raised **$110B** at an **$840B** valuation.
# - **Anthropic**: Raised **$30B** at a **$380B** valuation.
# - **Waymo**: Secured **$16B** for autonomous vehicles.
# - **xAI**: Raised **$20B** before merging with SpaceX (**$250B** valuation).
# - **AI startups** now attract **33% of all venture capital funding**.

# #### **AI Model Wars & Competition**
# - **OpenAI’s GPT-5.4** (March 2026):
#   - **1.05M-token context window**, **33% fewer errors** than GPT-5.2.
# - **Google’s Gemini 3.1 Pro**:
#   - Dominates **13/16 benchmarks**, leads in **context awareness** (integrates Gmail, Photos, YouTube, etc.).
# - **Anthropic’s Claude Opus 4.6**:
#   - Excels in **coding (80.8% on SWE-bench)** and **long-context analysis (1M tokens)**.
# - **Meta’s Muse Glimmer** (August 2026):
#   - Brings **local AI agents** to consumer GPUs.

# #### **AI Industry Shifts & Trends**
# - **Agentic AI in Production**:
#   - AI agents now **autonomously browse, code, manage files**, and coordinate in businesses.
# - **Multimodality Standard**:
#   - Leading models process **text, images, audio, video, and code** in a single context window.
# - **Regulation & Governance**:
#   - **EU AI Act**, **US Executive Orders**, and **global AI safety frameworks** are tightening compliance requirements.
# - **Open-Source AI**:
#   - **Alibaba & DeepSeek** driving **lower-cost AI models** in China.
#   - **Meta’s open-sourcing** of **Muse Glimmer** for local AI agents.

# #### **Healthcare & Scientific AI**
# - **Google AI Health Coach** (August 2026):
#   - Integrates **Abbott glucose data** for personalized health guidance.
# - **Novo Nordisk & AWS**:
#   - Deploy **agentic AI** in **drug discovery**.
# - **Stanford Evo 2 AI Model**:
#   - Generates **phages against E. coli** (August 2026).
# - **AlphaEvolve & Google DeepMind Accelerator**:
#   - Tackling **climate, logistics, and molecular simulations**.

# #### **Enterprise & Business AI**
# - **Alvys**: Launches **AI agents for freight logistics (TMS workflows)**.
# - **Aviva**: Uses AI to **stop £230M in insurance fraud**.
# - **HP & OpenAI Frontier**: Accelerate **enterprise workflows**.
# - **McDonald’s App**: Among **Top 10 global brands** due to AI-driven personalization.

# #### **Environment & Sustainability**
# - **China’s AI Mapped Entire Renewable Energy Grid** (May 2026).
# - **IBM Unveils Analog AI Chip** for **energy-efficient deep learning**.

# #### **Notable AI Shutdowns & Strategic Moves**
# - **OpenAI Shut Down Sora** (video generation) in **March 2026**, redirecting resources to **robotics & simulation**.
# - **AMD Invests $5B in Anthropic** (July 2026) for AI infrastructure.

# ---
# **Key Takeaways**:
# ✅ **AI is becoming more agentic, multimodal, and integrated** into daily life.
# 💰 **Massive funding & valuations** driving rapid innovation.
# 🔬 **Healthcare, science, and sustainability** are top AI application areas.
# 🏢 **Enterprises & governments** are adopting AI at scale, with **regulation tightening**.



#tools also have have these features >> 
# print(search_tool.name)
# print(search_tool.description)
# print(search_tool.args)


#OUTPUT > 
# search_tool = TavilySearchResults(max_results = 5) 
# tavily_search_results_json
# A search engine optimized for comprehensive, accurate, and trusted results. Useful for when you need to answer questions about current events. Input should be a search query.
# {'query': {'description': 'search query to look up', 'title': 'Query', 'type': 'string'}}