from falcon import testing
import pytest
from server import create_app


@pytest.fixture()
def client():
    return testing.TestClient(create_app())
