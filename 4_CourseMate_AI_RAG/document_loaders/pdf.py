from pathlib import Path
import sys

from langchain_community.document_loaders import PyPDFLoader
#by using document loader we can load any documnet

sys.stdout.reconfigure(encoding="utf-8")

pdf_path = Path(__file__).resolve().parent / "GRU.pdf"
data = PyPDFLoader(str(pdf_path))

docs = data.load()

#for text there was doing one docs only
#but for pdf
print(docs)

print(len(docs)) #-> for this 5> so now we have 5 documents inside a list and inside every document there will be its meta data and page content
#our pdf had 5 pages , so 5 document was created inside list

#print(docs[4]) #to see last page document
