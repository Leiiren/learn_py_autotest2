import requests

from configurations import SERVICE_URL
from src.baseclasses.get_company_response import Response
from src.pydantic_schemas.get_companies import GetCompanies


# resp = requests.get(SERVICE_URL)
# print(resp.json())

def test_getting_companies_list():
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    test_object.assert_status_code(201).validate(GetCompanies)