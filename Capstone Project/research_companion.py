from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# VectorDB
vector_db = None

# Embedding Model
embedding_model = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")


def init_vector_store(persist_directory='db'):

    global vector_db

    # TODO later
    # try:
    #     pass
    # except None:
    #     pass

    vector_db = Chroma(embedding_function=embedding_model,persist_directory=persist_directory)

    return vector_db


# def get_assistant_response(query):
#     return f"## Query is : {query}"


def add_documents_to_store(document_paths: list):

    global vector_db
    if vector_db is None:
        raise ValueError("Vector store not initialized. Call `init_vector_store()` first.")

    all_chunks = []
    for doc_path in document_paths:
        all_chunks.extend(load_and_chunk_pdf(doc_path))

    vector_db.add_documents(all_chunks)
    vector_db.persist()

def load_and_chunk_pdf(pdf_path: str):
    loader = PyPDFLoader(pdf_path, mode="page")
    pages = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300)
    return text_splitter.split_documents(pages)


def generate_embeddings(doc):
    # vectordb = Chroma.from_documents(documents=doc, embedding=embedding_fn)
    pass
