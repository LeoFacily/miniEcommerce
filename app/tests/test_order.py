from fastapi.testclient import TestClient

def test_order_get(client: TestClient):
    response = client.get('/order')
    assert response.json() == [] 