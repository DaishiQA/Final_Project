# Пынтя Денис, 46-я когорта — Финальный проект. Инженер по тестированию расширенный.
import configuration
import data
import requests

# POST-запрос на создание заказа
def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body,
        headers=data.headers)

# GET-запрос на получение информации о заказе по трек-номеру
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH + str(track),
        headers=data.headers)

# Запуск автотеста на проверку заказа по номеру трека и проверки получения статуса кода 200
def test_get_order_info_by_track():
# Извлекаем номер трека из ответа (формат JSON)
    track = create_new_order(data.order_body).json()['track']
    response = get_order_by_track(track)
# Проверяем, что код ответа 200
    assert response.status_code == 200