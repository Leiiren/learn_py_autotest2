# https://send-request.me/api/companies
# https://send-request.me/

import requests
from configurations import SERVICE_URL


def test_getting_post():
    response = requests.get(url=SERVICE_URL)
    print(response.json())


def test_equal():
    assert 1 == 1, "Number is not equal to expected"