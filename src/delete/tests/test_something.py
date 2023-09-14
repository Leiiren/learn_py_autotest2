# https://send-request.me/api/companies
# https://send-request.me/api/users
# https://send-request.me/

import requests
from configurations import SERVICE_URL


def test_getting_post():
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200, 'Received status code is not equal to expected'
    print(response.json())


def test_equal():
    assert 1 == 1, "Number is not equal to expected"