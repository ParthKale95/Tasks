from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
CHROMA_DIR = BASE_DIR / "chroma_db"

# Ollama
OLLAMA_EMBED_MODEL = "nomic-embed-text"

# Chunking
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# Chroma
COLLECTION_NAME = "documents"

# API
API_HOST = "0.0.0.0"
API_PORT = 8000
