# https://send-request.me/api/companies
# https://send-request.me/api/users
# https://send-request.me/

import requests
from configurations import SERVICE_URL
from src.enums.global_enums import GlobalErrorsMessages
import json


def test_getting_post():
    response = requests.get(url=SERVICE_URL)
    received_post = response.json()

    assert response.status_code == 200, GlobalErrorsMessages.WRONG_STASUS_CODE.value
    assert len(received_post) == 2, GlobalErrorsMessages.WRONG_ELEMENT_COUNT.value
    print(response.json())


def test_equal():
    assert 1 == 1, "Number is not equal to expected"