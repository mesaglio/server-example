def test_get_ping_response(test_client):
    response = test_client.get('/ping')
    assert response.status_code == 200
    assert b'Pong' in response.data
