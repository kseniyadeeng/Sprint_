import requests
import random
import string
from test_data import CREATE_COURIER, LOGIN_COURIER


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def login_and_get_courier_id(payload):
    login_response = requests.post(LOGIN_COURIER, json=payload)
    assert login_response.status_code == 200
    courier_id = login_response.json().get('id')
    assert courier_id is not None
    return courier_id

def delete_courier(courier_id):
    delete_response = requests.delete(f"{CREATE_COURIER}/{courier_id}")
    assert delete_response.status_code == 200

def register_new_courier_and_return_login_password():
    def generate_random_string_for_login(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    login_pass = []

    login = generate_random_string_for_login(10)
    password = generate_random_string_for_login(10)
    first_name = generate_random_string_for_login(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(CREATE_COURIER, data=payload)
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass