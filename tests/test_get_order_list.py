import allure
import requests
from test_data import GET_ORDERS

class TestGetOrders:
    @allure.title('Проверка успешного получения списка заказов')
    @allure.description('Проверка получения кода 200 Ok и списка заказов с id заказа при отправке GET-запроса '
                        'на получение списка заказов')
    def test_get_orders_list_success(self):
        response = requests.get(GET_ORDERS)
        assert (type(response.json()['orders']) == list
                and response.status_code == 200
                and 'id' in response.json()['orders'][0])