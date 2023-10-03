import requests


BASE_URL_AUTH = "http://127.0.0.1:8000/auth/api/"


def save_data_from_bot(**data):
    path = BASE_URL_AUTH + "save/bot/data/"
    resp = requests.post(path, data)
    return resp


#
# def check_number(phone_number, tg_username, tg_chat_id):
#     endpoint = BASE_URL_AUTH + 'check/phone_number/'
#     data = {
#         "phone_number": phone_number,
#         "tg_username": tg_username,
#         "tg_chat_id": tg_chat_id,
#     }
#     return requests.post(endpoint, data)