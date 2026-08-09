
# Splitting by character - Text splitter integration guide


# Character-based splitting is the simplest approach to text splitting. It divides text using a specified character 
# sequence (default: "\n\n"), with chunk length measured by the number of characters.
# Key points:
# How text is split: by a given character separator.
# How chunk size is measured: by character count.
# You can choose between:
# .split_text — returns plain string chunks.
# .create_documents — returns LangChain Document objects, useful when metadata needs to be preserved for downstream tasks.

# from langchain_community.document_loaders import TextLoader

# from langchain_text_splitters import CharacterTextSplitter


# text_splitter = CharacterTextSplitter(
#     chunk_size = 10, #size of chunk
#     chunk_overlap = 1, #overlap of chunk
# )

# data = TextLoader("document_loaders/notes_for_understanding_textSplitter.txt")

# docs = data.load()  #Load data into Document objects.

# chunks = text_splitter.split_documents(docs) #splitting the document into chunks

# print(len(chunks))
# print(chunks)


#Output >> 

# 1
# [Document(metadata={'source': 'document_loaders/notes_for_understanding_textSplitter.txt'}, 
#           page_content='Hello how are you\nI want to see what can I do and also I need your help\nplease help me')]




#------------------------------------------------------------------------------------------------------------------



#IF WE WANT ONLY CHARACTER BASED SPLITTING THEN WE CAN USE TEXT SPLITTER

from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import CharacterTextSplitter


text_splitter = CharacterTextSplitter(
    separator = "", #by default it is "\n\n" but we can give any character
    chunk_size = 10, #size of chunk
    chunk_overlap = 1, #overlap of chunk
)

data = TextLoader("document_loaders/notes_for_understanding_textSplitter.txt")

docs = data.load()  #Load data into Document objects.

chunks = text_splitter.split_documents(docs) #splitting the document into chunks

print(len(chunks))
print(chunks)

