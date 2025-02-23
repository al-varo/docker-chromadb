import json
import os
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

json_file = os.path.join("data", "persediaan_desember_2023.json")

with open(json_file, "r", encoding="utf-8") as file:
    data = json.load(file)

data_texts = [f"Produk: {item['Produk']}, Kuantitas: {item['Kuantitas']}, Nilai Persediaan: {item['Nilai Persediaan']}" for item in data]

vector_db = Chroma.from_texts(data_texts, embedding=OpenAIEmbeddings(), persist_directory="data/chromadb")

print("✅ Data disimpan ke ChromaDB.")
