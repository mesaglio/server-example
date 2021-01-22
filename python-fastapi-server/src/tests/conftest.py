import pytest
from fastapi.testclient import TestClient
from src.main import create_app


@pytest.fixture(scope='function')
def test_client():
    app = create_app()
    return TestClient(app)
