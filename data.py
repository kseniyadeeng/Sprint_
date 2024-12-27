MAIN_URL='http://qa-scooter.praktikum-services.ru'
CREATE_COURIER = '/api/v1/courier'
LOGIN_COURIER = '/api/v1/courier/login'
CREATE_ORDER = '/api/v1/orders'
GET_ORDERS = '/api/v1/orders'

login_valid = 'harry_potter'
password_valid = '111111!'

order_data_grey = {
    "firstName": "Harry",
    "lastName": "Potter",
    "address": "Hogwarts",
    "metroStation": 4,
    "phone": "+7 905 555 75 65",
    "rentTime": 5,
    "deliveryDate": "2024-12-24",
    "comment": "Patronum",
    "color": [
        "GREY"
    ]
}

order_data_black = {
    "firstName": "Ron",
    "lastName": "Weasley",
    "address": "Hogwarts",
    "metroStation": 3,
    "phone": "+7 905 556 75 65",
    "rentTime": 5,
    "deliveryDate": "2024-12-24",
    "comment": "No",
    "color": [
        "GREY"
    ]
}

order_data_multicolor = {
    "firstName": "Hermione",
    "lastName": "Granger",
    "address": "Hogwarts",
    "metroStation": 3,
    "phone": "+7 905 555 75 68",
    "rentTime": 1,
    "deliveryDate": "2024-12-24",
    "comment": "I know everything",
    "color": [
        "GREY", "BLACK"
    ]
}

order_data_no_color = {
    "firstName": "Tom",
    "lastName": "Riddle",
    "address": "Azkaban",
    "metroStation": 3,
    "phone": "+7 905 555 09 88",
    "rentTime": 4,
    "deliveryDate": "2024-12-24",
    "comment": "Harry Potter",
    "color": []
}