import pytest
from flask import current_app

from manage import application

@pytest.fixture
def a_client():
    with application.test_client() as client:
        assert current_app.config["ENV"] == "production"  # Error!
        yield client

