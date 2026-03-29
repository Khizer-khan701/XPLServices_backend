from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import PGVector
from app.core.config import settings

COLLECTION_NAME = "sunmarke_docs"

def get_vectorstore():
    embeddings = OpenAIEmbeddings(
        model="text-embedding-ada-002",
        openai_api_key=settings.OPENAI_API_KEY
    )

    vectorstore = PGVector(
        connection_string=settings.DATABASE_URL,
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
    )
    return vectorstore


def retrieve_context(query: str, k: int = 4) -> str:
    vectorstore = get_vectorstore()

    docs = vectorstore.similarity_search(query, k=k)

    if not docs:
        return ""

    context = "\n\n".join([doc.page_content for doc in docs])
    return context