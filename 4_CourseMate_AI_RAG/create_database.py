from pathlib import Path

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader


BASE_DIR = Path(__file__).resolve().parent
PDF_PATH = BASE_DIR / "document_loaders" / "fundamental_of_deep_learning.pdf"
CHROMA_PATH = BASE_DIR / "chroma_db"


def load_pdf_documents(pdf_path: Path) -> list[Document]:
    reader = PdfReader(str(pdf_path))
    documents: list[Document] = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if not text.strip():
            continue

        documents.append(
            Document(
                page_content=text,
                metadata={"source": pdf_path.name, "page": page_number},
            )
        )

    return documents


def main() -> None:
    load_dotenv()

    if not PDF_PATH.exists():
        raise FileNotFoundError(f"PDF not found: {PDF_PATH}")

    docs = load_pdf_documents(PDF_PATH)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    chunks = splitter.split_documents(docs)

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=str(CHROMA_PATH),
    )

    persist_method = getattr(vectorstore, "persist", None)
    if callable(persist_method):
        persist_method()

    print(f"Loaded {len(docs)} pages from {PDF_PATH.name}")
    print(f"Created {len(chunks)} chunks")
    print(f"Chroma database saved to: {CHROMA_PATH}")


if __name__ == "__main__":
    main()
