import requests
import pytest
import json
import random

port = 3000
base_url = f'http://localhost:{port}'
users_url = base_url + '/usuarios'
users = [
    {
        "documento": "39411052",
        "username": "juan",
        "nombres": "juan ignacio",
        "apellidos": "mesaglio",
        "genero": "masculino",
        "fechaNacimiento": "10/10/1996"
    },
    {
        "documento": "29366057",
        "username": "maga",
        "nombres": "magali",
        "apellidos": "braum",
        "genero": "femenino",
        "fechaNacimiento": "01/8/1996"
    }
]


def eq_obj(obj1, obj2):
    items_obj1 = obj1.items()
    items_obj2 = obj2.items()
    return all(item in items_obj1 for item in items_obj2)

def change_document(obj):
    obj['documento'] = random.randint(30000000,40000000)
    return obj


def test_empyt_users():
    empty_users = requests.get(users_url)
    assert empty_users.status_code == 200
    assert empty_users.content == b'[]'


def test_bad_requests():
    post_bad_request = requests.post(users_url, json={})
    assert post_bad_request.status_code == 400


def test_not_found():
    patch_bad_request = requests.patch(
        f"{users_url}/{random.choice(users).get('username')}", json={})
    assert patch_bad_request.status_code == 404


def test_delete_not_found():
    delete_request = requests.delete(f"{users_url}/{random.choice(users).get('username')}")
    assert delete_request.status_code == 200


def test_add_users():
    for user in users:
        response = requests.post(users_url, json=user)
        assert response.status_code == 200


def test_get_users():
    for user in users:
        response = requests.get(f"{users_url}/{user.get('username')}")
        assert response.status_code == 200
        assert eq_obj(user, json.loads(response.content))

def test_update_users():
    new_users = list(map(lambda o: change_document(o),users))
    for user in new_users:
        response = requests.patch(f"{users_url}/{user.get('username')}", json=user)
        assert response.status_code == 200
        response_get = requests.get(f"{users_url}/{user.get('username')}")
        assert response_get.status_code == 200
        assert eq_obj(user,json.loads(response_get.content))


def test_delete_all_users():
    for user in users:
        request = requests.delete(f"{users_url}/{user.get('username')}")
        assert request.status_code == 200
    all_users = requests.get(users_url)
    assert all_users.status_code == 200
    assert b'[]' in all_users.content
