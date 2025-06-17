import streamlit as st
from rag.query_engine import ask_question

st.title("🔍 CTI RAG System")
query = st.text_input("Ask a CTI question:", placeholder="e.g., What does technique T1059.003 describe?")
if st.button("Ask"):
    if query:
        answer, sources = ask_question(query)
        st.markdown("### 📄 Answer")
        st.write(answer)
        st.markdown("### 📚 Sources")
        for src in sources:
            st.write(f"- {src.metadata.get('id')}: {src.metadata.get('name')}")
    else:
        st.warning("Please enter a question.")
