from document_processor import DocumentProcessor
from embedding_service import EmbeddingService
from vector_store import VectorStore


class RAGPipeline:
    def __init__(self):
        self.processor = DocumentProcessor()
        self.embedder = EmbeddingService()
        self.store = VectorStore()

    def ingest_document(self, file_path: str):
        if file_path.endswith(".pdf"):
            text = self.processor.load_pdf(file_path)
        else:
            text = self.processor.load_text(file_path)

        chunks = self.processor.chunk_text(text)
        embeddings = self.embedder.embed_texts(chunks)
        self.store.add_documents(chunks, embeddings)

    def query(self, query: str, top_k=5):
        query_embedding = self.embedder.embed_query(query)
        results = self.store.similarity_search(query_embedding, top_k)
        return {
            "query_embedding": query_embedding,
            "results": results
        }
