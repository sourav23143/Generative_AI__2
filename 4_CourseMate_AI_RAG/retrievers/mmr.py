 
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings



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


#1. FIRST WE ARE USING SIMILARITY RETRIVAL 
similarity_retriever = vectorstore.as_retriever(
    search_type = "similarity",
    search_kwargs = {"k":3}
)

print("\n========== Similarity Search Results ==========\n")

similarity_docs = similarity_retriever.invoke("What is gradient descent")

for doc in similarity_docs:
    print(doc.page_content)





#2. FIRST WE ARE USING MMR RETRIVAL 
similarity_retriever = vectorstore.as_retriever(
    search_type = "mmr",
    search_kwargs = {"k":3}
)

print("\n========== MMR Results ==========\n")

similarity_docs = similarity_retriever.invoke("What is gradient descent")

for doc in similarity_docs:
    print(doc.page_content)


#OUTPUT > 

# ========== Similarity Search Results ==========

# Gradient descent is an optimization algorithm used in machine learning
# Gradient descent is an optimization that minimizes the loss function
# Gradient descent minimizes the loss function.

# ========== MMR Results ==========

# Gradient descent is an optimization algorithm used in machine learning
# Gradient descent is an optimization that minimizes the loss function
# Neural Network use gradient descent for training