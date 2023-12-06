from fastapi.testclient import TestClient
from app.main import app  
import pytest

@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client
        
        
        
def test_read_main(client):
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}