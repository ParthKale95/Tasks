from fastapi.testclient import TestClient
from api import app
import os

client = TestClient(app)


def test_upload_document():
    # create a temporary test file
    test_file_content = b"Machine learning is a subset of artificial intelligence."
    test_file_path = "test_sample.txt"

    with open(test_file_path, "wb") as f:
        f.write(test_file_content)

    with open(test_file_path, "rb") as f:
        response = client.post(
            "/documents/",
            files={"file": ("test_sample.txt", f, "text/plain")}
        )

    os.remove(test_file_path)

    assert response.status_code == 200
    assert response.json()["status"] == "Document ingested"


def test_query_documents():
    response = client.post(
        "/query/",
        params={
            "query": "What is machine learning?",
            "top_k": 1
        }
    )

    assert response.status_code == 200
    assert "results" in response.json()
    assert len(response.json()["results"]) > 0
    assert "cosine_similarity" in response.json()["results"][0]


def test_delete_documents():
    response = client.delete("/documents/")
    assert response.status_code == 200
    assert response.json()["status"] == "All documents deleted"
