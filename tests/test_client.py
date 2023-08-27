
import simple_flask
import pytest
from flask import Response




simple_flask.app.config['TESTING'] = True


def test_home_page():
   
    with simple_flask.app.test_client()  as test_client:
        response = test_client.get('/')
        assert response.status_code == 200

def test_login_page():
    
    with simple_flask.app.test_client()  as test_client:
        response = test_client.get('/login')
        assert response.status_code == 200


def test_register_page():
    
    with simple_flask.app.test_client()  as test_client:
        response = test_client.get('/register')
        assert response.status_code == 200

def test_user_creation():
    new_user = simple_flask.User("billy@yahoo.com","pass")
    assert new_user.email == "billy@yahoo.com"
    assert new_user.password_hashed == "pass"


def test_login():

    with simple_flask.app.test_client() as test_client:
        response = test_client.post('/login', data={'email': 'coletista7@gmail.com', 'password': 'salt'})
        assert response.status_code == 302
        assert response.headers['Location'] == '/'