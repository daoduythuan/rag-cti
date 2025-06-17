from rag.query_engine import ask_question

def main():
    print("🧠 Ask a question (e.g., 'What does technique T1059.003 describe?'):")
    query = input("🧠 Ask: ")
    answer, sources = ask_question(query)
    print(f"\n📄 Answer: {answer}")
    print("\n📚 Sources:")
    for source in sources:
        print(f" - {source.metadata.get('id', 'Unknown')}")

if __name__ == "__main__":
    main()
