import chromadb
import ollama

client = chromadb.Client()

collection = client.create_collection(
    name="documents"
)

documents = [
    "Python is a programming language",
    "AI agents use LLMs",
    "FastAPI builds APIs"
]

for index, doc in enumerate(documents):

    embedding = ollama.embeddings(
        model="nomic-embed-text",
        prompt=doc
    )["embedding"]

    collection.add(
        ids=[str(index)],
        documents=[doc],
        embeddings=[embedding]
    )

query = "How do AI systems work?"

query_embedding = ollama.embeddings(
    model="nomic-embed-text",
    prompt=query
)["embedding"]

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

print(results)