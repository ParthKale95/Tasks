import argparse
from rag_pipeline import RAGPipeline

pipeline = RAGPipeline()

parser = argparse.ArgumentParser(description="Vector RAG CLI")
parser.add_argument("--ingest", type=str, help="Path to document")
parser.add_argument("--query", type=str, help="Query text")

args = parser.parse_args()

if args.ingest:
    pipeline.ingest_document(args.ingest)
    print("Document ingested successfully")

if args.query:
    result = pipeline.query(args.query)
    print(result)
