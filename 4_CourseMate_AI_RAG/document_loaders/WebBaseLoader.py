from langchain_community.document_loaders import WebBaseLoader

url = "https://www.apple.com/in/macbook-pro/"
#to use multiple url > use it in list

data = WebBaseLoader(url) #creating object

docs = data.load()  #structuring the object

# print(len(docs))  #> 1 > as we have loaded one page only, as if we have loaded multiple pages then multiple document will be created

print(docs[0].page_content)