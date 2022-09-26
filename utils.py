import requests
from Config import api_secret, api_key


def get_bot_status():
    data = {
        "email": "hasnatali42@gmail.com",
        "password": "Admin#123"
    }

    login_response = requests.post("http://trading-bot-apis.herokuapp.com/api/login/", data=data).json()

    token = login_response["token"]["access"]

    headers = {
        'Authorization': f"Bearer {token}"
    }

    status = requests.get("http://trading-bot-apis.herokuapp.com/api/user_bot_status/", headers=headers).json()

    return status.get("is_bot_activate")


print(get_bot_status())
