from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

VECTORSTORE_PATH = "vectorstore/mitre_faiss_index/"

def ask_question(query):
    db = FAISS.load_local(VECTORSTORE_PATH, HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
    retriever = db.as_retriever()
    hf_pipeline = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.2", max_new_tokens=256, temperature=0.5)
    llm = HuggingFacePipeline(pipeline=hf_pipeline)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    result = qa_chain.invoke({"query": query})
    docs = retriever.get_relevant_documents(query)
    return result["result"], docs
