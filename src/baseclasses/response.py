# from jsonschema import validate
from src.enums.global_enums import GlobalErrorsMessages

# Здесь можно добавлять точечные ассерты, точечные проверки

class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json['data'], dict):
            for item in self.response_json['data']:
                schema.model_validate()
        else:
            schema.model_validate(self.response_json['data'][0])
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorsMessages.WRONG_STASUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorsMessages.WRONG_STASUS_CODE.value
        return self