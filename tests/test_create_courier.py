import allure
import pytest
import requests
from helpers import generate_random_string, login_and_get_courier_id, delete_courier
from data import CREATE_COURIER, login_valid


class TestCreateCourier:
    @allure.title('Проверка успешного создания курьера только при заполненных обязательных полях')
    @allure.description('Проверка получения кода 201 Created и сообщения {"ok": True} при отправке POST-запроса '
                        'на создание курьера при заполненных полях login и password валидными данными')
    def test_create_courier_required_fields_filled_in_success(self):
        payload = {'login': generate_random_string(10), 'password': generate_random_string(10)}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(CREATE_COURIER, json=payload, headers=headers)
        assert response.status_code == 201 and response.json() == {"ok": True}
        courier_id = login_and_get_courier_id(payload)
        delete_courier(courier_id)

    @allure.title('Проверка успешного создания курьера при всех заполненных полях')
    @allure.description('Проверка получения кода 201 Created и сообщения {"ok": True} при отправке POST-запроса '
                        'на создание курьера при заполненных полях login, password и firstName валидными данными')
    def test_create_courier_all_field_filled_in_success(self):
        payload = {'login': generate_random_string(10), 'password': generate_random_string(10),
                   'firstName': generate_random_string(10)}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(CREATE_COURIER, json=payload, headers=headers)
        assert response.status_code == 201 and response.json() == {"ok": True}
        courier_id = login_and_get_courier_id(payload)
        delete_courier(courier_id)

    @allure.title('Проверка неудачного создания курьера при незаполненных обязательных полях')
    @allure.description('Проверка получения кода 400 Bad request и сообщения '
                        '{"message": "Недостаточно данных для создания учетной записи"} при отправке POST-запроса '
                        'на создание курьера при незаполненных полях login/password')
    @pytest.mark.parametrize('login, password', [
        ('', generate_random_string(10)),
        (generate_random_string(10), ''),
        ('', '')
    ])
    def test_create_courier_without_required_fields_failed(self, login, password):
        payload = {'login': login, 'password': password}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(CREATE_COURIER, json=payload, headers=headers)
        assert (response.status_code == 400 and
                response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'})

    @allure.title('Проверка неудачного создания курьера при использовании существующего логина')
    @allure.description('Проверка получения кода 409 Conflict и сообщения '
                        '{"message": "Этот логин уже используется"} при отправке POST-запроса на создание курьера '
                        'при использовании существующего логина')
    def test_create_courier_with_existing_login(self):
        payload = {'login': login_valid, 'password': generate_random_string(10)}
        headers = {'Content-Type': 'application/json'}
        requests.post(CREATE_COURIER, json=payload, headers=headers)
        response_check = requests.post(CREATE_COURIER, json=payload, headers=headers)
        assert (response_check.status_code == 409 and
                response_check.json() == {'code': 409, "message": "Этот логин уже используется"})
