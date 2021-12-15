from fastapi.testclient import TestClient

def test_category_get(client: TestClient):
    response = client.get('/categories/')
    assert response.json() == []

def test_category_create(client: TestClient):
   response = client.post('/categories/',json={'name': 'Categoria Teste Pytest'})

   assert response.status_code == 201

   assert response.json()['name'] == 'Categoria Teste Pytest'


def test_category_update(client: TestClient):

    response = client.post('/categories/', json={'name': 'Categoria Alterada!!'})
    
    assert response.status_code == 201

    response = client.put(
        '/categories/1',
        json={'name': 'Categoria Alterada'})

    assert response.status_code == 200
    assert response.json()['name'] == 'Categoria Alterada'

    response = client.get('/categories/1')
    assert response.json()['name'] == 'Categoria Alterada!!'

