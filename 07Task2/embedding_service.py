import ollama
from typing import List
from config import OLLAMA_EMBED_MODEL


class EmbeddingService:
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        embeddings = []
        for text in texts:
            response = ollama.embeddings(
                model=OLLAMA_EMBED_MODEL,
                prompt=text
            )
            embeddings.append(response["embedding"])
        return embeddings

    def embed_query(self, query: str) -> List[float]:
        response = ollama.embeddings(
            model=OLLAMA_EMBED_MODEL,
            prompt=query
        )
        return response["embedding"]
