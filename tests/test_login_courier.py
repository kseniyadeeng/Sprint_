import allure
import pytest
import requests
from helpers import register_new_courier_and_return_login_password, generate_random_string, delete_courier
from test_data import LOGIN_COURIER, login_valid, password_valid


class TestLoginCourier:

    @allure.title('Проверка успешной авторизации курьера при заполненных обязательных полях')
    @allure.description('Проверка получения кода 200 Ok и сообщения {"id": [___]} при отправке POST-запроса '
                        'на авторизацию курьера при заполненных полях login и password валидными данными')
    def test_login_courier_required_fields_filled_in_success(self):
        create_login = register_new_courier_and_return_login_password()
        login, password, first_name = create_login
        payload = {'login': login, 'password': password}
        response = requests.post(LOGIN_COURIER, data=payload)
        assert response.status_code == 200 and 'id' in response.json()
        courier_id = response.json().get('id')
        delete_courier(courier_id)

    @allure.title('Проверка неудачного логина курьера при незаполненных обязательных полях')
    @allure.description('Проверка получения кода 400 Bad request и сообщения '
                        '{"message": "Недостаточно данных для входа"} при отправке POST-запроса '
                        'на авторизацию курьера при незаполненных полях login/password')
    @pytest.mark.parametrize('login, password', [
        ('', generate_random_string(10)),
        (generate_random_string(10), ''),
        ('', '')
    ])
    def test_login_courier_without_required_fields_failed(self, login, password):
        payload = {'login': login, 'password': password}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(LOGIN_COURIER, json=payload, headers=headers)
        assert (response.status_code == 400 and
                response.json() == {'code': 400, "message":  "Недостаточно данных для входа"})

    @allure.title('Проверка неудачного логина курьера при некорректно заполненных обязательных полях')
    @allure.description('Проверка получения кода 404 Not found и сообщения '
                        '{"message": "Учетная запись не найдена"} при отправке POST-запроса '
                        'на авторизацию курьера при несуществующем login и некорректном password')
    @pytest.mark.parametrize('login, password', [
        (generate_random_string(10), password_valid),
        (login_valid, generate_random_string(10))
    ])
    def test_login_courier_with_incorrect_data_failed(self, login, password):
        payload = {'login': login, 'password': password}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(LOGIN_COURIER, json=payload, headers=headers)
        assert (response.status_code == 404 and
                response.json() == {'code': 404, 'message': 'Учетная запись не найдена'})