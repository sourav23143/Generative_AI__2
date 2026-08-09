#if we want to load pdf file inm main.py > 

from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI

from langchain_community.document_loaders import PyPDFLoader
#by using document loader we can load any documnet

from langchain_core.prompts import ChatPromptTemplate #we are using ChatPromptTemplate as in this we can give roles also.




load_dotenv()

model = ChatMistralAI(model = "mistral-small-2506")



data = PyPDFLoader("4_CourseMate_AI_RAG/document_loaders/GRU.pdf")  
docs = data.load()


prompt_template = ChatPromptTemplate.from_messages(
    [("system", "you are a AI that summarizes the text"),
     ("human", "{data}")]

)


# final_prompt = prompt_template.format_messages(data = docs[0].page_content)

#or(we can use both)

#================================================================================================================================================


# BUT IN THIS THERE IS VERY BIG PROBLEM THAT IS Of CONTEX WINDOW, WE ARE USING mistral-small-2506 AND IF WE GIVE MISTRAL SMALL FULL PDF AT ONCE
#THEN IT WILL BE OUT OF ITS CONTEXT WINDOW AND WE WILL GOT A ERROR



#now we are sending 0th page here >
final_prompt = prompt_template.invoke(
    {"data" : docs[0].page_content}
)



#But if we send full docs then there will be an error for context window
# final_prompt = prompt_template.invoke(
#     {"data" : docs}
# )


#================================================================================================================================================

#SO FOR ITS SOLUTION  > WE DO CHUNKING


#================================================================================================================================================

result = model.invoke(final_prompt)

print(result.content)



# BUT IN THIS THERE IS VERY BIG PROBLEM THAT IS OG CONTEX WINDOW, WE ARE USING mistral-small-2506 AND IF WE GIVE MISTRAL SMALL FULL PDF AT ONCE
#THEN IT WILL BE OUT OF ITS CONTEXT WINDOW AND WE WILL GOT A ERROR


