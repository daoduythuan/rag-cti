# 🧠 Cyber Threat Intelligence RAG System

This is a Retrieval-Augmented Generation (RAG) system built for answering Cyber Threat Intelligence (CTI) questions using MITRE ATT&CK data and HuggingFace models.

> Powered by LangChain, FAISS, and HuggingFace Transformers.

## 📦 Features
- 💬 Ask natural language questions about MITRE techniques
- 🔎 FAISS-powered semantic search
- 🤗 HuggingFace models for embeddings and generation
- 🧱 Modular components for ingestion and querying
- 🌐 Streamlit UI

## 🛠️ Usage

### Setup

```bash
python3 -m venv rag-cti
source rag-cti/bin/activate
pip install -r requirements.txt
```

### Index data

```bash
python rag/load_mitre.py
```

### Query

```bash
python app/cli.py
```

### Streamlit

```bash
streamlit run streamlit_app.py
```

## 📚 Sample Input

```json
[
  {
    "id": "T1059.003",
    "name": "Windows Command Shell",
    "description": "Adversaries may abuse command-line shells to execute commands and scripts."
  }
]
```
# rag-cti
