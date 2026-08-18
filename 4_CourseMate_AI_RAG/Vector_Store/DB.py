from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings #For OpenAI Embeddings
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()



from langchain_core.documents import Document
# The from langchain_core.documents import Document statement imports the core data abstraction used across LangChain 
# to store a unit of text and its accompanying metadata.
#WE ARE USING IT TO MAKE OUR OWN DOCUMENT OBJECTS AND THEN WE CAN STORE IT IN VECTOR STORE


docs = [
    Document(page_content="Python is widely used in Artificial Intelligence.", metadata={"source": "AI_book"}),
    Document(page_content="Pandas is used for data analysis in Python.", metadata={"source": "DataScience_book"}),
    Document(page_content="Neural networks are used in deep learning.", metadata={"source": "DL_book"}),
]


#so in this way we have created 3 docs and now we have to generate embedding for these


#GOOD THING IS THAT CHROMA DB GENERATE EMBEDDING AUTOMATICALLY BY ITS OWN FOR US AND STORE IT IN VECTOR STORE
#JUST WE HAVE TO TELL IT THROUGH WHICH WE WANT TO GENERATE EMBEDINGS AND THEN IT WILL DO IT AUTOMATICALLY FOR US


#FOR THAT WE HAVE TO USE EMBEDDING MODEL , LOAD A MODEL

embedding_model  = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2") 

#after this we have to create a vector store where we will specify it to take "Documents" and will use this "Embedding Model"
#and where we will have to save this 
#we will tell all these things to our vector store class 

vectorstore = Chroma.from_documents(
    documents = docs,
    embedding=embedding_model, 
    persist_directory="chroma_db"  #for storing data in local storage we have to give persist_directory and then we have to give the path where we want to store it
)


#--------------------------------------------------------------------------------------------------------------------------------------------

#when we will run till here we see there will be a folder get created named > "chroma_db"
#this got created as we had made a persist_directory and saidwhat wil be the documents and other save inside it


#SO THE THINGS THAT GOT CREATED ARE >>
#1. chroma_db folder >> this is the folder where all the data will be stored IN STRUCTURED WAY


#BUT we in vector_database we store emneddings which are not stored in structured way
#>> but since we have more thing that are there  like page content and metadata and when we create embedding than also , embeddings of page content
#so we not only have to save embedding, but we also have to save page_content, metadata, so for it we have sqlite database which is also created inside the "chroma_db" folder


#APART from  "chroma.sqllite3", we have some more things i.e "data_level0.bin", "header.bin", "length.bin", "link_list.bin"

#in these we store the embeddings and other things in binary format
#these are created since, if we have to do similarity search then in these all things get 

#for ex > it uses HSNW technique for similarity search and it uses these binary files for it(graph structured used for nearest neighbor search)

#SO AT THE END OF DAY WE ARE CREATING ALL THE EMBEDDING AND ALSO SAVING THEM AND ALSO CREATING SOME STRUCTURED, SO THAT INSIDE THAT WE CAN DO
#DO FAST INDEXING


#--------------------------------------------------------------------------------------------------------------------------------------------


 
#Now after our vector_store get created, we will find our result

#SO AFTER THIS WE ALSO HAVE TO RETRIEVE THE DATA FROM VECTOR STORE, SO FOR THAT WE USE RETRIVERS


result = vectorstore.similarity_search("What is used for Data Analysis?", k=2) #k=2 means we want to get 2 most relevant documents from the vector store, so that we can use it to answer our question

#vector_store are not responsible for answering our question, it is only responsible for retrieving the relevant documents from the vector store, 
# so that we can use it to answer our question


#--------------------------------------------------------------------------------------------------------------------------------------------


# for r in result:
#     print(r)


#OUTPUT > 

# page_content='Pandas is used for data analysis in Python.' metadata={'source': 'DataScience_book'}
# page_content='Pandas is used for data analysis in Python.' metadata={'source': 'DataScience_book'}

# REASON >> 

#when we run it one time than first time 3 embedding will get created and most simlar is comming > "# page_content='Pandas is used for data analysis in Python.' metadata={'source': 'DataScience_book'}"
#so next time when running same 3 embedding gets created and most simlar is comming as output
#same thing is comming as its loading 2 times 
#so for understanding it properly we could have use jupyter notebook as it uses cell system 



# The reason it gets duplicated is this part in [DB.py (line 37)](/C:/Users/ASUS/genAI-2/4_CourseMate_AI_RAG/Vector_Store/DB.py:37):
# vectorstore = Chroma.from_documents(
#     documents=docs,
#     embedding=embedding_model,
#     persist_directory="chroma_db"
# )
# Because you used a persist_directory, the database is saved on disk. When you run DB.py again, it does not “replace” the 
# old data automatically. It adds the same 3 documents again into the same collection. So after running multiple times, your
#  DB can look like this:
# Python...
# Pandas...
# Neural networks...
# Python...
# Pandas...
# Neural networks...
# Then when you do similarity search for "What is used for Data Analysis?", the two closest matches are both the duplicated 
# Pandas... rows, so you get:
# page_content='Pandas is used for data analysis in Python.' metadata={'source': 'DataScience_book'}
# page_content='Pandas is used for data analysis in Python.' metadata={'source': 'DataScience_book'}

#--------------------------------------------------------------------------------------------------------------------------------------------


# 
for r in result:
    print(r.page_content)
    print(r.metadata)


#page_content and metadata we will save in sql_lite on the other hand query that get created saved automatically and inside that we can perform 
#simlilarity search



#so we have founded  2 simler searches  of " What is used for Data Analysis?" and store those in "result" and after that we will use retriver


retriver = vectorstore.as_retriever() #if we not write any things inside .as_retriever(), then by default "SIMILARITY SEARCH STRATEGIES" used
docs = retriver.invoke("Explain deep learning")

for d in docs:
    print(d.page_content)



# Pandas is used for data analysis in Python.
# {'source': 'DataScience_book'}
# Neural networks are used in deep learning.
# {'source': 'DL_book'}
# Neural networks are used in deep learning.
# Python is widely used in Artificial Intelligence.
# Pandas is used for data analysis in Python.
