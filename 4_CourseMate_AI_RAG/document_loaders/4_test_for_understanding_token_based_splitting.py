# Splitting by token - Text splitter integration guide


# Language models have a token limit. You should not exceed the token limit. When you split your text into chunks it is therefore a good idea to count the number of tokens.
# There are many tokenizers. When you count tokens in your text you should use the same tokenizer as used in the language model.


from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter


data = PyPDFLoader("document_loaders/GRU.pdf")


docs = data.load()


splitter = TokenTextSplitter(
    chunk_size = 100, #size of chunk
    chunk_overlap = 10, #overlap of chunk
)


chunks = splitter.split_documents(docs) #splitting the document into chunks

print(len(chunks)) # -> 10 

# print(chunks[0]) #to see first chunk document


#OUTPUT >>


# page_content='Gate-Variants of Gated Recurrent Unit (GRU) Neural 
# Networks  
 
# Rahul Dey and Fathi M. Salem 
# Circuits, Systems, and Neural Networks (CSANN) LAB 
# Department of Electrical and Computer Engineering 
# Michigan State University 
#  East Lansing, MI 48824-1226, USA 
#   deyrahul@msu.edu || salemf@msu.edu  '
# metadata={'producer': 'Nitro PDF PrimoPDF', 'creator': 'PrimoPDF http://www.primopdf.com', 'creationdate': '2017-01-20T15:45:30+05:00', 
#           'moddate': '2017-01-20T15:45:30+05:00', 'title': 'Microsoft Word - GRU_Variants_RahulDey_FathiMSalem_20Jan2017V.docx', 
#           'author': 'salem', 'source': 'document_loaders/GRU.pdf', 'total_pages': 5, 'page': 0, 'page_label': '1'}