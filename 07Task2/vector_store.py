import chromadb
from chromadb.config import Settings
from typing import List
from config import CHROMA_DIR, COLLECTION_NAME


class VectorStore:
    def __init__(self):
        self.client = chromadb.Client(
            Settings(
                persist_directory=str(CHROMA_DIR),
                anonymized_telemetry=False
            )
        )
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME
        )

    def add_documents(self, texts: List[str], embeddings: List[List[float]]):
        ids = [str(i) for i in range(len(texts))]
        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            ids=ids
        )

    def similarity_search(self, query_embedding, top_k=5):
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        return results

    def delete_all(self):
        self.client.delete_collection(COLLECTION_NAME)
