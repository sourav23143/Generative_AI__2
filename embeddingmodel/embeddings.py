from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(
    model = 'text-embedding-3-large', 
    dimensions = 64 #dimension of a text
)


texts = ["Hello I am Sourav",
         "You are embedding model",
         "And you are beautiful"
]


# vector  = embeddings.embed_query("we are going to learn GenAI")  #for query
vector = embeddings.embed_documents(texts)  #for documents

print(vector)