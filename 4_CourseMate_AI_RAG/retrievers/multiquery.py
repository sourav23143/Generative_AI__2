
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv


load_dotenv()



docs = [
    Document(page_content="Gradient descent is an optimization algorithm used in machine learning"),
    Document(page_content="Gradient descent minimizes the loss function."),
    Document(page_content="Gradient descent is an optimization that minimizes the loss function"),
    Document(page_content="Neural Network use gradient descent for training"),
    Document(page_content="Support Vector Machines are supervised learning algorithms"),

]


embeddings = HuggingFaceEmbeddings() #there is no need to define model, it automatically done


vectorstore = Chroma.from_documents(docs,embeddings)
#after creating vector store it will get save in our RAM locally, if we not tell it deginated location

retriver = vectorstore.as_retriever()


llm = ChatMistralAI(model= "mistral-small-latest")


multi_query_retriever = MultiQueryRetriever.from_llm(
    retriever=retriver, #here we are using normal retriver(cosine, mmr) inside multiquery retriver, means we will have multiple query
    #and for those query we can use retrive results by using that retriver
    llm = llm
)


#giving query 
query = "What is gradient descent?"

docs = multi_query_retriever.invoke(query)

print("\nRetrieved Documents:\n")

for doc in docs:
    print(doc.page_content)




# Retrieved Documents:

# Support Vector Machines are supervised learning algorithms
# Gradient descent is an optimization algorithm used in machine learning
# Neural Network use gradient descent for training
# Gradient descent is an optimization that minimizes the loss function
# Gradient descent minimizes the loss function.