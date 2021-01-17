import pytest
from flask.testing import FlaskClient

from __init__ import create_app


@pytest.fixture(scope='function')
def test_client() -> FlaskClient:
    flask_app = create_app()
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            return testing_client
