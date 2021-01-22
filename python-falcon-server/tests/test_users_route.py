import pytest
from falcon.testing import TestClient, Result


@pytest.fixture
def user() -> dict:
    return {
        "documento": "39466014",
        "username": "juanmesaglio",
        "nombres": "juan",
        "apellidos": "mesaglio",
        "genero": "masculino",
        "fechaNacimiento": "10/01/1996"
    }


def test_get_empty_users(client: TestClient):
    response = client.simulate_get('/usuarios')
    assert response.status_code == 200
    assert b'[]' in response.content


def test_create_user(client: TestClient, user: dict):
    response = client.simulate_post('/usuarios', json=user)
    assert response.status_code == 201


def test_create_user_bad_request(client: TestClient, user: dict):
    del user['documento']
    print(user)
    response = client.simulate_post('/usuarios', json=user)
    assert response.status_code == 400


def test_get_created_user(client: TestClient, user: dict):
    response = client.simulate_post('/usuarios', json=user)
    assert response.status_code == 201
    response2 = client.simulate_get(f"/usuarios/{user.get('username')}")
    assert response2.status_code == 200
    assert user.get('username').encode() in response2.content
    assert user.get('nombres').encode() in response2.content
    assert user.get('apellidos').encode() in response2.content
    assert user.get('genero').encode() in response2.content
    assert user.get('documento').encode() in response2.content
    assert user.get('fechaNacimiento').encode() in response2.content


def test_update_user(client: TestClient, user):
    user['nombres'] = 'juan ignacio'
    response = client.simulate_patch(f"/usuarios/{user.get('username')}", json=user)
    assert response.status_code == 200


def test_update_user_not_found(client: TestClient, user):
    user['nombres'] = 'juan ignacio'
    response = client.simulate_patch(f"/usuarios", json=user)
    assert response.status_code == 404


def test_update_user_bad_request(client: TestClient, user):
    del user['nombres']
    response = client.simulate_patch(f"/usuarios/{user.get('username')}", json=user)
    assert response.status_code == 400


def test_delete_user(client: TestClient, user):
    response = client.simulate_delete(f"/usuarios/{user.get('username')}")
    assert response.status_code == 200


def test_delete_not_found_user(client: TestClient):
    response = client.simulate_delete('/usuarios/fernando')
    assert response.status_code == 200


def test_not_found_user(client: TestClient):
    response2 = client.simulate_get(f"/usuarios/claudio")
    assert response2.status_code == 404
