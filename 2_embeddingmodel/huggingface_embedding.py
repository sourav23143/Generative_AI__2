from langchain_huggingface import HuggingFaceEmbeddings

# from dotenv import load_dotenv
# load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2",
)

texts = ["Hello I am Sourav",
         "You are embedding model",
         "And you are beautiful"
]


# vector  = embeddings.embed_query("we are going to learn GenAI")  #for query
vector = embeddings.embed_documents(texts)  #for documents

print(vector)