from fastapi import FastAPI, UploadFile, File
from rag_pipeline import RAGPipeline
import shutil

app = FastAPI(title="Vector RAG API")

pipeline = RAGPipeline()


@app.post("/documents/")
async def upload_document(file: UploadFile = File(...)):
    path = f"data/{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    pipeline.ingest_document(path)
    return {"status": "Document ingested"}


@app.post("/query/")
def query_documents(query: str, top_k: int = 5):
    return pipeline.query(query, top_k)


@app.delete("/documents/")
def delete_all_documents():
    pipeline.store.delete_all()
    return {"status": "All documents deleted"}
