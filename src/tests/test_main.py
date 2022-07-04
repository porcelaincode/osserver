from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/device/register/74382834fu4h48")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}