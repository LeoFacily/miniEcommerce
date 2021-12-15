from fastapi.testclient import TestClient

def test_supplier_get(client: TestClient):
    response = client.get('/suppliers/')
    assert response

def test_supplier_create(client: TestClient):
    response = client.post('/suppliers',
                            json={'':''})

    assert response.status_code == 201
    #assert response.json()['id'] == 1
