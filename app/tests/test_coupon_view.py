from fastapi.testclient import TestClient

def test_coupon_get(client: TestClient):
    response = client.get('/coupon/')
    assert response.json() == []

def test_coupon_create(client: TestClient, coupon_factory):
    coupon = coupon_factory()

    response = client.post('/coupon/',
                            json={
                                'code':'4A5B6C',
                                'expire_at':'3/14/2016',
                                'limit':1,
                                'mode':'VALUE',
                                'value':10.0
                            })

    assert response.status_code == 201
    assert response.json()['code'] == '4A5B6C'

def test_coupon_update(client: TestClient, coupon_factory):
    coupon = coupon_factory()
    
    response = client.post('/coupon/',
                            json={
                                'code':'4A5B6C',
                                'expire_at':'3/14/2016',
                                'limit':1,
                                'mode':'VALUE',
                                'value':10.0
                            })
    
    assert response.status_code == 201
    assert response.json()['code'] == '4A5B6C'

    response = client.put(
        '/coupon/1',
        json={'description': '4A5B6C Alterado!!'})

    assert response.status_code == 200
    assert response.json()['name'] == '4A5B6C Alterado!!'
