from falcon.testing import TestClient, Result


def test_get_ping(client: TestClient):
    res: Result = client.simulate_get('/ping')
    assert b'Pong' in res.content
