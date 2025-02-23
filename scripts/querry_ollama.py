import os
from langchain.llms import Ollama
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

OLLAMA_SERVER = os.getenv("OLLAMA_SERVER")
CHROMA_DB = os.getenv("CHROMA_DB")

llm = Ollama(model="llama3.1", base_url=OLLAMA_SERVER)
vector_db = Chroma(persist_directory="data/chromadb", embedding_function=OpenAIEmbeddings())

def ask_ai(question):
    retrieved_docs = vector_db.similarity_search(question)
    context = "\n".join([doc.page_content for doc in retrieved_docs])
    prompt = f"Gunakan data berikut:\n\n{context}\n\n{question}"
    
    response = llm(prompt)
    return response

query = "Berapa total nilai persediaan?"
answer = ask_ai(query)
print(f"❓ {query}\n💡 Jawaban: {answer}")
