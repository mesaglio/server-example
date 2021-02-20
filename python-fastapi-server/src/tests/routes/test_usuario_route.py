import pytest


@pytest.fixture
def user() -> dict:
    return {
        "documento": "39125623",
        "username": "juanmesaglio",
        "nombres": "juan",
        "apellidos": "mesaglio",
        "genero": "masculino",
        "fechaNacimiento": "10/01/1996"
    }


def test_get_empty_users(test_client):
    response = test_client.get('/usuarios')
    assert response.status_code == 200
    assert b'[]' in response.content


def test_create_user(test_client, user: dict):
    response = test_client.post('/usuarios', json=user)
    assert response.status_code == 201


def test_create_user_bad_request(test_client, user: dict):
    del user['documento']
    print(user)
    response = test_client.post('/usuarios', json=user)
    assert response.status_code == 422


def test_get_created_user(test_client, user: dict):
    response = test_client.post('/usuarios', json=user)
    assert response.status_code == 201
    response2 = test_client.get(f"/usuarios/{user.get('username')}")
    assert response2.status_code == 200
    assert user.get('username').encode() in response2.content
    assert user.get('nombres').encode() in response2.content
    assert user.get('apellidos').encode() in response2.content
    assert user.get('genero').encode() in response2.content
    assert user.get('documento').encode() in response2.content
    assert user.get('fechaNacimiento').encode() in response2.content


def test_update_user(test_client, user):
    user['nombres'] = 'juan ignacio'
    response = test_client.patch(f"/usuarios/{user.get('username')}", json=user)
    assert response.status_code == 200


def test_update_user_not_found(test_client, user):
    user['nombres'] = 'juan ignacio'
    response = test_client.patch(f"/usuarios/fernando", json=user)
    assert response.status_code == 404


def test_delete_user(test_client, user):
    response = test_client.delete(f"/usuarios/{user.get('username')}")
    assert response.status_code == 200


def test_delete_not_found_user(test_client):
    response = test_client.delete('/usuarios/fernando')
    assert response.status_code == 200


def test_not_found_user(test_client):
    response2 = test_client.get(f"/usuarios/claudio")
    assert response2.status_code == 404
