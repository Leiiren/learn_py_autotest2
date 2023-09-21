# from jsonschema import validate
from src.enums.global_enums import GlobalErrorsMessages

# Здесь можно добавлять точечные ассерты, точечные проверки

class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get('data')
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, dict):
            for item in self.response_json:
                schema.model_validate()
        else:
            schema.model_validate(self.response_json[0])
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

# Волшебная функция для дебага
    def __str__(self):
        return \
            f"\nStatus Code: {self.response_status} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body: {self.response_json} \n"