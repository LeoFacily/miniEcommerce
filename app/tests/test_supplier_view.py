from fastapi.testclient import TestClient

def test_supplier_get(client: TestClient):
    response = client.get('/suppliers/')
    assert response.json() == []

def test_supplier_create(client: TestClient):
    response = client.post('/suppliers/',json={'name':'Supplier 4'})

    assert response.status_code == 201

    response = client.put('/suppliers/1',json={'name':'Supplier 4'})

def test_supplier_update(client: TestClient):

    response = client.post('/suppliers/', json={'name': 'Suplier Alterado!!'})
    
    assert response.status_code == 201

    response = client.put(
        '/suppliers/1',
        json={'name': 'Suplier Alterado!!'})

    assert response.status_code == 200
    assert response.json()['name'] == 'Suplier Alterado!!'


