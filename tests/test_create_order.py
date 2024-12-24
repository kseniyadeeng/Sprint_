import allure
import pytest
import requests
from test_data import CREATE_ORDER, order_data_black, order_data_grey, order_data_multicolor, order_data_no_color


class TestCreateOrder:

    @allure.title('Проверка успешного создания заказа c различными параметрами поля color')
    @allure.description('Проверка получения кода 201 Created и сообщения {"ok": True} при отправке POST-запроса '
                        'на создание заказа при заполненном поле color одним цветом, двумя цветами и без цвета')
    @pytest.mark.parametrize('color', [order_data_black, order_data_grey, order_data_multicolor, order_data_no_color])
    def test_create_order_with_color_field_success(self, color):
        payload = color
        response = requests.post(CREATE_ORDER, json=payload)
        assert response.status_code == 201 and 'track' in response.json()