import json
from pathlib import Path
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document

DATA_PATH = "data/attack_patterns.json"
VECTORSTORE_PATH = "vectorstore/mitre_faiss_index/"

def load_data(path):
    with open(path, "r") as f:
        entries = json.load(f)
    docs = []
    for entry in entries:
        content = f"{entry['name']}\n{entry['description']}"
        doc = Document(page_content=content, metadata={"id": entry["id"], "name": entry["name"]})
        docs.append(doc)
    return docs

def main():
    docs = load_data(DATA_PATH)
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(chunks, embeddings)
    Path(VECTORSTORE_PATH).mkdir(parents=True, exist_ok=True)
    db.save_local(VECTORSTORE_PATH)
    print("✅ FAISS index built and saved.")

if __name__ == "__main__":
    main()
