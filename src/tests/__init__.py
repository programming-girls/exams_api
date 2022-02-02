import os
import tempfile

import pytest

from flaskr import create_app
from flaskr.db import init_db

from manage import application

@pytest.fixture
def a_client():
    db_fd, db_path = tempfile.mkstemp()
    with application.test_client() as client:
        with application.app_context():
            init_db()
        yield client
    os.close(db_fd)
    os.unlink(db_path)
