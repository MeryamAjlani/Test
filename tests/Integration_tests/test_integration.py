import pytest
import os
from app import app
from db_init import create_db

#to run the test:
#coverage run -m pytest


@pytest.fixture(scope="session", autouse=True)
def create_test_database(tmp_path_factory):
    create_db()


@pytest.fixture(scope='module')
def test_client():
    flask_app =app
    flask_app.secret_key = 'Secret'
    flask_app.config.update({"TESTING":True,})
    testing_client = flask_app.test_client(use_cookies=True)
    context = flask_app.app_context()
    context.push()
    yield testing_client
    context.pop()

def test_index(test_client):
    # Given
    expected_status_code = 200
    # When
    response = test_client.get('/')
    # Then
    assert expected_status_code == response.status_code



def test_employee_success(test_client):
    # Given
    expected_status_code = 200

    # When
    response = test_client.get('/')
    # Then
    assert expected_status_code == response.status_code


def test_add_employee_post(test_client):
    # Given
    expected_status_code = 200
    data_to_add={
                                        "name":"Sarah",
                                        "email":"sarah@gmail.com",
                                        "phone":"12345678"
                                            }
    # When
    response = test_client.post('/add',data=data_to_add,follow_redirects=True )
    # Then
    assert expected_status_code == response.status_code


def test_update_employee_post(test_client):
    # Given
    expected_status_code = 200

    id_to_update=1
    data_to_update = {
        "name":"Paul",
        "email":"34",
        "quantity":"5"
    }

    # When
    response = test_client.post(f'/edit/{id_to_update}',data=data_to_update,follow_redirects=True )
    # Then
    assert expected_status_code == response.status_code


def test_delete_employee_post(test_client):
    # Given
    expected_status_code = 200

    id_to_delete = 4
    # When
    response = test_client.post(f'/delete/{id_to_delete}',follow_redirects=True )
    # Then
    assert expected_status_code == response.status_code
 

