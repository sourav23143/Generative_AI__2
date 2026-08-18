from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma #we are doing it since we also have to fetch the croma_db created database by "create_database.py"

from langchain_mistralai import ChatMistralAI

from langchain_core.prompts import ChatPromptTemplate #we are using ChatPromptTemplate as in this we can give roles also.

from langchain_text_splitters import RecursiveCharacterTextSplitter


 
load_dotenv()

embedding_model = HuggingFaceEmbeddings()


#now to retrive the things from vector store, we have to load already created vector store in our file >
vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

retriever = vectorstore.as_retriever(
    search_type = "mmr",
    search_kwargs = {  #search keywords
        "k" : 4,
        "fetch_k":10,  #means intially we need 10 by similarity search, and on it we wil apply mmr than we will get 4
        "lambda_mult": 0.5, #0 -> very much diverse result , 1 -> very less diverse result


    }
)


llm = ChatMistralAI(model = "mistral-small-2506")




#PROMPT TEMPLATE
prompt_template = ChatPromptTemplate.from_messages(
    [("system", """you are a helpful AI assistant.
    
    Use ONLY the provided context to answer the question.
    
    If the answer is not present in the context,
    say: "I could not find the answer in the document."
    """),
     ("human", 
      """Context:
    {context}
       
    Question:
    {question} 
         """)

    ]

)

print("Rag system created")

print("press 0 to exit")

while True:
    query = input("You :")
    if query == "0":
        break
    docs = retriever.invoke(query)

    context = "\n\n".join(   #join since to make single string for all the docs
        [doc.page_content for doc in docs]
    )

    final_prompt = prompt_template.invoke({
        "context" : context,
        "question": query

    })

    response = llm.invoke(final_prompt)

    print(f"\n AI: {response.content}")



final_prompt = prompt_template.format_messages(data = docs)

result  = model.invoke(final_prompt)

print(result.content)


# press 0 to exit
# You :Can you tell me about the  Word2Vec framework

#  AI: The Word2Vec framework is a method for generating word embeddings, which are vector representations of words in a 
# continuous vector space. It includes two main models:

# 1. **Continuous Bag of Words (CBOW)**: Predicts a target word based on its surrounding context words.
# 2. **Skip-Gram**: The inverse of CBOW, where the target word is used as input to predict the surrounding context words.

# For example, in the sentence "the boy went to the bank," the Skip-Gram model would create (input, output) pairs where the 
# input is the target word, and the output is one of the context words. This helps in learning meaningful word embeddings that 
# capture semantic relationships.

# Word2Vec is not a deep learning model but is significant for its approach to finding embeddings. Pretrained word embeddings, 
# such as those generated from Google News (which includes vectors for 3 million words and phrases trained on roughly 
# 100 billion words), can be used via the `gensim` Python package. These embeddings can reveal meaningful clusters, such as 
# grouping similar languages, cultures, or concepts (e.g., "written" being close to "translated," "poetry," etc.).

# The embeddings can be visualized using techniques like t-SNE to project high-dimensional vectors (e.g., 128 dimensions) 
# into 2D space for easier interpretation
# You :