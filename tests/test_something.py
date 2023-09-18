import requests

from configurations import SERVICE_URL
from jsonschema import validate

from src.schemas.post import POST_SCHEMA_GET_COMPANIES
from src.baseclasses.response import Response

def test_getting_post():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(POST_SCHEMA_GET_COMPANIES)
    print('response:', response.response_json['data'])
    print('status_code:', response.response_status)
