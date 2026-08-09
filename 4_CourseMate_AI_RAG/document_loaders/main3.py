from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI

from langchain_community.document_loaders import PyPDFLoader
#by using document loader we can load any documnet

from langchain_core.prompts import ChatPromptTemplate #we are using ChatPromptTemplate as in this we can give roles also.

from langchain_text_splitters import RecursiveCharacterTextSplitter



load_dotenv()

model = ChatMistralAI(model = "mistral-small-2506")



data = PyPDFLoader("document_loaders/fundamental_of_deep_learning.pdf")  
docs = data.load()


#if we run like this only than error will come -> Rate Limit Exceeded: 429 > as we cant send whole pdf at once as it
#  will be out of context window of model 
# so first we will need to do chunking
#then we will store it Vector Database and then we will do RAG( Retrieval Augmented Generation) to get the answer from the pdf

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000, #size of chunk
    chunk_overlap = 200, #overlap of chunk
)
#now if we do chunking then it will split the document into chunks and then we can send it to model for summarization
#and that will not show error


chunks = splitter.split_documents(docs) #splitting the document into chunks

prompt_template = ChatPromptTemplate.from_messages(
    [("system", "you are a AI that summarizes the text"),
     ("human", "{data}")]

)


final_prompt = prompt_template.format_messages(data = docs)

result  = model.invoke(final_prompt)

print(result.content)


#if we run like this only than error will come -> Rate Limit Exceeded: 429 > as we cant send whole pdf at once as it
#  will be out of context window of model 
# so first we will need to do chunking
#then we will store it Vector Database and then we will do RAG( Retrieval Augmented Generation) to get the answer from the pdf