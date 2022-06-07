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
    expected_page_title = b"<h1>Welcome To App Test</h1>"
    # When
    response = test_client.get('/')
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_title in response.data



def test_employee_success(test_client):
    # Given
    expected_status_code = 200
    expected_page_title = b'<h1>Manages Employees'
    # When
    response = test_client.get('/')
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_title in response.data

def test_employee_failure(test_client):
    # Given
    expected_status_code = 200
    expected_page_alert = b'No employees Found'
    test_client.post('/delete/2')
    test_client.post('/delete/4')
    
    # When
    response = test_client.get('/')
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_alert in response.data

def test_addemployee_get(test_client):
    # Given
    expected_status_code = 200
    expected_page_title = b"<h1>Add Employee</h1>"
    # When
    response = test_client.get('/add')
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_title in response.data

def test_add_employee_post(test_client):
    # Given
    expected_status_code = 200
    expected_page_alert = b"EMployee added"
    expected_employee_name = b"TEST"
    expected_employee_price = b"1337"
    data_to_add={
                                        "name":"Sarah",
                                        "email":"sarah@gmail.com",
                                        "phone":"12345678"
                                            }
    # When
    response = test_client.post('/add',data=data_to_add,follow_redirects=True )
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_alert in response.data
    assert expected_employee_name in response.data
    assert expected_employee_price in response.data

def test_update_employee_get(test_client):
    # Given
    expected_status_code = 200
    expected_page_title = b"<h1>Edit Employee</h1>"
    id_to_update=2
    # When
    response = test_client.get(f'/send/{id_to_update}')
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_title in response.data

def test_update_employee_post(test_client):
    # Given
    expected_status_code = 200
    expected_page_alert = b"Employee updated successfully"
    expected_employee_name = b"paul"
    expected_employee_email = b"paul@gmail.com"
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
    assert expected_page_alert in response.data
    assert expected_employee_name in response.data
    assert expected_employee_email in response.data

def test_delete_employee_post(test_client):
    # Given
    expected_status_code = 200
    expected_page_alert = b"Employee Deleted"
    expected_employee_name = b"Mathis"
    id_to_delete = 4
    # When
    response = test_client.post(f'/delete/{id_to_delete}',follow_redirects=True )
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_alert in response.data
    assert expected_employee_name not in response.data

