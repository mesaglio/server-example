def test_ping_request(test_client):
    res = test_client.get('/ping')
    assert res.status_code == 200
    assert b'Pong' in res.content