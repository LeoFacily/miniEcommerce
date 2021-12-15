from fastapi.testclient import TestClient


def test_product_create(client: TestClient, category_factory, supplier_factory, admin_auth_header):
    category = category_factory()
    supplier = supplier_factory()

    response = client.post('/products/', 
                           json={
                               'description': 'descricao',
                               'price': 100,
                               'image': 'image.dev',
                               'technical_details': 'bla bla',
                               'visible': True,
                               'category_id': category.id,
                               'supplier_id': supplier.id
                           })

    assert response.status_code == 201
    assert response.json()['description'] == 'descricao'
    assert response.json()['category_id'] == category.id
    assert response.json()['supplier_id'] == supplier.id


def test_product_update(client: TestClient, category_factory, supplier_factory):
    category = category_factory()
    supplier = supplier_factory()
    
    response = client.post('/products/',  
                            json={
                               'description': 'descricao',
                               'price': 100,
                               'image': 'image.dev',
                               'technical_details': 'bla bla',
                               'visible': True,
                               'category_id': category.id,
                               'supplier_id': supplier.id
                           })
    
    assert response.status_code == 201

    response = client.put(
        '/products/1',
        json={'description': 'descricao Alterada!!'})

    assert response.status_code == 200
    assert response.json()['name'] == 'descricao Alterada!!!!'
