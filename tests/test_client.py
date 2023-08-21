
from app import simple_flask
import pytest
from flask import Response


@pytest.fixture
def test_client():
    simple_flask.app.config['TESTING'] = True
    client = simple_flask.app.test_client()
    assert client


def test_home_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
