import sys

import arxiv
from langchain_core.documents import Document


sys.stdout.reconfigure(encoding="utf-8")


def fetch_arxiv_docs(query: str, max_results: int = 2) -> list[Document]:
    client = arxiv.Client()
    search = arxiv.Search(query=query, max_results=max_results)

    docs: list[Document] = []
    for result in client.results(search):
        docs.append(
            Document(
                page_content=result.summary,
                metadata={
                    "Title": result.title,
                    "Authors": ", ".join(author.name for author in result.authors),
                    "Entry ID": result.entry_id,
                    "Published": result.updated.date().isoformat(),
                },
            )
        )

    return docs


docs = fetch_arxiv_docs("large language models", max_results=2)

for i, doc in enumerate(docs, start=1):
    print(f"\nResult {i}")
    print("Title:", doc.metadata.get("Title"))
    print("Authors:", doc.metadata.get("Authors"))
    print("Summary:", doc.page_content[:500])
